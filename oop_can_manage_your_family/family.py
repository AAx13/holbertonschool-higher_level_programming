from datetime import date

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
        if Person[3] == "Male":
            return True

    # age portion with comparitors
    def age(self):
        birthday = date(self.__date_of_birth[2], self.__date_of_birth[0], self.__date_of_birth[1])
        today = date(2016, 05, 20)
        age = date(2000, 02, 02)
        if today.year > birthday.year:
            age[0] = today.year - birthday.year - 1
        if today.month < birthday.month and today.month + birthday.month <= 12:
            age[1] = today.month + birthday.month
        else:
            age[1] = birthday.month - today.month
        if today.day < birthday.day and today.day + birthday.day <= 31:
            age[2] = today.day + birthday.day
        else:
            age[2] = birthday.day - today.day

        if today > birthday:
            return today - birthday - 1
