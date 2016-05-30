
class TaskModel:

    ''' Constructor '''
    def __init__(self, title):

        if not isinstance(title, str):
            raise Exception("title is not a string")

        self.__title = title

    def get_title(self):
        return self.__title

    def set_callback_title(self, callback):
        self.__callback_title = callback

    ''' This will reverse the string '''
    def toggle(self):
        self.__title = self.__title[::-1]
        self.__callback_title(self.__title)

    ''' Overloading funciton to print a string '''
    def __str__(self):
        return self.__title
