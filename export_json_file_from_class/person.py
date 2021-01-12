from data import COMPLETE_NAME, FIRST_NAME, LAST_NAME, AGE, GENDER, OCCUPATION, COUNTRY

class Person:
    
    def __init__(self, complete_name, first_name, last_name, age, gender, occupation, country):
        self.complete_name = complete_name
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.country = country

person = Person(COMPLETE_NAME, FIRST_NAME, LAST_NAME, AGE, GENDER, OCCUPATION, COUNTRY)
