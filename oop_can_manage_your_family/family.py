import os.path
import json

class Person():

    # class attributes
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]

    # constructor
    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):

        if id < 0 or not isinstance(id, int):
            raise Exception("id is not an integer")

        if first_name == None or not isinstance(first_name, str):
            raise Exception("string is not a string")

        if type(date_of_birth) == str or len(date_of_birth) != 3 or date_of_birth[0] not in range(1, 13) or date_of_birth[1] not in range(1, 32):
            raise Exception("date_of_birth is not a valid date")

        if not isinstance(genre, str) and genre not in self.GENRES:
            raise Exception("genre is not valid")

        if not isinstance(eyes_color, str) and eyes_color not in self.EYES_COLORS:
                raise Exception("eyes_color is not valid")

    # declaring all the private attributes
        self.__id = id
        self.__first_name = first_name
        self.__date_of_birth = date_of_birth
        self.__genre = genre
        self.__eyes_color = eyes_color

    # geta
    def get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_genre(self):
        return self.__genre

    def get_eyes_color(self):
        return self.__eyes_color

    # start of task 1 base class description
    def __str__(self):
        return self.__first_name + ' ' + self.last_name

    def is_male(self):
        if Person[3] != "Male":
            return False

    # age portion with comparitors
    # 05/20/2016
    def age(self):
        if self.__date_of_birth[0] > 5:
            return 2016 - self.__date_of_birth[2] - 1

    # comparitor overload
    def __gt__(self, other):
        return self.age() > other.age()

    def __ge__(self, other):
        return self >= other

    def __lt__(self, other):
        return self < other

    def __le__(self, other):
        return self <= other

    def __eq__(self, other):
        return self == other


# task 2 declaring methods to be overloaded by individual child classes.
    def can_run(self):
        return False

    def need_help(self):
        return False

    def is_young(self):
        return False

    def can_vote(self):
        return False


# can_run(self) => return True if the Class is Teenager or Adult
# need_help(self) => return True if the Class is Baby or Senior
# is_young(self) => return True if the Class is Baby or Teenager
# can_vote(self) => return True if the Class is Adult or Senior

# task 2 new classes to inherit Person class
class Baby(Person):
    def need_help(self):
        return True

    def is_young(self):
        return True

class Teenager(Person):
    def can_run(self):
        return True

    def is_young(self):
        return True

class Adult(Person):
    def can_run(self):
        return True

    def can_vote(self):
        return True

class Senior(Person):
    def need_help(self):
        return True

    def can_vote(self):
        return True

# task 3
# declaring a dictionary
def json(self):
    if not isinstance(json, dict):
        raise Exception("json is not valid")
    family_dict = {'id': self.__id,
    'first_name': self.__first_name,
    'date_of_birth': self.__date_of_birth,
    'genre': self.__genre,
    'eyes_color': self.__eyes_color}
    return family_dict

def load_from_json(self, json):
    self.__id = json['id']
    self.__first_name = json['first_name']
    self.__date_of_birth = json['date_of_birth']
    self.__genre = json['genre']
    self.__eyes_color = json['eyes_color']

def save_to_file(list, filename):
    if not isinstance(filename, str) or not os.path.isfile(filename):
        raise Exception("filename is not valid or doesn't exist")
    else:
        with open(filename, 'w') as outfile:
            json.dump(list, outfile)

def load_from_file(filename):
    if not isinstance(filename, str) or not os.path.isfile(filename):
        raise Exception("filename is not valid or doesn't exist")
    else:
        with open(filename) as json_data:
            data = json.load(json_data)
            return data
