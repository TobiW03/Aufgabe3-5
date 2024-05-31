import streamlit as st
import read_person_data
import ekgdata
from PIL import Image
import person

# Zu Beginn
# Lade alle Personen
person_data = read_person_data.load_person_data()
person_names = read_person_data.get_person_list(person_data)
ekg_data = None

tab1, tab2 = st.tabs(["EKG-Data", "ID-Informationen"])
with tab1:

    # Anlegen diverser Session States
    ## Gewählte Versuchsperson
    if 'aktuelle_versuchsperson' not in st.session_state:
        st.session_state.aktuelle_versuchsperson = 'None'

    ## Anlegen des Session State. Bild, wenn es kein Bild gibt
    if 'picture_path' not in st.session_state:
        st.session_state.picture_path = 'data/pictures/none.jpg'

    # Design des Dashboards
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
        # Weitere Daten wie Geburtsdatum etc. anzeigen
        if st.session_state.aktuelle_versuchsperson in person_names:
            st.session_state.picture_path = read_person_data.find_person_data_by_name(
                st.session_state.aktuelle_versuchsperson)["picture_path"]

            Patients = person.Person.load_person_data()
            for patient in Patients:
                if patient["lastname"] + ", " + patient["firstname"] == st.session_state.aktuelle_versuchsperson:
                    current_person = person.Person(patient)
                    break
            st.header("Pat-Daten")
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
            option = st.radio("EKG auswählen: ", (1, 2))
            current_ekg = ekgdata.EKGdata(current_person.ecg_data[option-1])
        else:
            current_ekg = ekgdata.EKGdata(current_person.ecg_data[0])
        st.write("Geschätzte Herzfrequenz: ", int(current_ekg.estimated_hr))

        # EKG-Daten als Plotly Plot anzeigen
        st.plotly_chart(current_ekg.fig)
    else:
        st.write("Bitte wählen Sie eine Versuchsperson aus.")

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        # ID Daten Ausgabe
        IDInputPers = st.text_input("ID eingeben; Personendaten", "0")
        if IDInputPers != "0":
            # Suche nach der Person mit der eingegebenen ID
            id_person = None
            for patient in person_data:
                if str(patient["id"]) == IDInputPers:
                    id_person = person.Person(patient)
                    break
            
            if id_person:
                st.write("Nachname: ", id_person.lastname)
                st.write("Vorname: ", id_person.firstname)
                st.write("ID: ", id_person.id)
                st.write("Geburtsjahr: ", id_person.date_of_birth)
                st.write("Alter: ", id_person.age)
                st.write("Maximale Herzfrequenz: ", id_person.maxHR)
                st.write("EKG Daten: ", id_person.ecg_data)
            else:
                st.write("ID nicht gefunden.")

    with col2:
        # ID eingeben für EKG-Daten
        # ID eingeben für EKG-Daten
        id_input = st.text_input("ID eingeben für EKG-Daten", "0")
        if id_input != "0":
            # Suche nach der EKG-Daten mit der eingegebenen ID
            ekg_data = None
            for counter in range(3):
                for ekg_test in person_data[counter]["ekg_tests"]:
                    if str(ekg_test["id"]) == id_input:
                        ekg_data = ekg_test
                        break
            
            # Falls die EKG-Daten gefunden wurden
        if ekg_data:
            # Ausgabe der EKG-Daten
            st.write("EKG-Daten für ID:", ekg_data["id"])
            st.write("Datum:", ekg_data["date"])
            st.write("Ergebnis Link:", ekg_data["result_link"])
            current_ekg = ekgdata.EKGdata(ekg_data)
            st.write("Geschätzte Herzfrequenz:", int(current_ekg.estimated_hr))    
        else:
            st.write("EKG-Daten für ID nicht gefunden.")

    # Laden und Anzeigen der EKG-Daten
    if ekg_data == None:
        pass
    else:

        st.plotly_chart(current_ekg.fig)