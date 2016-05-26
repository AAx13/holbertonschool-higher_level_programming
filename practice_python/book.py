
class Book:
    title = ''
    pages = 0

    def __init__(self, title='', pages=0):
        self.title = title
        self.pages = pages

    def __str__(self):
        return self.title

    def __radd__(self, other):
        return self.pages + other
