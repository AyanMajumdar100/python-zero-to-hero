# 1. Getting unique lengths of words in a list
words = ["apple", "bat", "car", "banana", "cat"]
s1 = {len(word) for word in words} # Results in {3, 5, 6}

# 2. Extracting unique vowels from a string
sentence = "education is important"
s2 = {char for char in sentence if char in "aeiou"}

# 3. Flattening a 2D list into a set of unique numbers
matrix = [[1, 2, 2], [2, 3, 3], [4, 4, 5]]
s3 = {num for row in matrix for num in row}

# 4. Generating a set of random-like deterministic hashes/math outputs
s4 = {x % 7 for x in range(100)} # Will only ever contain {0,1,2,3,4,5,6}

# 5. Extracting unique file extensions from a messy list of files
files = ["img.png", "doc.TXT", "script.py", "photo.PNG"]
s5 = {f.split(".")[-1].lower() for f in files}

# 6. Finding all unique characters shared across multiple words (Intersection logic via loops)
words = ["apple", "maple", "staple"]
s6 = {char for char in words[0] if all(char in w for w in words[1:])}

# 7. Unpacking unique values from a dictionary of lists
data = {"A": [1, 2], "B": [2, 3], "C": [3, 4]}
s7 = {val for lst in data.values() for val in lst}

# 8. Grouping anagrams by using sorted tuples as intermediate keys, then extracting uniqueness
words = ["rat", "tar", "art", "bat", "tab"]
s8 = {"".join(sorted(w)) for w in words} # Unique signatures: {'art', 'abt'}

# 9. Set of tuples (coordinates) within a certain distance from origin
s9 = {(x, y) for x in range(-5, 6) for y in range(-5, 6) if (x**2 + y**2)**0.5 <= 3}

# 10. Extracting all unique first characters from a list of strings
names = ["Alice", "Bob", "Charlie", "Amanda"]
s10 = {name[0] for name in names}

# 11. Creating a set of numbers that are divisible by both 3 and 5
s11 = {x for x in range(100) if x % 3 == 0 and x % 5 == 0}

# 12. Removing punctuation from a string and getting unique words
import string
text = "Hello, world! Hello universe."
s12 = {word.strip(string.punctuation).lower() for word in text.split()}

# 13. Unique combinations of rolling two six-sided dice (Ignoring order via min/max)
s13 = {(min(d1, d2), max(d1, d2)) for d1 in range(1, 7) for d2 in range(1, 7)}

# 14. Getting all unique types from a heavily mixed list
mixed = [1, 2.0, "three", True, None, [1], {2}]
s14 = {type(item).__name__ for item in mixed}

# 15. Set of perfect squares under 1000
s15 = {x**2 for x in range(32) if x**2 < 1000}

# 16. Filtering out unique valid email domains from a raw list
emails = ["a@gmail.com", "b@yahoo.com", "c@gmail.com", "invalid_email"]
s16 = {e.split("@")[1] for e in emails if "@" in e}

# 17. Generating a set of distinct leap years from a list of random years
years = [2000, 2001, 2004, 2100, 2024]
s17 = {y for y in years if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)}

# 18. Creating a set of purely alphabetical strings from messy inputs
inputs = ["Python", "C++", "Java!", "Ruby"]
s18 = {lang for lang in inputs if lang.isalpha()}

# 19. Set of unique directory paths from absolute file paths
paths = ["/usr/bin/python", "/usr/bin/bash", "/var/log/syslog"]
s19 = {"/".join(p.split("/")[:-1]) for p in paths}

# 20. Frozenset comprehension (You wrap a generator expression in frozenset())
s20 = frozenset(x for x in range(10) if x % 2 == 0)