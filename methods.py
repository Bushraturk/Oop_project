# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self,name):
        print(f"{self.name} says woof!")

d1 = Dog("Buddy", "Golden Retriever") 
print(d1.name)
d1.bark("dogi")  # Output: Buddy says woof!

            