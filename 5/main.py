import streamlit as st
import read_person_data
import ekgdata
from PIL import Image
import person

#%% Zu Beginn
# Lade alle Personen
person_names = read_person_data.get_person_list(read_person_data.load_person_data())

# Anlegen diverser Session States
## Gewählte Versuchsperson
if 'aktuelle_versuchsperson' not in st.session_state:
    st.session_state.aktuelle_versuchsperson = 'None'

## Anlegen des Session State. Bild, wenn es kein Bild gibt
if 'picture_path' not in st.session_state:
    st.session_state.picture_path = 'data/pictures/none.jpg'

## TODO: Session State für Pfad zu EKG Daten

#%% Design des Dashboards
# Schreibe die Überschrift
st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

# Auswahlbox, wenn Personen anzulegen sind
st.session_state.aktuelle_versuchsperson = st.selectbox(
    'Versuchsperson',
    options=person_names, key="sbVersuchsperson")

# Name der Versuchsperson
st.write("Der Name ist: ", st.session_state.aktuelle_versuchsperson)

col1, col2 = st.columns(2)

with col1:
    # TODO: Weitere Daten wie Geburtsdatum etc. schön anzeigen
    if st.session_state.aktuelle_versuchsperson in person_names:
        st.session_state.picture_path = read_person_data.find_person_data_by_name(
            st.session_state.aktuelle_versuchsperson)["picture_path"]
        
        Patients = person.Person.load_person_data()
        for patient in Patients:
            if patient["lastname"] + ", " + patient["firstname"] == st.session_state.aktuelle_versuchsperson:
                current_person = person.Person(patient)
                break
        st.header("Personendaten")
        st.write("Nachname: ", current_person.lastname)
        st.write("Vorname: ", current_person.firstname)
        st.write("ID: ", current_person.id)
        st.write("Geburtsjahr: ", current_person.date_of_birth)
        st.write("Alter: ", current_person.age)
        st.write("Maximale Herzfrequenz: ", current_person.maxHR)
        st.write("EKG Daten: ", current_person.ecg_data)

with col2:
    # Bild anzeigen
    image = Image.open(st.session_state.picture_path)
    st.image(image, caption=st.session_state.aktuelle_versuchsperson)

# Öffne EKG-Daten
if 'current_person' in locals():
    if len(current_person.ecg_data) > 1:
        option = st.radio("Wähle welches EKG: ", (1, 2))
        current_ekg = ekgdata.EKGdata(current_person.ecg_data[option-1])
    else:
        current_ekg = ekgdata.EKGdata(current_person.ecg_data[0])
    st.write("Geschätzte Herzfrequenz: ", int(current_ekg.estimated_hr))

    # EKG-Daten als Plotly Plot anzeigen
    st.plotly_chart(current_ekg.fig)
else:
    st.write("Bitte wählen Sie eine Versuchsperson aus.")