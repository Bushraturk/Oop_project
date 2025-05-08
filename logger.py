# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

# solution:
class Logger:
    def __init__(self):
        print("Logger message: Object created!")

    def __del__(self):
        print("Logger message: object destructor called!")


log = Logger()  # This will call the constructor and print the message
del log  # This will call the destructor and print the message            