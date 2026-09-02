# C. Returning Functions — The "Function Factory"
# A function can return another function.
# This becomes especially powerful when the returned function remembers values from the outer function. That's a closure.

# Example 1
def outer():
    def inner():
        print("Hello from inner")
    return inner
func = outer()      # outer() runs and returns the inner function.
func()              # func is essentially inner; so func() calls inner()

# Important distinction: 
# "return inner" -> means return the function itself.
# "return inner()" -> means Execute inner() and return its result.

# Example 2
def make_multiplier(n):
    def multiplier(number):
        return number * n
    return multiplier

doubler = make_multiplier(2)    # n=2 isnt forgotten; This is called a closure.
tripler = make_multiplier(3)
ten_times = make_multiplier(10)

print(doubler(5))
print(tripler(5))
print(ten_times(5))

# What is a Closure?
# A closure occurs when an inner function:
# 1. is defined inside another function,
# 2. uses a variable from the outer function,
# 3. is returned/exposed outside the outer function.

# How to inspect the Closure?
print(doubler.__closure__)                      # (<cell at 0x...: int object at 0x...>,)
print(doubler.__closure__[0].cell_contents)     # 2
# That's the closure memory.

# Example 3
def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

hello = make_greeter("Hello")
good_morning = make_greeter("Good Morning")
welcome = make_greeter("Welcome")

print(hello("Ayan"))        # Hello, Ayan!
print(good_morning("Ayan")) # Good Morning, Ayan!
print(welcome("Ayan"))      # Welcome, Ayan!


# Example 4
def make_power(exponent):
    def power(number):
        return number ** exponent
    return power

square = make_power(2)
cube = make_power(3)
fourth_power = make_power(4)

print(square(5))
print(cube(5))
print(fourth_power(2))

# Example 5
def make_discount(discount):
    def calculate(price):
        return price - (price * discount / 100)
    return calculate

ten_percent = make_discount(10)
twenty_percent = make_discount(20)
fifty_percent = make_discount(50)

print(ten_percent(1000))
print(twenty_percent(1000))
print(fifty_percent(1000))

# Example 6
def make_checker(required_role):
    def check(user_role):
        return user_role == required_role
    return check

admin_checker = make_checker("admin")
user_checker = make_checker("user")

print(admin_checker("admin"))
print(user_checker("user"))
print(admin_checker("user"))

# Example 7
def make_prefix(prefix):
    def add_prefix(text):
        return f"{prefix}{text}"
    return add_prefix

error = make_prefix("[ERROR] ")
info = make_prefix("[INFO] ")
warning = make_prefix("[WARNING] ")

print(error("Database failed"))
print(info("Server started"))
print(warning("Low memory"))