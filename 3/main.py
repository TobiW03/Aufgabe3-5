import streamlit as st
import read_pandas
import my_plot

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

    col1, col2 = st.columns(2)

    with col1:
        st.header("Power-Data")
        st.write("# My Plot")

        fig = my_plot.PowerPlot()

        st.plotly_chart(fig)
    with col2:
        HRMAX = 193
        #Mittelwert & Maximalwert
        MWP,MaxP = read_pandas.maths_activity((read_pandas.read_my_csv_Activity()['PowerOriginal']))
        #5 Zonen HF
        Hrmax1,Hrmax2,Hrmax3,Hrmax4,Hrmax5 = read_pandas.HR_Zones((read_pandas.read_my_csv_Activity()['HeartRate']),HRMAX)
        #Zeit in den 5 Zonen
        Time1,Time2,Time3,Time4,Time5 = read_pandas.mean_time_Zone(read_pandas.create_table(read_pandas.read_my_csv_Activity(),
            read_pandas.HR_Zones_Filter((read_pandas.read_my_csv_Activity()['HeartRate']),HRMAX)))
        #Durchschnittliche Leistung pro Zohne
        MeanPowerValuesZones = read_pandas.mean_Power_Zones_Values(read_pandas.create_table(read_pandas.read_my_csv_Activity(),
            read_pandas.HR_Zones_Filter((read_pandas.read_my_csv_Activity()['HeartRate']),HRMAX)))
        #Datenausgabe Streamlit
        st.write(f"Mittelwert: {MWP:.2f}BPM, Maximum: {MaxP:.2f}BPM.")
        st.write(f"Zoneneinteilung: {Hrmax1:.2f}-{Hrmax2:.2f}BPM, {Hrmax2:.2f}-{Hrmax3:.2f}BPM, {Hrmax3:.2f}-{Hrmax4:.2f}BPM, {Hrmax4:.2f}-{Hrmax5:.2f}BPM und > {Hrmax5:.2f}BPM.")
        st.write(f"Zeiten pro Zone {Time1:.2f}s, {Time2:.2f}s, {Time3:.2f}s, {Time4:.2f}s, {Time5:.2f}s.")
        st.write(f"Durchschnittliche Leistung pro Zone: {MeanPowerValuesZones[0]:.2f}, {MeanPowerValuesZones[1]:.2f}, {MeanPowerValuesZones[2]:.2f}, {MeanPowerValuesZones[3]:.2f}, {MeanPowerValuesZones[4]:.2f}")
        

