# LOOPS & OPTIMIZATIONS

# Loop Mechanics (Iteration vs. Indexing)
# Rule of Thumb: Never use range(len(sequence)) 
# unless you absolutely must mutate the sequence via indices.

text = "AYAN MAJUMDAR"
# Un-Pythonic (Indexing):
for i in range(len(text)): print(text[i])

# Pythonic (Iteration):
for char in text: print(char)

# 1. enumerate() - when you need indices as well
for index, char in enumerate(text):
    print(f"Index {index} has {char}")

# 2. zip() - To loop through 2 iterables at the same time 
# (Assuming we had two strings of equal length)
for char1, char2 in zip("ABC", "XYZ"):    print(char1, char2)
# A X
# B Y
# C Z

# The while Loop : Used when you don't know how many times you need to loop beforehand 
# (e.g., waiting for a network response or validating user input).


# SECRET : Python loops have an optional else block.
for num in range(5):
    if num == 10:        break
else:    print("Loop finished without hitting a break!") # This WILL print


# 1. Comprehensions (The "One-Liner" Loops) : They run at C-speed under the hood
# List Comprehension:
numbers = [1, 2, 3, 4, 5]
squares = []
# BAD
for num in numbers:
    if num % 2 == 0:        squares.append(num ** 2)
# GOOD COMPREHENSION
squares = [num ** 2 for num in numbers if num % 2 == 0]

# Dictionary and Set Comprehensions:
square_dict = {num: num ** 2 for num in range(1, 4)}
print(square_dict)      # {1: 1, 2: 4, 3: 9}

unique_lengths = {len(word) for word in ["apple", "bat", "apple", "car"]}
print(unique_lengths)   # {3, 5}

# 2. Looping Through Dictionaries
user = {"name": "Ayan", "role": "Admin"}
# KEYS(DEFAULT)
for key in user:    print(f"{key}: {user[key]}")
# ITEMS
for key, value in user.items():    print(f"{key}: {value}")
# VALUES
for value in user.values():    print(value)

# 3. Loop Modifiers: reversed() and sorted()
names = ["Ayan", "Rayn", "Bob"]
for name in sorted(names):    print(name)
# better than slicing names[::-1] for huge lists
for name in reversed(names):    print(name)

# 5. The pass Placeholder
data = [1,2,3,4,5,6,7]
for item in data:
    # TODO: Implement parsing logic later
    pass

# 6. Itertools (The Advanced Looping Toolkit)
import itertools

colors = ["red", "blue"]
sizes = ["S", "M", "L"]
# 1. itertools.product(iterable,iterable): Instead of writing a nested loop, itertools.product creates every combination
for color, size in itertools.product(colors, sizes):
    print(color, size)  # Outputs: red S, red M, red L, blue S, blue M, blue L

# 2. COMBINATORICS (Combinations & Permutations)
import itertools
players = ["Alice", "Bob", "Charlie"]
# A. combinations(iterable, r): Returns all possible groupings of length r where order does not matter
for match in itertools.combinations(players, 2):
    print(match)
# B. permutations(iterable, r): Returns all groupings where order DOES matter
for result in itertools.permutations(players, 2):
    print(result)

# 2. INFINITE ITERATORS
import itertools
# A. cycle(iterable): Repeats a sequence endlessly. Perfect for turn-based games or alternating UI colors.
turns = itertools.cycle(["Player 1", "Player 2"])
print(next(turns)) # Output: Player 1
print(next(turns)) # Output: Player 2
print(next(turns)) # Output: Player 1

# B. count(start, step): Like range(), but it never stops.
data = ["Apple", "Banana", "Cherry"]
# zip() stops automatically when the shortest list (data) runs out!
for id_num, fruit in zip(itertools.count(100, 10), data):
    print(f"ID: {id_num} -> {fruit}") # Output: ID: 100 -> Apple, ID: 110 -> Banana, ID: 120 -> Cherry

# 3. Data Wrangling (Chaining & Grouping)
import itertools
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# Output: bird: 1, cat: 1, dog: 3
# A. chain(*iterables): Glues multiple lists together to loop over them as one continuous list, but without copying them in memory.
for num in itertools.chain(list1, list2, list3):
    print(num, end=" ")         # Output: 1 2 3 4 5 6 7 8 9
print()
# B. groupby(iterable, key): Groups adjacent identical elements together.
animals = ["dog", "dog", "cat", "dog", "bird"]
animals.sort()
for animal_type, group in itertools.groupby(animals):
    count = len(list(group))
    print(f"{animal_type}: {count}")

