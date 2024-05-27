import json
from datetime import datetime

class Person:
    @staticmethod
    def load_person_data():
        """A Function that knows where the person Database is and returns a Dictionary with the Persons"""
        file = open("data/person_db.json")
        person_data = json.load(file)
        return person_data

    @staticmethod
    def get_person_list(person_data):
        """A Function that takes the persons-dictionary and returns a list auf all person names"""
        list_of_names = []

        for eintrag in person_data:
            list_of_names.append(eintrag["lastname"] + ", " +  eintrag["firstname"])
        return list_of_names
    
    @staticmethod
    def find_person_data_by_name(suchstring):
        """ Eine Funktion der Nachname, Vorname als ein String übergeben wird
        und die die Person als Dictionary zurück gibt"""

        person_data = Person.load_person_data()
        #print(suchstring)
        if suchstring == "None":
            return {}

        two_names = suchstring.split(", ")
        vorname = two_names[1]
        nachname = two_names[0]

        for eintrag in person_data:
            if (eintrag["lastname"] == nachname and eintrag["firstname"] == vorname):
                print()

                return eintrag
        else:
            return {}
        
    def __init__(self, person_dict) -> None:
        self.date_of_birth = person_dict["date_of_birth"]
        self.firstname = person_dict["firstname"]
        self.lastname = person_dict["lastname"]
        self.picture_path = person_dict["picture_path"]
        self.id = person_dict["id"]

    def calc_age(self):
        date = datetime.now()
        print(date)
        currentyear = date.year
        self.age = currentyear - self.date_of_birth

    def calc_max_heart_rate(self):
        self.maxHR = 220-self.age

    def load_by_id(self, ID):
        if ID == self.id:
            print(self.__dict__)
        else:
            print("Wrong ID, try again")

if __name__ == "__main__":
    print("This is a module with some functions to read the person data")
    persons = Person.load_person_data()
    person_names = Person.get_person_list(persons)
    print(person_names)
    Person1 = Person(persons[0])
    Person1.calc_age()
    Person1.calc_max_heart_rate()
    Person1.load_by_id(1)
    #print(Person.find_person_data_by_name("Huber, Julian"))