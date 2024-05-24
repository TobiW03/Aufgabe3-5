import pandas as pd
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from read_pandas import read_my_csv_Activity, create_pow_curve

def PowerCurve():
    #Daten einlesen
    datas = read_my_csv_Activity()
    arr = np.arange(1, len(datas["PowerOriginal"]))
    #Plot erstellen
    plt.plot(arr,(create_pow_curve(datas,arr,1)))
    plt.xlabel("Time [s]")
    plt.ylabel("Power [W]")
    plt.title("Power Curve")
    plt.legend(["Power"])
    plt.xlim(0, len(datas["PowerOriginal"]))
    plt.grid()
    plt.show()

PowerCurve()
