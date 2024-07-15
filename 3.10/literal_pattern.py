def greet(name):
    match name:
        case "David":
            print("Hi David")
        case _:
            print("Hi Stranger")