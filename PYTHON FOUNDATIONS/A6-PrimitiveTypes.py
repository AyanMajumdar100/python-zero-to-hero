# 1. INT
# (ARBITRARY PRECISION) - Python 3 integers have arbitrary precision. 
# They can grow as large as your RAM allows. 
# There is no integer overflow (unlike Java or C++).
massive_number = 2 ** 1000
# type(variable) - This method is used to get the type of a variable
print(type(massive_number))     # <class 'int'>
print(massive_number)           # OUTPUT : 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376

# 2. FLOAT
# Implemented using C's double (IEEE 754 standard).
# Because of binary fraction representation, 0.1 + 0.2 equals 0.30000000000000004, not 0.3.
result = 0.1 + 0.2

print(f"0.1 + 0.2 = {result}")
print(f"Does 0.1 + 0.2 == 0.3? {result == 0.3}") # Returns False

# Fix it using math.isclose()
import math
print(f"Are they close enough? {math.isclose(result, 0.3)}") # Returns True

# 3. BOOL
# bool: True and False are actually subclasses of int. 
# True is structurally exactly 1, and False is 0. 
# We can literally do arithmetic with them: True + True == 2
print(f"True is 1  : {True == 1}")          # True is 1  : True
print(f"False is 0 : {False == 0}")         # False is 0 : True

# DOING MATH WITH BOOL
print(f"True + True = {True + True}")        # 1 + 1 = 2
print(f"False + 5 = {False + 5}")            # 0 + 5 = 5
print(f"True * 50 = {True * 50}")            # 1 * 50 = 50

# 4. NONE (The Singleton)
# The None object represents the absence of a value. 
# It is a singleton (only one None exists in memory).
# Always compare things to None using the is keyword instead of ==
var1 = None
var2 = None
print(f"var1 is var2 : {var1 is var2}") 

if var1 is None:
    print("var1 has no value!")