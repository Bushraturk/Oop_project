# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

# solurtion
class Mathutils:
    @staticmethod
    def add(a, b):
        return a + b
    
result = Mathutils.add(5, 10 )
print("Sum of my 2 numbers are:",result)   
