import streamlit as st
import read_pandas
import my_plot


st.header("Power-Curve")

df = read_pandas.read_my_csv_Activity()
fig = my_plot.PowerCurve(df)

st.plotly_chart(fig)

