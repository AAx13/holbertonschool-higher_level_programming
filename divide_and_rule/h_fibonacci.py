import threading

class FibonacciThread(threading.Thread):

    def __init__(self, number):

        self.__number = number

        if not type(self.__number, int):
            raise Exception("number is not an integer")

    def run(self):
        
