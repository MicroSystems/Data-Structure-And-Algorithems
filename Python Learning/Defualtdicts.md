Defaultdicts
In Python, a defaultdict is a subclass of the built-in dict (dictionary) class from the collections module. It provides a default value for a nonexistent key, which makes it useful for handling missing keys and simplifies the code for certain operations.
Key Features of defaultdict:
Default Factory Function: When a key that doesn’t exist is accessed, the defaultdict automatically creates a default value using the factory function provided when the defaultdict is initialized.
Avoids Key Errors: It eliminates the need to check whether a key exists before accessing or modifying its value.
Basic Usage
Importing defaultdict
from collections import defaultdict

​
Initializing a defaultdict
You need to provide a factory function that generates the default value. Common factory functions include int, list, and set.
# Using int as the factory function
# Default value will be 0 (since int() returns 0)
default_dict_int = defaultdict(int)

# Using list as the factory function
# Default value will be an empty list (since list() returns [])
default_dict_list = defaultdict(list)

# Using set as the factory function
# Default value will be an empty set (since set() returns set())
default_dict_set = defaultdict(set)

​
Examples
Example 1: Using int as the Default Factory
from collections import defaultdict

# Initialize defaultdict with int factory function
default_dict = defaultdict(int)

default_dict['a'] += 1
default_dict['b'] += 2

print(default_dict)
# Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})

print(default_dict['c'])
# Output: 0 (default value for non-existent key 'c')

​
Example 2: Using list as the Default Factory
from collections import defaultdict

# Initialize defaultdict with list factory function
default_dict = defaultdict(list)

default_dict['fruits'].append('apple')
default_dict['fruits'].append('banana')
default_dict['vegetables'].append('carrot')

print(default_dict)
# Output: defaultdict(<class 'list'>, {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']})

print(default_dict['unknown'])
# Output: [] (default value for non-existent key 'unknown')

​
Example 3: Using set as the Default Factory
from collections import defaultdict

# Initialize defaultdict with set factory function
default_dict = defaultdict(set)

default_dict['even'].add(2)
default_dict['even'].add(4)
default_dict['odd'].add(1)
default_dict['odd'].add(3)

print(default_dict)
# Output: defaultdict(<class 'set'>, {'even': {2, 4}, 'odd': {1, 3}})

print(default_dict['primes'])
# Output: set() (default value for non-existent key 'primes')

​
Summary
defaultdict: A dictionary-like object that provides a default value for nonexistent keys.
Factory Function: Specifies the default value type (e.g., int, list, set).
Key Advantages: Simplifies code by eliminating explicit checks for key existence and avoids KeyError.
Using defaultdict can greatly simplify code where default values are frequently needed, such as counting occurrences or grouping data.
