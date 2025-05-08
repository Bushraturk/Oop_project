# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.


# solution
class Bank:
     bank_name = "ABC BANK"

     def __init__(self, account_holder):
            self.account_holder = account_holder
            
     @classmethod
     def change_bank_name(cls, name):
                 cls.bank_name = name


     def display_info(self):
                 print(f"Account Holder: {self.account_holder}, Bank Name: {Bank.bank_name}") 

acc1 = Bank("Ali")
acc2 = Bank("Burhan")   
acc1.display_info()  # Before changing bank name
acc2.display_info()  # Before changing bank name    

Bank.change_bank_name("XYZ BANK")  # Changing bank name
acc1.display_info()  # After changing bank name
acc2.display_info()  # After changing bank name

        