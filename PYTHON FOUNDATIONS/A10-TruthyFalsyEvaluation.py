# In Python, boolean operators (and, or) and conditional statements (if, while) 
# don't actually require a literal True or False. They look at the "Truthiness" of an object.

# All of these will print, because the objects are Truthy
if "False":
    print("A string of the word 'False' is Truthy!")

if "0":
    print("A string containing zero is Truthy!")

if [-1]:
    print("A list with a negative number is Truthy!")

# bool()
print(bool("Hello"))  # True
print(bool(""))       # False
print(bool([" "]))    # True (List containing a space string)

# OTHER TYPES OF zeros ARE FALSY
print(bool(0.0))      # False (Float zero)
print(bool(0j))       # False (Complex number zero)

from decimal import Decimal
print(bool(Decimal(0))) # False (Decimal zero)

# Custom Objects are Truthy by Default
# If you create your own class in Python, any object you make from it 
# will automatically be Truthy, even if it contains no data.

# To make a custom object behave like built-in collections (where it becomes Falsy if it's "empty"), 
# you have to explicitly define a __bool__() or __len__() method inside your class. 
# Python checks __bool__() first, and if it's missing, it checks if __len__() returns 0.

class Box:
    def __init__(self, items):
        self.items = items
    # Python looks for this to determine Truthiness!
    def __len__(self):
        return len(self.items)

box1 = Box([])          # Because __len__ returns 0, the object is Falsy
if box1:
    print("The box has something in it.")
else:
    print("The box is completely empty!")       # Output: The box is completely empty!


# NOW LETS SEE WHAT HAPPENS WITHOUT THE __len__(self) method
class Box:
    def __init__(self, items):
        self.items = items
box1 = Box([])
# 
if box1:
    print("The box has something in it.")   # WILL RETURN THIS (TRUTHY)
else:
    print("The box is completely empty!") 