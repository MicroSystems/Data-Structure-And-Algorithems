Python’s `set` is a built-in data structure that represents an unordered collection of unique elements. It’s very useful for operations involving uniqueness, membership tests, and set theory operations.

Here are the **most commonly used functions** and operations with sets in Python:

### 1. **Creating a Set**

```python
my_set = {1, 2, 3, 4}
# or
my_set = set([1, 2, 3, 4])

```

### 2. **Adding Elements**

```python
my_set.add(5)
# my_set = {1, 2, 3, 4, 5}

```

### 3. **Removing Elements**

- **Remove with an error if element is not present:**
    
    ```python
    my_set.remove(3)
    # my_set = {1, 2, 4, 5}
    
    ```
    
- **Discard (won’t raise an error if the element isn’t found):**
    
    ```python
    my_set.discard(10)  # Does nothing if element is not present
    
    ```
    

### 4. **Clearing the Set**

```python
my_set.clear()
# my_set = set()

```

### 5. **Union of Sets** (combine sets)

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
# union_set = {1, 2, 3, 4, 5}

```

### 6. **Intersection of Sets** (common elements)

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
# intersection_set = {3}

```

### 7. **Difference of Sets** (elements in one set but not the other)

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
# difference_set = {1, 2}

```

### 8. **Symmetric Difference** (elements in either set but not both)

```python
sym_diff_set = set1.symmetric_difference(set2)
# sym_diff_set = {1, 2, 4, 5}

```

### 9. **Checking Subset**

```python
set1 = {1, 2}
set2 = {1, 2, 3}
is_subset = set1.issubset(set2)
# is_subset = True

```

### 10. **Checking Superset**

```python
set1 = {1, 2, 3}
set2 = {1, 2}
is_superset = set1.issuperset(set2)
# is_superset = True

```

### 11. **Set Length**

```python
length = len(my_set)
# length = 4 (if my_set contains {1, 2, 3, 4})

```

### 12. **Checking Element Existence**

```python
2 in my_set  # True
10 in my_set  # False

```

### 13. **Frozen Sets (Immutable Sets)**

```python
my_frozen_set = frozenset([1, 2, 3, 4])
# Similar to a set, but immutable (cannot add or remove elements)

```

### 14. **Pop an Element** (Removes and returns an arbitrary element)

```python
element = my_set.pop()  # Removes and returns a random element

```

These functions provide the core capabilities of Python’s `set` data structure, allowing you to perform common set operations efficiently.