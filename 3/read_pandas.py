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

def HR_Zones(Heartrate):
    HR_Max = Heartrate.max(numeric_only=True)
    HR_Zone1 = HR_Max * 0.2
    HR_Zone2 = HR_Max * 0.4
    HR_Zone3 = HR_Max * 0.6
    HR_Zone4 = HR_Max * 0.8
    HR_Zone5 = HR_Max * 1
    return HR_Zone1, HR_Zone2, HR_Zone3, HR_Zone4, HR_Zone5

def HR_Zones_Filter(Heartrate):
    HR_Zone1, HR_Zone2, HR_Zone3, HR_Zone4, HR_Zone5 = HR_Zones(Heartrate)
    HR_Zone1_Filter = Heartrate <= HR_Zone1
    HR_Zone2_Filter = (Heartrate > HR_Zone1) & (Heartrate <= HR_Zone2)
    HR_Zone3_Filter = (Heartrate > HR_Zone2) & (Heartrate <= HR_Zone3)
    HR_Zone4_Filter = (Heartrate > HR_Zone3) & (Heartrate <= HR_Zone4)
    HR_Zone5_Filter = (Heartrate > HR_Zone4) & (Heartrate <= HR_Zone5)
    return HR_Zone1_Filter, HR_Zone2_Filter, HR_Zone3_Filter, HR_Zone4_Filter, HR_Zone5_Filter

def HR_Zones_Filter_Values(Heartrate):
    HR_Zone1, HR_Zone2, HR_Zone3, HR_Zone4, HR_Zone5 = HR_Zones(Heartrate)
    HR_Zone1_Filter = Heartrate[Heartrate <= HR_Zone1]
    HR_Zone2_Filter = Heartrate[(Heartrate > HR_Zone1) & (Heartrate <= HR_Zone2)]
    HR_Zone3_Filter = Heartrate[(Heartrate > HR_Zone2) & (Heartrate <= HR_Zone3)]
    HR_Zone4_Filter = Heartrate[(Heartrate > HR_Zone3) & (Heartrate <= HR_Zone4)]
    HR_Zone5_Filter = Heartrate[(Heartrate > HR_Zone4) & (Heartrate <= HR_Zone5)]
    return HR_Zone1_Filter, HR_Zone2_Filter, HR_Zone3_Filter, HR_Zone4_Filter, HR_Zone5_Filter

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



#Test
if __name__ == "__main__":
    Activity = read_my_csv_Activity()
    HRZonesFilters = HR_Zones_Filter(Activity['HeartRate'])
    df_table_Filters = create_table(Activity,HRZonesFilters)