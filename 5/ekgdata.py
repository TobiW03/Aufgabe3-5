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
        self.peaks,self.properties = self.find_peaks_ekg()
        self.estimated_hr = self.estimate_hr()
        self.fig = self.plot_time_series()

    def find_peaks_ekg(self):
        peaks, properties = find_peaks(self.df['EKG in mV'], height=340, distance=20)
        return peaks,properties
    
    def estimate_hr(self):
        estimated_hr = ((len(self.peaks)) / (len(self.df['Time in ms'])/1000)*60)
        return estimated_hr
    
    def plot_time_series(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=self.df['Time in ms'], y=self.df['EKG in mV'], mode='lines', name='EKG Signal'))
        fig.add_trace(go.Scatter(x=self.df['Time in ms'][self.peaks], y=self.df['EKG in mV'][self.peaks], mode='markers', name='Peaks', marker=dict(color='red', size=10, symbol='x')))
        fig.update_layout(title='Peaks im EKG-Signal',
            xaxis_title='Zeit [s]',
            yaxis_title='Amplitude',
            showlegend=True)
        return fig
        
            
    def load_by_id(self, id):
        if id == self.id:
            print(self.__dict__)
        else:
            print("ID not found")




if __name__ == "__main__":
    print("This is a module with some functions to read the EKG data")
    file = open("data/person_db.json")
    person_data = json.load(file)
    ekg_dict = person_data[0]["ekg_tests"][0]
    #print(ekg_dict)
    ekg = EKGdata(ekg_dict)
    #ekg.load_by_id(1)
    #ekg.find_peaks()
    #ekg.estimate_hr()
    #ekg.plot_time_series()