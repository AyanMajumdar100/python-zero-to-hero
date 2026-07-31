# This file contains the details of all immutable datatypes in python
# Immutability - Once created their contents cannot be modified; if an immutable object is tried to be modified - 
# Python creates a new object in memory & moves our reference to it

# Immutable Datatypes : int, float, bool, str, tuple

# 1. String
message = "Ayan"
print(f"Memory Id of 'message' object({message}) before update = {id(message)}")
# OUTPUT = Memory Id of 'message' object(Ayan) before update = 2434712843344

# Trying to modify an immutable datatype
message = message + " Majumdar"
print(f"Memory Id of 'message' object({message}) after update = {id(message)}")
# OUTPUT = Memory Id of 'message' object(Ayan Majumdar) after update = 2434713019696

# TUPLES
# Because tuples are immutable, Python provides only 2 built-in methods for tuple objects: .count() and .index()

null_tuple = ()     # Empty tuple
single_elem_tuple = (12,)       # without the , it is considered "int"
mixed_tuple = (1, 3.14, "Python", True)
packing_tuple = 1, 3, 15, 19

# Accessing elements in a tuple
fruits = ("apple", "banana", "orange", "kiwi", "banana")
print(fruits[0])            # apple
print(fruits[1:3])          # ('banana', 'orange')
print(fruits[-1])           # banana

# Testing Immutability of a tuple
numbers = (1, 10, 20, 30, 50)
# numbers[0] = 10           TypeError: 'tuple' object does not support item assignment

# Unpacking of a tuple
data = (10, 20, 30)
x, y, z = data
print(f"X = {x}, Y = {y}, Z = {z}")         #X = 10, Y = 20, Z = 30

# Extended unpacking using * Operator
# Only one unpack operation allowed in list
a, *b, c = 1,2,3,4,5,7
print(f"A = {a}, B = {b}, C = {c}")      #A = 1, B = [2, 3, 4, 5], C = 7

# Due to immutability there are only 2 methods defined for tuples - .index() & .count()
numbers = (10, 20, 30, 40, 30, 50)  
print(numbers.count(30))            # 2
print(numbers.count(100))           # 0

# numbers.index(100) -> will throw ValueError 
print(numbers.index(30))            # 2
# Search index of 30 starting from index 3
print(numbers.index(30, 3))         # 4

# ValueError try except block
try:
    numbers.index(100)
except ValueError:
    print("Element not present in the tuple")

# Some common Python Built-in functions we can use with tuples
data = (5, 2, 8, 1, 9)
print(len(data))                    # 5 (length)
print(min(data))                    # 1 (minimum value)
print(max(data))                    # 9 (maximum value)
print(sum(data))                    # 25 (sum of elements)
print(sorted(data))                 # [1, 2, 5, 8, 9] (returns a new sorted LIST)