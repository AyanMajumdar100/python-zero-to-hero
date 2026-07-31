# RECALL LISTS (ORDERED, MUTABLE COLLECTIONS) fruits = ["Apple", "Banana", "Cherry"] -> append, insert, extend, reverse, sort, remove, pop

# DICTIONARY
# KEY - VALUE Pair with keys being unique and immutable

# EMPTY DICTIONARY
dict_1 = {}
dict_2 = dict()

# USING KEYWORD ARGUEMENTS
dict_3 = dict(name = "Aryan", age = 25, nickname = "Pepe")

# USING ITERABLE TUPLES
dict_4 = dict([("name","Ayan"),("Job", "Engineer")])

# SETTING DEFAULT VALUES TO KEYS
keys = ['a', 'b', 'c', 'd']
dict_5 = dict.fromkeys(keys,0)

print(dict_1)       # {}
print(dict_2)       # {}
print(dict_3)       # {'name': 'Aryan', 'age': 25, 'nickname': 'Pepe'}
print(dict_4)       # {'name': 'Ayan', 'Job': 'Engineer'}
print(dict_5)       # {'a': 0, 'b': 0, 'c': 0, 'd': 0}


# LITERAL WITH DATA
user = {
    "name" : "Ayan",
    "age" : 28,
    "role" : "Admin"
}
print(f"USER DICTIONARY : {user}")
# OUTPUT : USER DICTIONARY : {'name': 'Ayan', 'age': 28, 'role': 'Admin'}

# DIRECT ASSIGNMENT
user["country"] = "India"
# OUTPUT : USER DICTIONARY : {'name': 'Ayan', 'age': 25, 'role': 'Admin', 'country': 'India'}

# Dictionary Methods
# 1. dict1.get(key, default) - Safely fetches a value, returns none(default) if no matching key found
print(f"Name : {user.get("name")}")         # Name : Ayan
print(f"Gender : {user.get("gender")}")     # Gender : None
print(f"Gender : {user.get("gender", "Not Specified")}")    # Gender : Not Specified

# 2. dict1.keys(), dict1.values(), dict1.items()
# Keys in the dictionary : dict_keys(['name', 'age', 'role'])
print(f"Keys in the dictionary : {user.keys()}")

# Values in the dictionary : dict_values(['Ayan', 28, 'Admin'])
print(f"Values in the dictionary : {user.values()}")

# Items in the dictionary : dict_items([('name', 'Ayan'), ('age', 28), ('role', 'Admin')])
print(f"Items in the dictionary : {user.items()}")

# 3. dict1.update(dict1) - Merges another dict to this dict OR updates the existing keys
user.update({"age" : 25, "gender" : "Male"})
print(user)
# OUTPUT : {'name': 'Ayan', 'age': 25, 'role': 'Admin', 'gender': 'Male'}

# 4. dict1.pop(key) - removes key-value pair and returns the value
# TypeError - pop expected at least 1 argument
removed_value = user.pop("gender")
print(f"Removed = {removed_value} | Updated Dict = {user}")
# OUTPUT : Removed = Male | Updated Dict = {'name': 'Ayan', 'age': 25, 'role': 'Admin'}

# 4.1 - dict_name.popitem() pops the last key-value pair(LIFO) and returns it as a tuple
# popitem() on an empty dictionary = raises a KeyError exception.
k,v = user.popitem()
print(k,v)      # OUTPUT - country India


# 5. dict1.setdefault() - Inserts key with default value only if the key doesnt exist
user.setdefault("country", "USA")       # it wont update if a key value is already present
print(user)
# OUTPUT : {'name': 'Ayan', 'age': 25, 'role': 'Admin', 'country': 'USA'}

# Check if key exists
has_key = "name" in user
print(has_key)      # OUTPUT : True


# WAYS TO ADD : Direct Assignment - dict1[key] = value,dic1.setdefault(key,value), dict1.update(dict2)
d = {"name": "Ayan"}
d["age"] = 25 
d.setdefault("country", "USA")  # doesnt update if country key-value already present
d.update({"age": 26, "city": "NY"})


