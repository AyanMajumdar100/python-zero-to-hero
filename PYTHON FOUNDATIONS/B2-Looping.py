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