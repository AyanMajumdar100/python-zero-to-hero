# LETS RECALL DICTIONARY : dict_3 = dict(name = "Aryan", age = 25, nickname = "Pepe") dict1.get(key, default), dict1.keys(), dict1.values(), dict1.items(), dict1.update(dict1), dict1.pop(key), dict_name.popitem(), dict1.setdefault(), dict1.copy()
# WAYS TO ADD : Direct Assignment - dict1[key] = value,dic1.setdefault(key,value), dict1.update(dict2)
# WAYS TO REMOVE : dic1.pop(key,default), dic1.popitem(), del dict1[key], dict1.clear(), del d1
# ITERATION THROUGH DICTIONARIES (keys, values, items, next&None for lookups)
# all_true = all(squares_dict) any_true = any(squares_dict) [ANY 0 KEY  = FALSY]


# SETS : UNIQUE, UNORDERED(HASHING)
# 2 Types : set & frozenset

# Empty set is denoted by "set()" method and not {} - this is for dictionary
empty_set = set()
print(empty_set)    # set()
# ANOTHER WAY OF SET CREATION
set_1 = set([1,2,3])
print(set_1)    # {1, 2, 3}

set_a = {1, 2, 3, 4}
set_b = {4, 5, 6, 7}

# Methods for sets
# 1. set.add(item)
set_a.add(99)
print(set_a)    # {1, 2, 99, 3, 4} -> Unordered

# 2. remove(item) - Removes the item, but crashes if not present
set_a.remove(99)    # Will work
set_a.remove(100)   # Will crash [KeyError: 100]

# 3. discard(item) - safer
set_a.discard(100)  # Takes only 1 arguement, no fallback

# 4. copy() - Shallow copy
copy_set = set_a.copy()
print(copy_set)     # {1, 2, 3}

# 5. union()  OR  | - Combine both sets but ignore dupes
print(set_a.union(set_b))
print(set_a | set_b)    # {1, 2, 3, 4, 5, 6, 7}

# 6. intersection  OR  & - Find only the common elements
print(set_a.intersection(set_b))
print(set_a & set_b)    # {4}

# 7. Difference  OR  -  : Only elements unique to first set (common elements deleted)
print(set_a.difference(set_b))
print(set_a - set_b)    # {1, 2, 3}
print(set_b - set_a)    # {5, 6, 7}

# 8. Symmetric Difference  OR  ^ - uncommon in both
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)    # {1, 2, 3, 5, 6, 7}
print(set_b ^ set_a)    # {1, 2, 3, 5, 6, 7}

# 9. pop() - removes and returns an arbitrary element in the set (Since unordered)
print(set_a)
item = set_a.pop()
print(f"Arbitrary Popped Item : {item}")    # Arbitrary Popped Item : 1

# 10. set1.update(set2) - union of 2 sets
set1 = set([1,2,3,4])
set2 = set([3,4,5,6,7])
set1.update(set2)
print(set1)         # {1, 2, 3, 4, 5, 6, 7}


# INPLACE MATHEMATICAL MUTATIONS (Reassign set_a & set_b after every function call here) - UPDATES HAPPEN ON THE FIRST SET
# 1. Intersection Update - removes items from 1st set which arent present in second set
set_a.intersection_update(set_b)
set_a &= set_b
print(set_a)        # {4}

# 2. Difference Update - removes the common elements from 1st set which are present in second set
set_a.difference_update(set_b)
set_a -= set_b
print(set_a)        # {1, 2, 3}

# 3. Symmetric Difference Update - 
set_a.symmetric_difference_update(set_b)
set_a ^= set_b
print(set_a)        # {1, 2, 3, 5, 6, 7}

# EVALUATION AND RELATIONSHIPS (RETURN True/False results)
set1 = set([1,2,3])
set2 = set([5,6,7])
set3 = set([1,2,3,4,5,6])
print(set1,set2,set3)       # {1, 2, 3} {5, 6, 7} {1, 2, 3, 4, 5, 6}

# 1. set1.isdisjoint(set2) - No intersection = True
print(set1.isdisjoint(set2))    # True
print(set1.isdisjoint(set3))    # False

# 2. set1.issubset(set2) - All elements of 1 are present in 2
print(set1.issubset(set3))      # True
print(set3.issubset(set1))      # False

# 3. set1.issuperset(set2) - All elements of 2 are present in 1
print(set1.issuperset(set3))    # False
print(set3.issuperset(set1))    # True

# OTHER BUILT IN METHODS PERFORMED ON SETS
print(len(set1))    # 3
print(all(set1))    # True
print(any(set1))    # True

set1.clear()
print(set1)         # set()


# FROZEN SET - IMMUTABLE, UNIQUE, UNORDERED
frozen_set = frozenset(["apple", "banana", "cherry"])
print(frozen_set)   # frozenset({'cherry', 'banana', 'apple'})

frozen_set.add(100) #AttributeError: 'frozenset' object has no attribute 'add'