# WAYS TO REMOVE : dic1.pop(key,default), dic1.popitem(), del dict1[key], dict1.clear(), del d1
dict1 = dict(a=1,b=2,c=3,d=4,e=5)
print(dict1)        # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

popped_value = dict1.pop('a')
print(f"Popped value = {popped_value}")     # Popped value = 1
popped_value = dict1.pop('a',"Key Not Found")
print(f"Popped value = {popped_value}")     # Popped value = Key Not Found

k,v = dict1.popitem()
print(f"Popped Tuple : {k,v} | dict 1 = {dict1}")
# OUPUT : Popped Tuple : ('e', 5) | dict 1 = {'b': 2, 'c': 3, 'd': 4}

del dict1["b"]
print(dict1)        # {'c': 3, 'd': 4}

del dict1           # DELETES ENTIRE DICTIONARY
dict1.clear()       # CLEARS ENTIRE DICTIONARY FROM MEMORY


# ITERATION THROUGH DICTIONARIES (keys, values, items, next&None for lookups)
dict2 = dict(a=1,b=2,c=3,d=4,e=5)
print(dict2)
# KEYS
for key in dict2:
    print(key)
for key in dict2.keys():
    print(key)
# VALUES
for value in dict2.values():
    print(value)
# ITEMS
for k,v in dict2.items():
    print(k,v)

# NOW IF WE WANT TO FIND KEY FROM VALUES
# APPROACH 1 (VANILLA)
target = 5
# target = input("ENTER VALUE TO SEARCH : ")
# next(iterable,default)
# next() retrieves the very next item from the iterator, no seperate list is created, just producing value 1 by 1 on demand
# None - If next() runs out of items to check and finds nothing, it crashes and throws a STOPITERATIONERROR.
# So, it accepts a second optional arguement to act as a default fallback
key = next((k for k,v in dict2.items() if v == target),None)
print(f"Key for {target} is {key}")     # Key for 5 is e

# APPROACH 2 (External Libraries like bidict or inverse)
# from bidict import bidict
# d1 = bidict(a=1,b=2,c=3,d=4,e=5)
# print(d1["a"])
# print(d1.inverse[5])          # dict_name.inverse[value]

# from inverse import inverse
# d2 = dict(a=1,b=2,c=3,d=4,e=5)
# print(inverse(d2)[5])           # inverse(dict_name)[value]

# COPYING AND MERGING OF DICTIONARIES
dict_1 = dict(a=1,b=2)
dict_2 = dict(b=99,c=3)

# SHALLOW COPY
dict_copy = dict_1.copy()
print(f"Copied Dictionary : {dict_copy}")           # Copied Dictionary : {'a': 1, 'b': 2}
# dict_copy['a'] = 10
# print(f"DICT 1 : {dict_1} | Copied DICT 1 : {dict_copy}")

# MERGING USING UNPACKING OPERATOR (**)
merged_dict1 = {**dict_1, **dict_2}
print(f"Merged Dictionary 1 : {merged_dict1}")      # Merged Dictionary 1 : {'a': 1, 'b': 99, 'c': 3}

# MERGING USING UNION OPERATOR
merged_dict2 = dict_1 | dict_2
print(f"Merged Dictionary 2 : {merged_dict1}")      # Merged Dictionary 2 : {'a': 1, 'b': 99, 'c': 3}

# ADVANCED MANIPULATION
squares_dict = {x:x**2 for x in range(10)}      # Till <10
squares_dict1 = {x:x**2 for x in range(1,11)}   # From 1 to 10(included)
print(squares_dict)

inverted_squares = {v:k for k,v in squares_dict.items()}
print(inverted_squares)

# STRUCTURAL EVALUATION (Python only looks at the keys)
# Truthiness: In Python, the integer 0 is considered Falsy, 
# while any non-zero integer is considered Truthy
all_true = all(squares_dict)        # keys have 0 -> so Falsy
any_true = any(squares_dict)        # Any non 0 integer = Truthy
print(f"ALL TRUE : {all_true}, ANY TRUE : {any_true}")
# OUTPUT : ALL TRUE : False, ANY TRUE : True