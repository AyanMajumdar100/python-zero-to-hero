# Identity VS Equality

# == : denotes equality and means that 2 objects have the same value
# is : Denotes identity  which checks if 2 variables are pointing to thesame object in the memory
# id() : THis function is used to check the memory addresses

list_a = [1,2,3]
list_b = [1,2,3]

print(f"Check for list equality : {list_a == list_b}")     # returns Check for list equality : True
print(f"Check for list identity : {list_a is list_b}")     # returns Check for list identity : False

# f is used for formatting inside the print function to use both text and variables together for display

# Now pointing a new variable to the same object
list_c = list_a
print(f"Check for list equality : {list_a == list_c}")     # returns Check for list equality : True
print(f"Check for list identity : {list_a is list_c}")     # returns Check for list identity : True

print(f"Memory address of List A : {id(list_a)}")
print(f"Memory address of List B : {id(list_b)}")
print(f"Memory address of List C : {id(list_c)}")
# OUTPUT
# Memory address of List A : 1757370758528 (Same as C)
# Memory address of List B : 1757370830464 (Different)
# Memory address of List C : 1757370758528 (Same as A)

# TRAP : INTERNING
# Python auto-caches small strings and integer values behind the scene to save memory
# So, if integers range from (-5, 256) they point to same preallocated objects

a = -5
b = -5
print(f"Check for identity : {a is b}")     # returns Check for identity : True

a = 256
b = 256
print(f"Check for identity : {a is b}")     # returns Check for identity : True

a = 300
b = 300
print(f"Check for identity : {a is b}")     # returns Check for identity : False
