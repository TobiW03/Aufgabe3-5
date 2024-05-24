# Interactive Power Plot
## Description
The Interactive Power Plot is a project designed to read data, create a plot, and add some other features (listed below) to an application.
## Features
- Reads data from `activity.csv` with `pd.read_csv`
- Creates a plot (my_plot.py).
- Adds the plot to the application.
- Enables an input to define the `MAXHR`.
- Shows minimum and maximum heartrate, and defines five `HR-zones`, based on the input.
- Shows how much time is spent in each zone and the average power in each zone.
## How to Use
1. Clone this repository to your local machine.
    ```bash
    git clone https://github.com/TobiW03/Aufgabe3-5
    ```
2. Make sure you have Python installed.
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. To execute the project, run:
     ```bash
    streamlit run 3/main.py
    ```
5. You can now view your streamlit app in your browser.
6. Input the desired `MAXHR` in the provided input box. 
## Screenshot of the app
![image](https://github.com/TobiW03/Aufgabe3-5/assets/163830822/08aa6e5e-cb8c-4617-a04b-774c6d32d8b6)



