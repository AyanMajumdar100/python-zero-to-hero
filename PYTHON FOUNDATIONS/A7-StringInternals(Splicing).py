# SPLICING : segmenting string objects based on needs; STRING IS IMMUTABLE,
# So, when we splice a string it creates a brand new object in memory with the carved letters
# SYNTAX : string_var[start:end:step]

original = "Ayan Majumdar"
length = len(original)
# 1. WAYS TO Reverse a String
rev = original[length:0:-1] # radmujaM nay  [A is cut out of range]
rev = original[length::-1]  # works
rev = original[::-1]        # works
print(rev)

# 2. Extract every 2nd item from the end
ext1 = original[length::-2]
print(ext1)

# The slice gets its own unique memory address
print(f"Original ID : {id(original)} ('{original}')")
print(f"Slice ID    : {id(ext1)} ('{ext1}')")
# Original ID : 1510738055280 ('Ayan Majumdar')
# Slice ID    : 1510737483440 ('rdua aA')

# 3. Extract a specific inner chunk, reversed
print(original[length:4:-1])

# 4. MORE ON NEGATIVE INDEXING
seq = "0123456789"

# Strip the first and last characters
print(seq[1:-1])        # Output: '12345678'

# Get the last N elements 
n = 3
print(seq[-n:])         # Output: '789'

# Get everything EXCEPT the last N elements
print(seq[:-3])         # Output: '0123456'

# Slice using only negative indices (going forward)
print(seq[-8:-2])       # Output: '234567'

# Slice using only negative indices (going backward)
print(seq[-2:-8:-1])    # Output: '876543'

# Conflicting directions return an empty sequence (No error thrown!)
print(seq[2:8:-1]) 


# 5. Shallow copy a list (Creates a new list object with the same top-level data)
seq_copy = seq[:]


# 6. Reversing every row in a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Original matrix : {matrix}")         # Original matrix : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
reversed_matrix = [row[::-1] for row in matrix]
print(f"Reversed Rows : {reversed_matrix}")  # Output: [[3, 2, 1], [6, 5, 4], [9, 8, 7]]



# LIST SPLICING EXAMPLES

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# INSERT IN LIST WHILE REPLACING ELEMENTS
lst[2:4] = [100,100,100,100,100]
print(lst)  # OUTPUT : [0, 1, 100, 100, 100, 100, 100, 4, 5, 6, 7, 8, 9]

lst[2:4] = [100]
print(lst)  # OUTPUT : [0, 1, 100, 4, 5, 6, 7, 8, 9]

# INSERT IN LIST WITHOUT REPLACING
lst = [0, 1, 2]
lst[1:1] = [99, 100]    # Since end index is omitted and its same as start index so that element is kept and not replaced
# lst is now: [0, 99, 100, 1, 2]


# Replace an extended slice (Step > 1).
lst = [0, 1, 2, 3, 4, 5]

# ERROR : 
# ValueError: attempt to assign sequence of size 4 to extended slice of size 3)
lst[::2] = [99, 99, 99, 99]
print(lst)

# CORRECT : 
# The injected list MUST perfectly match the length of the replaced slice.
lst = [0, 1, 2, 3, 4, 5]
lst[::2] = [99, 99, 99]
print(lst)      # OUTPUT : [99, 1, 99, 3, 99, 5]

# Delete elements using slicing
lst = [0, 1, 2, 3, 4, 5]
del lst[1::2]
print(lst)      # [0, 2, 4]

# CLEAR LIST
lst[:] = []
print(lst)