# 4. itertools.batched(data, n) to instantly chunk a massive list into smaller lists of length n 
# (e.g., grabbing 100 API results at a time) without writing complex index-slicing math!


# 5.LOOP OPTIMIZATION
# Python loops are relatively slow because the PVM has to evaluate types and variables on every single pass.
# How to avoid unnecessary passes:
# Early break: If you are searching for an item, break the loop the millisecond you find it.
# continue: Skip the rest of the current loop iteration if a condition is met, saving unnecessary computation below it.
# Hoist dot-lookups: Looking up methods (like string.upper) inside a loop takes time. If it doesn't change, do it outside the loop.

# Slower: Python has to look up what .upper() is on every pass
for char in text:    
    new_text += char.upper()

# Faster: (Though using string methods directly is best, this illustrates the point)
upper_func = str.upper
for char in text:    
    new_text += upper_func(char)

# To develop a strong intuition for loop optimization in Python,
# we have to shift how you view the Python Virtual Machine (PVM). 
# Python is notoriously slow at running for loops because it has to 
# 1. check variable types and 2. memory allocations on every single pass.

# Golden rule of Python optimization: 
# Push the looping down to the C level whenever possible, 
# and never evaluate something twice if you can evaluate it once.

# 1. The O(1) Lookup Swap 
# Using the in keyword on a list forces Python to scan the list item by item (NESTED LOOP)
# Convert the target list to a set before the loop. Set lookups happen instantly (O(1) time) via a hash table.
# The Scenario: Find all users in 'new_users' that already exist in 'banned_users'
new_users = ["Alice", "Bob", "Charlie", "David"] * 1000  # 4000 users
banned_users = ["Bob", "Eve", "Frank"] * 1000            # 3000 users
found_bans = []
# BAD = 4,000 * 3,000 = 12,000,000 operations!
for user in new_users:
    if user in banned_users:  # BECOMES A LOOP (Loops through every element in list)
        found_bans.append(user)

# GOOD = 4,000 + 3,000 = 7,000 operations. (1,700x faster)
banned_set = set(banned_users)
found_bans = [user for user in new_users if user in banned_set]

# 2. Lazy Evaluation (Avoiding Full Memory Passes)
# List comprehensions are incredibly fast, but they have a fatal flaw: 
# they evaluate the entire collection into memory before doing anything else. 
# If you are searching for a condition, you want to stop the millisecond you find it.

# Use generator expressions combined with Python's built-in any() or all() functions.
def expensive_check(num):    return num == 5
massive_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 10000
# BAD (Greedy Evaluation)
if True in [expensive_check(n) for n in massive_data]:    
    print("Found it!")
# GOOD (Lazy Short-Circuiting)
if any(expensive_check(n) for n in massive_data):    
    print("Found it!")

# 3. Branch Hoisting (Extracting Invariants)
# An "invariant" is a condition that does not change during the loop. 
# If you have an if statement inside a loop that checks a static configuration, 
# you are wasting CPU cycles evaluating the exact same question thousands of times.

# Hoist (lift) the static if statement outside the loop, and duplicate the loop inside the branches.
is_metric = True
measurements = [10, 20, 30, 40, 50] * 1000
results = []
# BAD
for m in measurements:
    if is_metric:        
        results.append(m * 2.54)
    else:        
        results.append(m)

# GOOD
if is_metric:    
    results = [m * 2.54 for m in measurements]
else:    
    results = measurements.copy()

# 4. Function Call Overhead (Variable Caching)
# Python has a surprisingly high overhead for calling functions and looking up object methods 
# (like string.lower or list.append) because it has to resolve the scope dictionary on every pass.

# If you are calling the same method in a tight, massive loop, assign that method to a local variable just outside the loop. 
# Local variable lookups in Python are much faster than attribute lookups (the . operator).
import math
data = range(1000000)
results = []
# BAD: On every pass, Python looks at the 'math' module, searches for 'sqrt', and then executes it. (1,000,000 lookups)
for num in data:    
    results.append(math.sqrt(num))
# GOOD: We look up math.sqrt ONCE, and results.append ONCE.
fast_sqrt = math.sqrt
fast_append = results.append
for num in data:    
    fast_append(fast_sqrt(num))

# NOTE: A list comprehension `[math.sqrt(x) for x in data]` 
# handles this specific C-level optimization for you automatically! 
# But caching is vital for complex while-loops or custom object methods.