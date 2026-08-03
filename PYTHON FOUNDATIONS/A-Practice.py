# 20 Coding Challenges on Core language foundation

# 1. Slice Trickery: Given s = "TheQuickBrownFox", write a single slice operation that extracts "noB".
s = "TheQuickBrownFox"
print(s[12:7:-2])

# 2. Boolean Math: What is the integer result of (True + True) ** (False == 0)?
print((True + True) ** (False == 0))    # (1+1)^1 = 2

# 3. Float Precision Fix: Write an expression without using modules to check if 0.1 + 0.2 is equal to 0.3 
# by rounding both sides to one decimal place.
print(round(0.1 + 0.2, 1))
print(round(0.3, 1))
print(round(0.1 + 0.2, 1) == round(0.3, 1))

import math
print(math.isclose((0.1+0.2), 0.3))

# 4. Memory Address: Create a variable x = 256 and y = 256. 
# Write a boolean expression checking if they are the exact same object in memory. 
# Repeat for 257.
x = 256
y = 256
z = 257
print(x is y)
print(x is z)

# 5. Short-Circuit Assignment: Write an expression using or that assigns the variable username to "Guest" 
# if the variable input_name is an empty string.
input_name = ""
username = input_name or "Guest"
print(username)


# 6. String Reversal Step: Given word = "racecar", write a boolean expression to check 
# if it is a palindrome using only slicing and ==.
word = "racecar"
if word == word[len(word)::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 7. Unicode Extraction: Write an expression that gets the Unicode integer code 
# point of the last character of the string "Python".
str = "Python"
print(str[-1])      # returns last character
print(ord(str[-1])) # 110

# 8. Byte Conversion: Convert the string "Café" to UTF-8 bytes, then 
# immediately count the number of bytes using len(). (Note: It won't be 4!).
str = "Café"
encoded_str = str.encode('utf-8')
print(len(encoded_str))     # Result: 5. The 'é' character takes 2 bytes in UTF-8 encoding.

# 9. Truthy Check: What does bool("False") == bool("0") evaluate to, and why?
print(bool("False") == bool(0))     # False
print(bool("False") == bool("0"))   # True; Both are non-empty strings, which always evaluate to True in Python. True == True

# 10. Type Hierarchy: Check if type(False) is a subclass of int using issubclass(bool, int). 
# What is the result?
print(type(False).__name__)
print(type(type(False).__name__))   # String obj so doesnt compare and throws error
# print((type(False)).issubclass(int)) -> this is wrong (x.issubclass) is only applicable for sets

# print(issubclass(child, parent))
print(issubclass(type(False), int))
print(issubclass(type(False), int))

# 11. Negative Slicing: Given s = "0123456789", what does s[-2:-8:-2] return?
s = "0123456789"
print(s[-2:-8:-2])      # 864

# 12. Object Identity Mutation: 
# Predict the output: s = "a"; id_1 = id(s); s = s + "b"; id_2 = id(s); print(id_1 == id_2).
s = "a"
id_1 = id(s)
s = s + "b"
id_2 = id(s)
print(id_1 == id_2) # FALSE; STRINGS ARE IMMUTABLE


# 13. Binary to Int: Use a built-in Python function to convert the binary string 
# "1101" into a base-10 integer.
print(int("1101",2))        # 13

# Hexadecimal (Base 16) to Int
# Valid characters are 0-9 and A-F
print(int("1A", 16))        # Output: 26

# Octal (Base 8) to Int
# Valid characters are 0-7
print(int("17", 8))         # Output: 15

# It even works if the string has standard Python prefixes (0x, 0b, 0o)
print(int("0x1A", 16)) # Output: 26

# BASE 10 TO OTHER BASES (STRING)
number = 26

# Integer to Binary String
# Adds the '0b' prefix
print(bin(number))  
# Output: '0b11010'

# Integer to Hexadecimal String
# Adds the '0x' prefix
print(hex(number))  
# Output: '0x1a'

# Integer to Octal String
# Adds the '0o' prefix
print(oct(number))  
# Output: '0o32'


# 14. Complex Truthy: Evaluate the expression: "" or 0 or [] or "Python" or None. 
# What string does it return?
"" or 0 or [] or "Python" or Non    # Result: "Python". The 'or' operator scans left to right and returns the first truthy object it finds.

# 15. Advanced Slicing: Extract the first half of a string s of unknown even length using len(s) inside the slice.
s = "asdadasdasdasdas"
spliced = s[0:int(len(s)/2)]
print(spliced)
# OR
s[:len(s)//2]   # FLOOR DIVISION - Extract int PART

# 16. Modulo & Floor Division: Extract the tens digit of the number 1492 using only % and // arithmetic.
number = 1492
# tens digit
print ((1492 // 10) % 10)
# hundreds digit
print ((1492 // 100) % 10)

# all digits extracted
while number>0:
    print(number%10)
    number = number // 10


# 17. String Immutability Proof: Write code that attempts to change the first letter of "hello" to "H". 
# Observe the specific TypeError Python throws.
s = "hello"
s[0] = "H"      # Raises: TypeError: 'str' object does not support item assignment

# 18. Chained Comparisons: Write a single expression that checks if a variable n is greater than 10, 
# less than 20, and not equal to 15, using Python's chained comparison syntax (e.g., a < b < c).
n  = 15
print(10 < n < 20 and n != 15)      # Python supports chaining mathematical operators natively (10 < n < 20).)

# 19. None Identity: Write an expression to check if a variable val is exactly 
# None using the recommended identity operator, rather than equality.
var = None
print(var is None)

# 20. XOR Cipher Prep: Given a character char = 'A', 
# write a one-liner that converts it to its integer code, adds 3 to it, and converts it back to a character.
char = 'A'
char_encoded = chr(ord(char) + 3)
print(char_encoded)     # D