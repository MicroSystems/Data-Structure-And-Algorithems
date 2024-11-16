# Data Structure And Algorithms (Python)
In Python, lists are one of the most versatile and commonly used data structures. Here are some of the most commonly used list functions and methods:

### 1. **Creating a List**

```python
my_list = [1, 2, 3, 4, 5]

```

### 2. **Appending an Element**

- Adds a single element to the end of the list.

```python
my_list.append(6)
# Output: [1, 2, 3, 4, 5, 6]

```

### 3. **Extending a List**

- Adds multiple elements to the end of the list.

```python
my_list.extend([7, 8, 9])
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

```

### 4. **Inserting an Element**

- Inserts an element at a specific index.

```python
my_list.insert(2, 'a')
# Output: [1, 2, 'a', 3, 4, 5, 6]

```

### 5. **Removing an Element by Value**

- Removes the first occurrence of the value.

```python
my_list.remove('a')
# Output: [1, 2, 3, 4, 5, 6]

```

### 6. **Popping an Element**

- Removes and returns the element at the specified index (default is the last element).

```python
my_list.pop()       # Removes and returns the last element
# Output: 6 (element removed), list becomes [1, 2, 3, 4, 5]

my_list.pop(1)      # Removes the element at index 1
# Output: 2 (element removed), list becomes [1, 3, 4, 5]

```

### 7. **Finding the Index of an Element**

- Returns the index of the first occurrence of the value.

```python
index = my_list.index(3)
# Output: 1

```

### 8. **Counting Occurrences**

- Counts how many times a value occurs in the list.

```python
count = my_list.count(3)
# Output: 1

```

### 9. **Sorting a List**

- Sorts the list in ascending order (in-place or returns a new sorted list).

```python
my_list.sort()
# Output: [1, 3, 4, 5]

# To get a new sorted list without modifying the original:
sorted_list = sorted(my_list)

```

### 10. **Reversing a List**

- Reverses the order of the list.

```python
my_list.reverse()
# Output: [5, 4, 3, 1]

```

### 11. **List Comprehension**

- Creates a new list by applying an expression to each element.

```python
squared = [x**2 for x in my_list]
# Output: [25, 16, 9, 1]

```

### 12. **Checking Membership**

- Checks if an element exists in the list.

```python
exists = 4 in my_list
# Output: True

```

### 13. **Copying a List**

- Creates a shallow copy of the list.

```python
new_list = my_list.copy()
# Output: [5, 4, 3, 1]

```

### 14. **Clearing a List**

- Removes all elements from the list.

```python
my_list.clear()
# Output: []

```

These are some of the most frequently used functions and methods in Python when working with lists. Let me know if you need further clarification on any of them!