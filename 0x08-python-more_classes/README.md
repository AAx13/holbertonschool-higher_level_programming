# More Classes and Objects Project ([@Holbertonschool](https://www.holbertonschool.com/))

## Project Requirements
* Allowed editors: `vi`, `vim`, `emacs`.
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3).
* All your files should end with a new line.
* The first line of all your files should be exactly `#!/usr/bin/python3`.
* A `README.md` file, at the root of the folder of the project, is mandatory.
* Your code should use the `PEP 8` style.
* All your files must be executable.
* The length of your files will be tested using `wc`.
* All your modules should have a documentation `(python3 -c               'print(__import__("my_module").__doc__)')`
* All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
* All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
* You are not allowed to import any module

## Modules
An empty class `Rectangle` that defines a rectangle.
* You are not allowed to import any module

[0-rectangle.py](../0x08-python-more_classes/0-rectangle.py)

***
A class `Rectangle` that defines a rectangle by: (based on `0-rectangle.py`)

* Private instance attribute: `width:`
* Property `def width(self):` to retrieve it
* Property setter `def width(self, value):` to set it:

        Width must be an integer, otherwise raise a TypeError exception with the message width must be an integer.

        If width is less than 0, raise a ValueError exception with the message width must be >= 0.

* Private instance attribute: `height`:
* Property `def height(self):` to retrieve it
* Property setter `def height(self, value):` to set it:

        Height must be an integer, otherwise raise a TypeError exception with the message height must be an integer

        If height is less than 0, raise a ValueError exception with the message height must be >= 0

* Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`

[1-rectangle.py](../0x08-python-more_classes/1-rectangle.py)

***
A class `Rectangle` that defines a rectangle by: (based on `1-rectangle.py`)

* Public instance method: `def area(self):` that returns the rectangle area.
* Public instance method: `def perimeter(self):` that returns the rectangle perimeter:

        if width or height is equal to 0, perimeter is equal to 0.

[2-rectangle.py](../0x08-python-more_classes/2-rectangle.py)

***
A class `Rectangle` that defines a rectangle by: (based on `2-rectangle.py`)

* `print()` and `str()` should print the rectangle with the character `#`:

        If width or height is equal to 0, return an empty string.

[3-rectangle.py](../0x08-python-more_classes/3-rectangle.py)

***
A class `Rectangle` that defines a rectangle by: (based on `3-rectangle.py`)

* `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`.

[4-rectangle.py](../0x08-python-more_classes/4-rectangle.py)
