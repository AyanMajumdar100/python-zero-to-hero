# STRING MANIPULATION

# A> STRING CASE CHANGERS
text = "hello WORLD! python is Fun."

# 1. upper() - Converts all characters to uppercase
print(text.upper())         # Output: 'HELLO WORLD! PYTHON IS FUN.'

# 2. lower() - Converts all characters to lowercase
print(text.lower())         # Output: 'hello world! python is fun.'

# 3. capitalize() - Capitalizes only the very first letter of the string
print(text.capitalize())    # Output: 'Hello world! python is fun.'

# 4. title() - Capitalizes the first letter of every word
print(text.title())         # Output: 'Hello World! Python Is Fun.'

# 5. swapcase() - Swaps lowercase to uppercase and vice versa
print(text.swapcase())      # Output: 'HELLO world! PYTHON IS fUN.'


# B> CLEANUP METHODS OF STRING
messy_text = "   python coding   "
csv_data = "apple,banana,cherry"

# 1. strip() - Removes whitespace (or specific characters) from both ends
# lstrip() for left-side only
# rstrip() for right-side only
print(f"'{messy_text.strip()}'")                            # Output: 'python coding'

# 2. replace(old, new, count) - Replaces parts of the string
print(messy_text.replace("python", "java").strip())         # Output: 'java coding'

# 3. split(separator) - Breaks a string into a LIST of strings based on a separator
fruits_list = csv_data.split(",")
print(fruits_list)                                          # Output: ['apple', 'banana', 'cherry']

# 4. join(iterable) - The exact opposite of split. Joins a list into a single string.
joined_text = " --- ".join(fruits_list)
print(joined_text)                                          # Output: 'apple --- banana --- cherry'

# 5. zfill(width) - Pads the string with zeros on the left (great for formatting numbers)
number_str = "42"
print(number_str.zfill(5))                                  # Output: '00042'


# When you provide absolutely no arguments in "split()", 
# Python looks for any combination of spaces, tabs (\t), or newlines (\n). 
# More importantly, it treats consecutive whitespace as a single separator, 
# and it automatically ignores whitespace at the very beginning or end of the string.
text = "  apples   bananas \t cherries \n dates     "
cleaned_text = ", ".join(text.split())
print(cleaned_text)         # Output: apples, bananas, cherries, dates



# C> SEARCHING AND FINDING IN A STRING
sentence = "The quick brown fox jumps over the lazy dog."

# 1. find(substring) - Returns the lowest index where the substring starts. 
# Returns -1 if it is not found.
print(sentence.find("fox"))         # Output: 16
print(sentence.find("cat"))         # Output: -1

# 2. index(substring) - Exactly like find(), but CRASHES (ValueError) if not found.
print(sentence.index("brown"))      # Output: 10

# 3. count(substring) - Counts how many times[case-sensitive] a substring appears
print(sentence.count("the"))        # Output: 1

# 4. startswith(substring) - Returns True/False
print(sentence.startswith("The")) # Output: True

# 5. endswith(substring) - Returns True/False
print(sentence.endswith("cat."))  # Output: False


# MORE ON INDEXING/FINDING
# CASE 1 : LAST INDEX
sentence = "A dog is a dog, and that dog is happy."
# 1. rfind(substring) - Searches from the right. Returns -1 if not found.
last_dog = sentence.rfind("dog")
print(f"Last 'dog' is at index : {last_dog}")       # Output: 25

# 2. rindex(substring) - Same as rfind, but crashes (ValueError) if not found.
last_is = sentence.rindex("is")
print(f"Last 'is' is at index  : {last_is}")        # Output: 29

# CASE 2 : MIDDLE/SECOND INDEX
sentence = "A dog is a dog, and that dog is happy."
# Find the first occurrence
first_dog = sentence.find("dog")
print(f"First 'dog' : {first_dog}")                 # Output: 2
# We tell find() to start searching at index 3 (first_dog + 1)
second_dog = sentence.find("dog", first_dog + 1)
print(f"Second 'dog': {second_dog}")                # Output: 11

# CASE 3 : ALL OCCURENCES
sentence = "apple banana apple cherry apple date apple"
target = "apple"
all_indices = []
current_index = sentence.find(target)
while current_index != -1:
    all_indices.append(current_index) 
    current_index = sentence.find(target, current_index + 1)
print(f"All indices: {all_indices}")                # Output: [0, 13, 26, 37]
# NOW WE CAN FIND nth INDEX ANYTIME
print(f"Second instance: {all_indices[1]}")


# D> VALIDATION AND CHECKING
# 1. isdigit() - True if ALL characters are numbers (0-9)
print("12345".isdigit())                # True
print("123.45".isdigit())               # False (the decimal point is not a digit)

# 2. isalpha() - True if ALL characters are letters (a-z, A-Z)
print("Python".isalpha())               # True
print("Python3".isalpha())              # False (contains a number)

# 3. isalnum() - True if ALL characters are alphanumeric (letters OR numbers)
print("Python3".isalnum())              # True
print("Python 3".isalnum())             # False (contains a space)

# 4. isspace() - True if the string is ONLY whitespace (spaces, tabs, newlines)
print("   \n \t ".isspace())            # True