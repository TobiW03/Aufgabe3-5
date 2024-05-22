# Paket für Bearbeitung von Tabellen
import pandas as pd
# Paket
import plotly.express as px
#EKG
def read_my_csv_EKG():
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    df = pd.read_csv("data/ekg_data/01_Ruhe.txt", sep="\t", header=None)

    # Setzt die Columnnames im Dataframe
    df.columns = ["Messwerte in mV","Zeit in ms"]
    
    # Gibt den geladen Dataframe zurück
    return df

def make_plot(df):

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df.head(2000), x= "Zeit in ms", y="Messwerte in mV")
    return fig

def read_my_csv_Activity():
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    
    column_names = ["Duration","Distance","OriginalPace","HeartRate","Cadence","PowerOriginal","CalculatedPace","CalculatedStrideLength","CalculatedAerobicEfficiencyPace","CalculatedAerobicEfficiencyPower","CalculatedEfficiencyIndex"]
    df = pd.read_csv("data/activities/activity.csv", sep=",", header=None,skiprows=1, usecols=range(11), names=column_names)

    # Setzt die Columnnames im Dataframe
    #df.columns = ["Messwerte in mV","Zeit in ms"]
    
    # Gibt den geladen Dataframe zurück
    return df

def maths_activity(power):
    power_mean = power.mean(numeric_only=True)
    power_max = power.max(numeric_only=True)
    return power_mean, power_max

def HR_Zones(Heartrate,HR_Max):
    HR_Max = Heartrate.max(numeric_only=True)
    HR_Zone1 = HR_Max * 0.65
    HR_Zone2 = HR_Max * 0.75
    HR_Zone3 = HR_Max * 0.85
    HR_Zone4 = HR_Max * 0.95
    HR_Zone5 = HR_Max * 1
    return HR_Zone1, HR_Zone2, HR_Zone3, HR_Zone4, HR_Zone5

def HR_Zones_Filter(Heartrate,HR_Max):
    HR_Zone1, HR_Zone2, HR_Zone3, HR_Zone4, HR_Zone5 = HR_Zones(Heartrate,HR_Max)
    HR_Zone1_Filter = Heartrate <= HR_Zone1
    HR_Zone2_Filter = (Heartrate > HR_Zone1) & (Heartrate <= HR_Zone2)
    HR_Zone3_Filter = (Heartrate > HR_Zone2) & (Heartrate <= HR_Zone3)
    HR_Zone4_Filter = (Heartrate > HR_Zone3) & (Heartrate <= HR_Zone4)
    HR_Zone5_Filter = (Heartrate > HR_Zone4)
    return HR_Zone1_Filter, HR_Zone2_Filter, HR_Zone3_Filter, HR_Zone4_Filter, HR_Zone5_Filter

def HR_Zones_Filter_Values(Heartrate,HR_Max):
    HR_Zone1, HR_Zone2, HR_Zone3, HR_Zone4, HR_Zone5 = HR_Zones(Heartrate,HR_Max)
    HR_Zone1_Filter = Heartrate[Heartrate <= HR_Zone1]
    HR_Zone2_Filter = Heartrate[(Heartrate > HR_Zone1) & (Heartrate <= HR_Zone2)]
    HR_Zone3_Filter = Heartrate[(Heartrate > HR_Zone2) & (Heartrate <= HR_Zone3)]
    HR_Zone4_Filter = Heartrate[(Heartrate > HR_Zone3) & (Heartrate <= HR_Zone4)]
    HR_Zone5_Filter = Heartrate[(Heartrate > HR_Zone4)]
    return HR_Zone1_Filter, HR_Zone2_Filter, HR_Zone3_Filter, HR_Zone4_Filter, HR_Zone5_Filter

def mean_HR_Zones_Values(Heartrate,HR_Max):
    Values = HR_Zones_Filter_Values(Heartrate,HR_Max)
    HR_Zone1_Mean = Values[0].mean(numeric_only=True)
    HR_Zone2_Mean = Values[1].mean(numeric_only=True)
    HR_Zone3_Mean = Values[2].mean(numeric_only=True)
    HR_Zone4_Mean = Values[3].mean(numeric_only=True)
    HR_Zone5_Mean = Values[4].mean(numeric_only=True)
    return HR_Zone1_Mean, HR_Zone2_Mean, HR_Zone3_Mean, HR_Zone4_Mean, HR_Zone5_Mean

def mean_Power_Zones_Values(df):
    dfZ1 = df[df["FilterHRZone1"] == True]
    dfZ2 = df[df["FilterHRZone2"] == True]
    dfZ3 = df[df["FilterHRZone3"] == True]
    dfZ4 = df[df["FilterHRZone4"] == True]
    dfZ5 = df[df["FilterHRZone5"] == True]
    
    # Berechne den Mittelwert der "PowerOriginal"-Spalte für jede gefilterte DataFrame
    PowerMean_Zone1 = dfZ1["PowerOriginal"].mean()
    PowerMean_Zone2 = dfZ2["PowerOriginal"].mean()
    PowerMean_Zone3 = dfZ3["PowerOriginal"].mean()
    PowerMean_Zone4 = dfZ4["PowerOriginal"].mean()
    PowerMean_Zone5 = dfZ5["PowerOriginal"].mean()
    return PowerMean_Zone1, PowerMean_Zone2, PowerMean_Zone3, PowerMean_Zone4, PowerMean_Zone5

def mean_time_Zone(df):
    dfZ1 = df[df["FilterHRZone1"] == True]
    dfZ2 = df[df["FilterHRZone2"] == True]
    dfZ3 = df[df["FilterHRZone3"] == True]
    dfZ4 = df[df["FilterHRZone4"] == True]
    dfZ5 = df[df["FilterHRZone5"] == True]
    return len(dfZ1), len(dfZ2), len(dfZ3), len(dfZ4), len(dfZ5)

def create_table(Activity,HRZonesFilters):
    df_test = pd.DataFrame({
    'Duration': Activity['Duration'],
    'PowerOriginal': Activity['PowerOriginal'],
    'FilterHRZone1': HRZonesFilters[0],
    'FilterHRZone2': HRZonesFilters[1],
    'FilterHRZone3': HRZonesFilters[2],
    'FilterHRZone4': HRZonesFilters[3],
    'FilterHRZone5': HRZonesFilters[4],
    })
    return df_test

if __name__ == "__main__":
    Activity = read_my_csv_Activity()
    HRMAX = 193
    Activity = read_my_csv_Activity()
    HRZonesFilters = HR_Zones_Filter(Activity['HeartRate'],HRMAX)
    df_table_Filters = create_table(Activity,HRZonesFilters)
    Mean_HRValues_Zones = mean_HR_Zones_Values(Activity['HeartRate'],193)
    MeanPowerValuesZones = mean_Power_Zones_Values(df_table_Filters)
    MeanTimePerFilter = mean_time_Zone(df_table_Filters)