# Paket für Bearbeitung von Tabellen
import pandas as pd
import scipy as sp
import numpy as np

def read_my_csv():
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

def find_best_effort(df,timeintv,fs): #fs = sampling frequency pro sekunde, timeintv = Zeitintervall in Sekunden
    window_size = int(timeintv * (1/fs))
    rolling_avg = df["PowerOriginal"].rolling(window=(window_size)).mean()
    return rolling_avg.max()

def create_pow_curve(df,Intervals,fs):
    ListPowCurve=[]
    for element in Intervals:
        ListPowCurve.append([find_best_effort(df,element,fs),element])
    dfPowerCurve = pd.DataFrame(ListPowCurve, columns=['Leistung in W', 'Zeit in s'])
    return dfPowerCurve