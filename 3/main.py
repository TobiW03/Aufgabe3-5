import streamlit as st
import read_pandas
import my_plot
import pandas as pd

# Wo startet sie Zeitreihe
# Wo endet sich
# Was ist die Maximale und Minimale Spannung
# Grafik
tab1, tab2 = st.tabs(["EKG-Data", "Power-Data"])

with tab1:
    st.header("EKG-Data")
    st.write("# My Plot")

    df = read_pandas.read_my_csv_EKG()
    fig = read_pandas.make_plot(df)

    st.plotly_chart(fig)

with tab2:
                 
    st.header("Power-Data")
    st.write("# My Plot")

    fig = my_plot.PowerPlot()

    st.plotly_chart(fig)
    
    st.header("Messwerte")
    #Standardwert
    HRMAX = read_pandas.read_my_csv_Activity()['HeartRate'].max()
    #Variabler Wert
    HRInput = st.number_input("Geben Sie einen Wert ein:", value=HRMAX)
    #Mittelwert & Maximalwert

    MWP,MaxP = read_pandas.maths_activity((read_pandas.read_my_csv_Activity()['PowerOriginal']))
    #5 Zonen HF
    Hrmax1,Hrmax2,Hrmax3,Hrmax4,Hrmax5 = read_pandas.HR_Zones((read_pandas.read_my_csv_Activity()['HeartRate']),HRInput)
    #Zeit in den 5 Zonen
    Time1,Time2,Time3,Time4,Time5 = read_pandas.mean_time_Zone(read_pandas.create_table(read_pandas.read_my_csv_Activity(),
        read_pandas.HR_Zones_Filter((read_pandas.read_my_csv_Activity()['HeartRate']),HRInput)))
    #Durchschnittliche Leistung pro Zohne
    MeanPowerValuesZones = read_pandas.mean_Power_Zones_Values(read_pandas.create_table(read_pandas.read_my_csv_Activity(),
        read_pandas.HR_Zones_Filter((read_pandas.read_my_csv_Activity()['HeartRate']),HRInput)))
    #Datenausgabe Streamlit
    st.write(f"Mittelwert: {MWP:.2f}BPM, Maximum: {MaxP:.2f}BPM.")
    #Tabelle
    datatabel = {
    'Spalte 1': [(str(round(Hrmax1,2)) + "-" + str(round(Hrmax2,2))), (str(round(Hrmax2,2)) + "-" + str(round(Hrmax3,2))), (str(round(Hrmax3,2)) + "-" + str(round(Hrmax4,2))), (str(round(Hrmax4,2)) + "-" + str(round(Hrmax5,2))), ("> " + str(round(Hrmax5,2)))],
    'Spalte 2': [round(Time1,2), round(Time2,2), round(Time3,2), round(Time4,2), round(Time5,2)],
    'Spalte 3': [round(MeanPowerValuesZones[0],2), round(MeanPowerValuesZones[1],2), round(MeanPowerValuesZones[2],2), round(MeanPowerValuesZones[3],2), round(MeanPowerValuesZones[4],2)],
    }
    dftable = pd.DataFrame(datatabel)
    dftable.columns = ["Zoneneinteilung [BPM]", "Zeiten Pro Zone [s]", "Durchschnittliche Leistung pro Zone [W]"]
    st.table(dftable)