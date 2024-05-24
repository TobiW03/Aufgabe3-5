import pandas as pd
import scipy as sp
import numpy as np
import plotly.express as px
from read_pandas import read_my_csv_Activity, create_pow_curve

def PowerCurve(datas):
    #Daten einlesen
    #datas = read_my_csv_Activity()
    arr = np.arange(1, len(datas["PowerOriginal"]))
    #Plot erstellen
    #plt.plot(arr,(create_pow_curve(datas,arr,1)))
    var = create_pow_curve(datas,arr,1)
    #plt.plot(var['Zeit in s'],var['Leistung in W'])
    fig = px.line(datas, x = var["Zeit in s"], y = var["Leistung in W"])
    fig.update_layout(title='Power Curve', xaxis_title='Time [s]', yaxis_title='Power [W]')

    #plt.xlabel("Time [s]")
    #plt.ylabel("Power [W]")
    #plt.title("Power Curve")
    #plt.legend(["Power"])
    #plt.xlim(0, len(datas["PowerOriginal"]))
    #plt.grid()
    return fig

PowerCurve()
