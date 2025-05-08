# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

# solution:
class A:
    def show(self):
        print("A's show() method")


class B(A):
    def show(self):
        print("B'S SHOW() METHOD")


class C(A):
    def show(self):
        print("C's show() method")

class D(B, C):
    def show(self):
        return super().show()
    
# Create an object of D and call show() to observe MRO
d = D()
d.show()
print(D.mro())  # Method Resolution Order (MRO) of class D
# Output:
# B'S SHOW() METHOD
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
