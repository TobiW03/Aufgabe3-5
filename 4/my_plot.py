import pandas as pd
import scipy as sp
import numpy as np
import plotly.express as px
from read_pandas import read_my_csv_Activity, create_pow_curve

def PowerCurve1(datas):
    #Daten einlesen
    arr = np.arange(1, len(datas["PowerOriginal"]))
    #Plot erstellen
    var = create_pow_curve(datas,arr,1)
    fig = px.line(datas, x = var["Zeit in s"], y = var["Leistung in W"])
    fig.update_layout(xaxis_title='Time [s]', yaxis_title='Power [W]')
    fig.update_layout(xaxis=dict(type='log', title='Time [s]'))
    return fig
def PowerCurve2(datas):
    #Daten einlesen
    arr = np.arange(1, len(datas["PowerOriginal"]))
    #Plot erstellen
    var = create_pow_curve(datas,arr,1)
    fig = px.line(datas, x = var["Zeit in s"], y = var["Leistung in W"])
    fig.update_layout(xaxis_title='Time [s]', yaxis_title='Power [W]')
    return fig


