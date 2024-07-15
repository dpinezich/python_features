import enum

class Pythonista(str, enum.Enum):
    DAPI = "David"

def greet(name):
    match name:
        case Pythonista.DAPI:
            print("Hi, David!")
        case _:
            print("Howdy, stranger!")

greet("David")
greet("Roger")