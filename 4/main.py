import streamlit as st
import read_pandas
import my_plot
#Daten einlesen und weitergeben
df = read_pandas.read_my_csv_Activity()
#figures for streamlit
fig = my_plot.PowerCurve1(df)
fig2 = my_plot.PowerCurve2(df)
#streamlit
st.header("Power-Curve log.")
st.plotly_chart(fig)
st.header("Power-Curve linear")
st.plotly_chart(fig2)