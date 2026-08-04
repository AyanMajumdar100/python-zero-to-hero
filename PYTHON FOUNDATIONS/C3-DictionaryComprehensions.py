# DICTIONARY COMPREHENSIONS
# 1. Swapping Keys and Values (Inverting a dict)
original = {"a": 1, "b": 2, "c": 3}
d1 = {v: k for k, v in original.items()}

# 2. Mapping a list of strings to their lengths
words = ["apple", "bat", "crocodile"]
d2 = {word: len(word) for word in words}

# 3. Filtering out None values from a dictionary
dirty_dict = {"name": "Alice", "age": None, "email": "a@a.com"}
d3 = {k: v for k, v in dirty_dict.items() if v is not None}

# 4. Combining two lists into a dictionary using zip()
keys, values = ["name", "age", "role"], ["Bob", 25, "Dev"]
d4 = {k: v for k, v in zip(keys, values)}

# 5. Applying a function (math) to all values
prices = {"apple": 1.0, "banana": 0.5}
d5 = {k: round(v * 1.05, 2) for k, v in prices.items()} # 5% tax

# 6. Grouping items into a dictionary by type (requires ternary or pre-sorting, here we create lists of evens/odds)
nums = [1, 2, 3, 4, 5, 6]
d6 = {"Evens": [x for x in nums if x % 2 == 0], "Odds": [x for x in nums if x % 2 != 0]}

# 7. Character frequency counter for a string
text = "hello world"
d7 = {char: text.count(char) for char in set(text)}

# 8. Conditional Key Transformation (uppercase keys if value > 50)
scores = {"bob": 40, "alice": 95}
d8 = {k.upper() if v > 50 else k: v for k, v in scores.items()}

# 9. Extracting a subset of a dictionary based on a list of keys
user = dict(name="Ayan",role = "Admin")
target_keys = {"name", "role"}
d9 = {k: user[k] for k in target_keys if k in user}

# 10. Creating a mapping of numbers to their binary string representation
d10 = {x: bin(x)[2:] for x in range(1, 6)}

# 11. Nested dictionary comprehension (multiplication table)
d11 = {x: {y: x * y for y in range(1, 4)} for x in range(1, 4)}

# 12. Dictionary from enumerate() - mapping index to item
fruits = ["apple", "banana", "cherry"]
d12 = {index: fruit for index, fruit in enumerate(fruits)}

# 13. Transforming a dictionary of lists into a dictionary of sums
grades = {"Alice": [90, 85, 92], "Bob": [70, 80, 75]}
d13 = {name: sum(scores) for name, scores in grades.items()}

# 14. Flattening a dictionary containing another dictionary
nested = {"A": {"x": 1, "y": 2}, "B": {"x": 3, "y": 4}}
d14 = {f"{outer}_{inner}": val for outer, sub in nested.items() for inner, val in sub.items()}

# 15. Initializing a dict with dynamic default values based on key
d15 = {k: [] if k.startswith("list_") else 0 for k in ["list_a", "count_b", "list_c"]}

# 16. Filtering a dictionary by type of the value
mixed = {"a": 1, "b": "string", "c": 3.14}
d16 = {k: v for k, v in mixed.items() if isinstance(v, int)}

# 17. Mapping a list of tuples to a dictionary, modifying values
pairs = [("A", 10), ("B", 20)]
d17 = {k: v ** 2 for k, v in pairs}

# 18. Dictionary of ASCII values for an alphabet string
d18 = {char: ord(char) for char in "ABCDE"}

# 19. Filtering out dictionary items where the key and value are identical strings
data = {"a": "a", "b": "c", "d": "d"}
d19 = {k: v for k, v in data.items() if k != v}

# 20. Re-indexing a list of dicts by a specific ID field
records = [{"id": 101, "name": "A"}, {"id": 102, "name": "B"}]
d20 = {record["id"]: record for record in records}