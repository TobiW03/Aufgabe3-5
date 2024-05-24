import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from read_pandas import read_my_csv_Activity

def PowerPlot():
    #Daten einlesen
    Activity = read_my_csv_Activity()
    #Time-Spalte erstellen
    durationsum = sum(Activity['Duration'])
    time = np.arange(0,durationsum)
    column_names = ["Duration","Distance","OriginalPace","HeartRate","Cadence","PowerOriginal","CalculatedPace","CalculatedStrideLength","CalculatedAerobicEfficiencyPace","CalculatedAerobicEfficiencyPower","CalculatedEfficiencyIndex"]
    df = pd.read_csv("data/activities/activity.csv", sep=",", header=None,skiprows=1, usecols=range(11), names=column_names)
    df["Time"] = time
    #Plot erstellen
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Time'], y=df['PowerOriginal'], mode='lines', name='PowerOriginal', yaxis='y1'))
    fig.add_trace(go.Scatter(x=df['Time'], y=df['HeartRate'], mode='lines', name='HeartRate', yaxis='y2'))
    fig.update_layout(title='Power and HeartRate over Time', xaxis_title='Time in s', yaxis_title='Power in W', yaxis2=dict(title='HeartRate in BPM', overlaying='y', side='right'))
    return fig