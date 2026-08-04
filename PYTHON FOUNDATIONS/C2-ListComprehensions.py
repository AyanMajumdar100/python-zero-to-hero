# LIST COMPREHENSIONS

# 1. Ternary Map: Even or Odd labels
l1 = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]

# 2. Extracting numbers from a string
text = "I have 2 apples and 15 bananas"
l2 = [int(word) for word in text.split() if word.isdigit()]

# For complex splitting we use regex
import re
text = "I have 2 apples and 15aasdasd bananas"
# re.findall('\d+', text) automatically extracts ['2', '15']
l2 = [int(num) for num in re.findall(r'\d+', text)]
print(l2)   # Output: [2, 15]

# 3. Flattening a 2D Matrix (List of lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l3 = [num for row in matrix for num in row]

# 4. Matrix Transposition (Swapping rows and columns)
l4 = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# 5. Cartesian Product (All combinations of two lists)
colors, sizes = ["Red", "Blue"], ["S", "M"]
l5 = [(c, s) for c in colors for s in sizes]

# 6. Removing specific stop-words from a sentence
sentence = "the quick brown fox jumps over the lazy dog".split()
stops = {"the", "over"}
l6 = [word for word in sentence if word not in stops]

# 7. FizzBuzz using list comprehension
l7 = ["FizzBuzz" if x % 15 == 0 else "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else x for x in range(1, 16)]

# 8. Unpacking a list of tuples
pairs = [("A", 1), ("B", 2), ("C", 3)]
l8 = [f"{k}={v}" for k, v in pairs]

# 9. Finding common elements in two lists (Intersection)
a, b = [1, 2, 3, 4], [3, 4, 5, 6]
l9 = [x for x in a if x in b]

# 10. Generating a deck of cards
suits, ranks = ["Hearts", "Spades"], ["King", "Queen", "Jack"]
l10 = [f"{r} of {s}" for s in suits for r in ranks]

# 11. Creating a list of cumulative sums (requires python 3.8+ walrus operator for pure one-liner, or state logic)
total = 0
l11 = [(total := total + x) for x in [1, 2, 3, 4, 5]]

# 12. Filtering a list of dictionaries by a specific key's value
users = [{"name": "A", "age": 20}, {"name": "B", "age": 30}]
l12 = [u["name"] for u in users if u["age"] >= 25]

# 13. Getting the diagonal of a square matrix
l13 = [matrix[i][i] for i in range(len(matrix))]

# 14. Nested filtering: Only keep even numbers from a 2D list
l14 = [num for row in matrix for num in row if num % 2 == 0]

# 15. Generating prime numbers up to 50
l15 = [x for x in range(2, 51) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]

# 16. Reversing only the strings in a mixed list
mixed = [1, "hello", 3.14, "world"]
l16 = [x[::-1] if isinstance(x, str) else x for x in mixed]

# 17. Creating an Identity Matrix (1s on diagonal, 0s elsewhere)
size = 3
l17 = [[1 if i == j else 0 for j in range(size)] for i in range(size)]

# 18. Stripping whitespace and lowercasing a list of raw inputs
raw = ["  APPLE ", "bAnAnA  ", "  CHerry"]
l18 = [fruit.strip().lower() for fruit in raw]

# 19. Extracting file extensions from a list of filenames
files = ["data.csv", "image.png", "script.py"]
l19 = [f.split(".")[-1] for f in files]

# 20. Chunking a flat list into pairs
flat = [1, 2, 3, 4, 5, 6]
l20 = [flat[i:i+2] for i in range(0, len(flat), 2)]