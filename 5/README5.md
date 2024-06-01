# Dashboard Integration
## Description
The dashboard integration is a project designed to read ekg-data, create a plot, and add some other features (listed below) to an application on a locahost webiste.
## Features
- Reads datas from `person_db.json` (name, age, ekgs,.) with `person.py` and interpretes the ekg with ekgdata.py
- Creates a plot (ekgdata).
- Adds the plot to the application.
- Creates a chart of the heartrate over time and shows max heartrate.
- On the website you can choose the patient and decide which ekg of him to show. There's also a second tab to access patient data or ekgs via an ID.
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
    streamlit run 5/main.py
    ```
5. You can now view your streamlit app in your browser.
6. Choose the patient on the first tab or enter an ID to the second tab 
## Screenshot of the app
![image](https://github.com/TobiW03/Aufgabe3-5/blob/01092b3624978cf34fef92ec5cbefc47c646f317/5/ScreenshotTab1.png)
![image](https://github.com/TobiW03/Aufgabe3-5/blob/01092b3624978cf34fef92ec5cbefc47c646f317/5/ScreenshotTab2.png)