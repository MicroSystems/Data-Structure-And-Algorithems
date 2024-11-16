# HashMaps

In Python, **HashMaps** are implemented as **dictionaries** (using the `dict` type). Here are the most commonly used dictionary functions and methods:

### 1. **Creating a Dictionary**

- A dictionary is created using curly braces `{}` with key-value pairs.

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

```

### 2. **Accessing a Value by Key**

- Retrieve a value associated with a key.

```python
value = my_dict['a']
# Output: 1

```

### 3. **Adding or Updating a Key-Value Pair**

- You can add a new key-value pair or update an existing one by assigning to the key.

```python
my_dict['d'] = 4   # Adding a new key-value pair
my_dict['a'] = 10  # Updating the value for an existing key
# Output: {'a': 10, 'b': 2, 'c': 3, 'd': 4}

```

### 4. **Removing a Key-Value Pair**

- You can remove a key-value pair using the `del` keyword or the `pop()` method.

```python
del my_dict['b']   # Deletes the key 'b'
# Output: {'a': 10, 'c': 3, 'd': 4}

# Using pop() to remove and return the value of the key
value = my_dict.pop('c')
# Output: 3 (value of 'c'), dictionary becomes {'a': 10, 'd': 4}

```

### 5. **Checking if a Key Exists**

- Use the `in` keyword to check if a key is in the dictionary.

```python
exists = 'a' in my_dict
# Output: True

```

### 6. **Getting a Value with a Default**

- Use `get()` to retrieve a value, returning a default if the key does not exist (instead of raising a `KeyError`).

```python
value = my_dict.get('b', 0)  # Returns 0 if 'b' doesn't exist
# Output: 0

```

### 7. **Iterating Over Keys, Values, or Key-Value Pairs**

- You can loop over keys, values, or both.

```python
# Iterating over keys
for key in my_dict:
    print(key)

# Iterating over values
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)

```

### 8. **Getting All Keys, Values, or Items**

- Use `keys()`, `values()`, and `items()` to get views of the dictionary's keys, values, or key-value pairs.

```python
keys = my_dict.keys()      # dict_keys(['a', 'd'])
values = my_dict.values()  # dict_values([10, 4])
items = my_dict.items()    # dict_items([('a', 10), ('d', 4)])

```

### 9. **Copying a Dictionary**

- Use `copy()` to create a shallow copy of the dictionary.

```python
new_dict = my_dict.copy()
# Output: {'a': 10, 'd': 4}

```

### 10. **Merging Two Dictionaries**

- Use the `update()` method to merge another dictionary into the current dictionary.

```python
my_dict.update({'e': 5, 'f': 6})
# Output: {'a': 10, 'd': 4, 'e': 5, 'f': 6}

```

### 11. **Clearing a Dictionary**

- Use `clear()` to remove all items from the dictionary.

```python
my_dict.clear()
# Output: {}

```

### 12. **Dictionary Comprehension**

- Create a new dictionary using a comprehension.

```python
squared_dict = {x: x**2 for x in range(5)}
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

```

### 13. **Set Default Value**

- `setdefault()` returns the value of a key if it exists; otherwise, it sets the key to a default value.

```python
value = my_dict.setdefault('g', 7)
# Output: 7 (if 'g' did not exist, it is now added with value 7)

```

### 14. **Length of a Dictionary**

- Use `len()` to get the number of key-value pairs in a dictionary.

```python
size = len(my_dict)
# Output: 2

```

### 15. **Removing and Returning an Arbitrary Item**

- `popitem()` removes and returns an arbitrary key-value pair as a tuple.

```python
key, value = my_dict.popitem()
# Output: ('f', 6)

```

These are the most frequently used functions and methods when working with dictionaries (or HashMaps) in Python. Let me know if you need more examples or explanations!