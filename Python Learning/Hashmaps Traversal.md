In Python, you can use a dictionary to mimic the behavior of a `HashMap` from other programming languages like Java. Here’s how you can traverse a dictionary (which is a hash map in Python):

### Sample HashMap (Dictionary) in Python:

```python
my_dict = {
    "apple": 3,
    "banana": 5,
    "cherry": 7
}

```

### Traversing a Python Dictionary (HashMap):

1. **Traverse keys:**
    
    ```python
    for key in my_dict:
        print(key)
    
    ```
    
2. **Traverse values:**
    
    ```python
    for value in my_dict.values():
        print(value)
    
    ```
    
3. **Traverse both keys and values:**
    
    ```python
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")
    
    ```
    
4. **Checking existence of a key:**
    
    ```python
    if "apple" in my_dict:
        print("Key exists")
    
    ```
    
5. **Fetching a value by key with default value:**
    
    ```python
    value = my_dict.get("apple", "Not found")
    print(value)
    
    ```
    

This is the basic way to traverse and manipulate a dictionary (`HashMap`) in Python. Let me know if you'd like to see more advanced operations!