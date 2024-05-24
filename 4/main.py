import streamlit as st
import read_pandas
import my_plot
#Streamlit Einstellungen
st.header("Power-Curve log.")
#Daten einlesen und weitergeben
df = read_pandas.read_my_csv_Activity()
#Plot erstellen
fig = my_plot.PowerCurve1(df)
fig2 = my_plot.PowerCurve2(df)
#Plot anzeigen
st.plotly_chart(fig)
st.header("Power-Curve linear.")
st.plotly_chart(fig2)