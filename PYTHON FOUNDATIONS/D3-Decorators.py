# DECORATORS ARE USED WHEN WE WANT TO ADD FUNCTIONALITY WITHOUT MODIFYING THE ORIGINAL METHOD
# EXAMPLE 1
def logger(func):
    def wrapper(*args, **kwargs):
        print("Calling FUNCTION: ", func.__name__)
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@logger
def introduce(name, age):
    return f"{name} is {age}"


introduce("Ayan", age=22)
# OUTPUT
# Before : Calling FUNCTION:  introduce
# After
# 'Ayan is 22'

# WHY NOT Before ➔ Ayan is 22 ➔ After?
# The introduce function does not print anything. 
# It uses return.When result = func(*args, **kwargs) runs inside the wrapper, 
# it quietly captures the text "Ayan is 22" into a variable. 
# It does not display on the screen yet.Then, print("After") runs.
# Finally, the wrapper returns the captured text. Your interactive console sees this final return value 
# and displays it at the very end.

def logger(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print(result) # Explicitly print the result here
        print("After")
        return result
    return wrapper
@logger
def introduce(name, age):
    return f"{name} is {age}"

introduce("Ayan", age=22)

# EXAMPLE 2
def logger(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs) # -> add() returned 30 but the wrapper didnt return it; so the value got lost
        print("After")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b
result = add(10, 20)
print(result)  # OUTPUT: None

# FUNCTION META DATA PROBLEM
print(add.__name__) # OUTPUT: wrapper
print(add.__doc__)  # OUTPUT: None


# FUNCTOOLS.WRAP solves this issue
from functools import wraps
def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling function")
        result = func(*args, **kwargs)
        return result
    return wrapper

@logger
def add(a, b):
    """Add two numbers."""
    return a + b

print(add.__name__) # add
print(add.__doc__)  # Add two numbers.

# EXAMPLE 3 : Production-Quality Basic Decorator
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished")
        return result
    return wrapper
@logger
def add(a, b):
    """Add two numbers."""
    return a + b
print(add(10, 20))

# EXAMPLE 4 : Authentication
from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user != "admin":
            return "Access denied"
        return func(user, *args, **kwargs)
    return wrapper

@require_admin
def delete_database(user):
    return "Database deleted"

print(delete_database("admin"))
print(delete_database("Ayan"))


# EXAMPLE 5: 
from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function:", func.__name__)
        print("args:", args)
        print("kwargs:", kwargs)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result
    return wrapper

@logger
def introduce(name, age, city="Unknown"):
    return f"{name}, {age}, {city}"
print(introduce("Ayan", 22, city="Kolkata"))
# OUTPUT:
# Function: introduce
# args: ('Ayan', 22)
# kwargs: {'city': 'Kolkata'}
# Result: Ayan, 22, Kolkata