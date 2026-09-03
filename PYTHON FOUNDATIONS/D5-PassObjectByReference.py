# Python passes object references by value.
def greet(name):
    print(name)
person = "Ayan"

greet(person)

# "name" does not receive a copy of the string object.
# Instead, Python passes the reference to the object into the function.
# So both variables can refer to the same object

def change_number(x):
    print("Inside function:", x)
    x = 100
    print("After reassignment:", x)

number = 10
print("Before function:", number)
change_number(number)
print("After function:", number)

# Python gives the function's parameter x a reference to the same object:
# does not modify the integer 10.
# Instead, it makes x refer to another object
# Reassignment changes what a local name points to.

# NOW FOR LISTS :
def add_item(items):
    items.append("Python")      # items.append("Python") mutates the existing list

languages = ["Java", "C++"] # Before: ['Java', 'C++']
print("Before:", languages)
add_item(languages)
print("After:", languages)  # After: ['Java', 'C++', 'Python']

# MUTATION VS REASSIGNMENT
def reassign(items):
    items = ["Python"]

def mutate(items):
    items.append("Python")

languages = ["Java", "C++"]
reassign(languages)
print(languages)    # ['Java', 'C++'] -> Original List not touched
mutate(languages)
print(languages)    # ['Java', 'C++', 'Python'] -> Mutated

# languages ──► ["Java", "C++"]
# items ──────► ["Java", "C++"]
# items = ["Python"]
# languages ──► ["Java", "C++"]
# items ──────► ["Python"]

def change_name(name):
    name += " Majumdar"

name = "Ayan"
change_name(name)
print(name)

# Reassignment (items = ...): This breaks the local variable's link to the original object 
# and points it to a brand-new object. 
# The original object outside the function remains completely untouched.

# Mutation (items.append(...) or items[key] = value): This modifies the actual object that the reference points to. 
# Since the inside and outside variables point to the same object, the changes are visible everywhere.
def reassign_dict(data):
    # This creates a brand new dictionary. 
    # The original 'languages' dict is untouched.
    data = {"new_key": "Python"} 

def mutate_dict(data):
    # This modifies the existing dictionary in place.
    data["new_key"] = "Python"

# Test Reassignment
languages = {"primary": "Java", "secondary": "C++"}
reassign_dict(languages)
print(languages)  
# Output: {'primary': 'Java', 'secondary': 'C++'} -> Unchanged

# Test Mutation
mutate_dict(languages)
print(languages)  
# Output: {'primary': 'Java', 'secondary': 'C++', 'new_key': 'Python'} -> Updated!

# "is" helps us understand this
# Python provides the is operator to check whether two names refer to the same object.
def check(data):
    print(data is numbers)  # True
    data = [100]
    print(data is numbers)  # False

numbers = [10, 20, 30]
check(numbers)

# Tricky Example:
def modify(numbers):
    numbers.append(100)
    numbers = [1, 2, 3]  # the local numbers point to a new list.

values = [10, 20, 30]
modify(values)
print(values)   # [10, 20, 30, 100]