# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

# The Engine class should have a method called start that returns a string "Engine started".
# The Car class should have a method called drive that returns a string "Car is driving" and should also call the start method of the Engine class.

class Engine:
    def start(self):
        return "Engine started"
    
class Car:
        def __init__(self, engine):
            self.engine = engine
    
        def drive(self):
            engine_status = self.engine.start()
            return f"{engine_status} - Car is driving"
            
# Example usage:
engine = Engine()
car = Car(engine)
print(car.drive())  # Output: "Engine started - Car is driving"