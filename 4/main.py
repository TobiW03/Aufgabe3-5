import streamlit as st
import read_pandas
import my_plot
#Streamlit Einstellungen
st.header("Power-Curve")
#Daten einlesen und weitergeben
df = read_pandas.read_my_csv_Activity()
#Plot erstellen
fig = my_plot.PowerCurve(df)
#Plot anzeigen
st.plotly_chart(fig)