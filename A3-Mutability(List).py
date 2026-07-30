# RECALL TUPLES A BIT - Immutablility, packing, unpacking,index(), count(), Use , for singleton tuple or else will be considered int
# fruits = ("apple", "banana", "orange", "kiwi", "banana")

# NOW MUTABLE DATATYPES IN PYTHON
# 1. LISTS
# (ORDERED, MUTABLE COLLECTIONS)
fruits = ["Apple", "Banana", "Cherry"]
print(f"Original List - FRUITS : {fruits}")     # returns Updated List - FRUITS : ['Apple', 'Banana', 'Cherry', 'Kiwi']
# LIST METHODS 
# 1. append(item) - Adds an item to the very end of the list
fruits.append("Kiwi")
print(f"Updated List - FRUITS : {fruits}")      # returns Updated List - FRUITS : ['Apple', 'Banana', 'Cherry', 'Kiwi']

# 2. insert(index, item) - Inserts item at the given index
fruits.insert(2, "Mango")  # Add this twice
print(f"Index inserted List - FRUITS : {fruits}")       # returns Index inserted List - FRUITS : ['Apple', 'Banana', 'Mango', 'Cherry', 'Kiwi']
# fruits.insert("Durian") -> you need to specify the index or else error

# 3. remove(item) - Removes the first matching item from the list
fruits.remove("Mango")  # -> Removes the first instance of mango at index 2

# 4. pop(index) - Removes and returns the item at given index (default = last)
popped_fruit = fruits.pop(2)
# OUTPUT : Popped fruit : Mango | Fruits List : ['Apple', 'Banana', 'Mango', 'Cherry', 'Kiwi']
print(f"Popped fruit : {popped_fruit} | Fruits List : {fruits}")

# 5. sort() - Sorts the list alphabetically or numerically in place
fruits.sort()
print(f"After sort FRUITS : {fruits}")
# OUTPUT : After sort FRUITS : ['Apple', 'Banana', 'Cherry', 'Kiwi', 'Mango']

# 6. extend(iterable) - Add multiple items from another list
fruits.extend(["Durian", "Dragonfruit"])
print(f"Extended Fruits LIST : {fruits}")
# OUTPUT : Extended Fruits LIST : ['Apple', 'Banana', 'Cherry', 'Kiwi', 'Mango', 'Durian', 'Dragonfruit']

# Removes every "Mango"
fruits = [x for x in fruits if x != "Mango"] 

# OTHER LIST FUNCTIONS

# 1. count(item)
apple_count = fruits.count("apple")

# 2. index(item, [start], [end])
mango_idx = fruits.index("mango")       # Returns 2
# ValueError try-except block
try:
    idx = fruits.index("ABCD")
    print(f"Found at index: {idx}")
except ValueError:
    print(f"ABCD does not exist in the list.")

# 3. reverse()
fruits.reverse() 
print(f"Reversed Fruits LIST : {fruits}")

# 4. copy()
new_fruits = fruits.copy()
print(f"COPIED LIST : {new_fruits}")

# 5. clear()
new_fruits.clear()
print(f"Cleared new_fruits LIST : {new_fruits}")

# 6. len(list)
print(fruits)
print(len(fruits))