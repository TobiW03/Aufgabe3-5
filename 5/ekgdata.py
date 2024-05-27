import json
import pandas as pd
from scipy.signal import find_peaks
import plotly.express as px
import plotly.graph_objects as go

# %% Objekt-Welt

# Klasse EKG-Data für Peakfinder, die uns ermöglicht peaks zu finden

class EKGdata:

## Konstruktor der Klasse soll die Daten einlesen

    def __init__(self, ekg_dict):
        pass
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.data = ekg_dict["result_link"]
        self.df = pd.read_csv(self.data, sep='\t', header=None, names=['EKG in mV','Time in ms',])
    
    def find_peaks(self):
        self.peaks, self.properties = find_peaks(self.df['EKG in mV'], height=340, distance=20)

    def estimate_hr():
        

    def plot_time_series():
        pass
            
    def load_by_id(self, id):
        if id == self.id:
            print(self.__dict__)
        else:
            print("ID not found")

    def plot(self):
        self.fig = go.Figure()
        self.fig.add_trace(go.Scatter(x=self.df['Time in ms'], y=self.df['EKG in mV'], mode='lines', name='EKG Signal'))
        self.fig.add_trace(go.Scatter(x=self.df['Time in ms'][self.peaks], y=self.df['EKG in mV'][self.peaks], mode='markers', name='Peaks', marker=dict(color='red', size=10, symbol='x')))
        self.fig.update_layout(title='Peaks im EKG-Signal',
            xaxis_title='Zeit [s]',
            yaxis_title='Amplitude',
            showlegend=True)
        self.fig.show()



if __name__ == "__main__":
    print("This is a module with some functions to read the EKG data")
    file = open("data/person_db.json")
    person_data = json.load(file)
    ekg_dict = person_data[0]["ekg_tests"][0]
    #print(ekg_dict)
    ekg = EKGdata(ekg_dict)
    ekg.load_by_id(1)
    ekg.find_peaks()
    ekg.plot()
