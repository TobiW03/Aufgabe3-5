Sure, here is a concise version of the README in English:
Power Curve Analysis with Streamlit and Plotly

This project visualizes power data from a CSV file, displaying a power curve with interactive features.
Prerequisites

Install the required Python packages:

bash

pip install pandas scipy numpy plotly streamlit

Modules and Functions
read_pandas.py

    read_my_csv(): Reads EKG data and returns a DataFrame.
    make_plot(df): Creates a plot of the first 2000 EKG values.
    read_my_csv_Activity(): Reads activity data and returns a DataFrame.
    find_best_effort(df, timeintv, fs): Calculates the best power value for a given interval.
    create_pow_curve(df, Intervals, fs): Creates a power curve based on given intervals.

my_plot.py
    PowerCurve(datas): Creates a power curve plot using Plotly.

app.py
    Entry point for the Streamlit app. Reads data, creates the power curve, and displays it.

Usage
    Ensure your CSV files are in the correct directories (data/activities/activity.csv and data/ekg_data/01_Ruhe.txt).
    Run the Streamlit app:

    streamlit run app.py

Open the provided link in your browser to view the power curve analysis

written with the help of chatgpt