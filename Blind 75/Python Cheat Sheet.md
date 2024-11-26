# Python Cheat Sheet

# Numbers
___

Python's 2 main types for Numbers are **int** and **float** (or integers and floating-point numbers).

```python
type(1)   # int 
type(-10) # int
type(0)   # int
type(0.0) # float
type(2.2) # float
type(4E2) # float - 4 * 10 to the power of 2

# Arithmetic
10 + 3  # 13
10 - 3  # 7
10 * 3  # 30
10 ** 3 # 1000
10 / 3  # 3.3333333333333335
10 // 3 # 3 --> floor division - no decimals and returns an int
10 % 3  # 1 --> modulo operator - return the remainder. Good for deciding if number is even or odd

# Basic Functions
pow(5, 2)      # 25 --> like doing 5 ** 2
abs(-50)       # 50
round(5.46)    # 5
round(5.468, 2)# 5.47 --> round to nth digit
bin(512)       # '0b1000000000' --> binary format
hex(512)       # '0x200' --> hexadecimal format

# Converting Strings to Numbers
age = input("How old are you?")
age = int(age)
pi = input("What is the value of pi?")
pi = float(pi)
```

# Strings
___

Strings in Python are stored as sequences of letters in memory.

```python
type('Hellloooooo') # str

'I\'m thirsty'
"I'm thirsty"
"\n" # new line
"\t" # adds a tab

# String Indexing and Slicing
'Hey you!'[4] # y

name = 'Andrei Neagoie'
name[4]     # e
name[:]     # Andrei Neagoie
name[1:]    # ndrei Neagoie
name[:1]    # A
name[-1]    # e
name[::1]   # Andrei Neagoie
name[::-1]  # eiogaeN ierdnA
name[0:10:2]# Ade e
# : is called slicing and has the format [ start : end : step ]

#String Concatenation and Repetition

'Hi there ' + 'Timmy' # 'Hi there Timmy'
'*'*10                # **********

# Basic Functions
len('turtle') # 6


# Basic Methods
'  I am alone '.strip()               # 'I am alone' --> Strips all whitespace characters from both ends.
'On an island'.strip('d')             # 'On an islan' --> Strips all passed characters from both ends.
'but life is good!'.split()           # ['but', 'life', 'is', 'good!']
'Help me'.replace('me', 'you')        # 'Help you' --> Replaces first with second param
'Need to make fire'.startswith('Need')# True
'and cook rice'.endswith('rice')      # True
'bye bye'.index('e')                  # 2
'still there?'.upper()                # STILL THERE?
'HELLO?!'.lower()                     # hello?!
'ok, I am done.'.capitalize()         # 'Ok, I am done.'
'oh hi there'.find('i')               # 4 --> returns the starting index position of the first occurrence
'oh hi there'.count('e')              # 2

# String Formatting
name1 = 'Andrei'
name2 = 'Sunny'
print(f'Hello there {name1} and {name2}')        # Hello there Andrei and Sunny - Newer way to do things as of Python 3.6
print('Hello there {} and {}'.format(name1, name2)) # Hello there Andrei and Sunny
print('Hello there %s and %s' %(name1, name2))   # Hello there Andrei and Sunny --> %d, %f, %r for integers, floats, string representations

# Palindrome Check
word = 'reviver'
p = bool(word.find(word[::-1]) + 1)
print(p) # True
```

# Boolean
___

True or False. Used in a lot of comparison and logical operations in Python.

```python
bool(True)
bool(False)

Falsy Values

All of the below evaluate to False. Everything else will evaluate to True in Python.

print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(''))
print(bool(range(0)))
print(bool(set()))
```
See Logical Operators and Comparison Operators section for more on booleans.

# Lists
___

Unlike strings, lists are mutable sequences in Python.

```python
my_list = [1, 2, '3', True]  # We assume this list won't mutate for each example below
len(my_list)                  # 4
my_list.index('3')            # 2
my_list.count(2)              # 1 --> count how many times 2 appears

my_list[3]                    # True
my_list[1:]                   # [2, '3', True]
my_list[:1]                   # [1]
my_list[-1]                   # True
my_list[::1]                  # [1, 2, '3', True]
my_list[::-1]                 # [True, '3', 2, 1]
my_list[0:3:2]                # [1, '3']

Slicing: The format is [ start : end : step ].

# Add to List
my_list * 2                   # [1, 2, '3', True, 1, 2, '3', True]
my_list + [100]               # [1, 2, '3', True, 100] --> creates new list, does not mutate original
my_list.append(100)           # None --> Mutates original list to [1, 2, '3', True, 100]
my_list.extend([100, 200])    # None --> Mutates original list to [1, 2, '3', True, 100, 200]
my_list.insert(2, '!!!')      # None --> [1, 2, '!!!', '3', True] - Inserts item at index and moves the rest
' '.join(['Hello', 'There'])  # 'Hello There' --> Joins elements using a space separator.


# Copy a List
basket = ['apples', 'pears', 'oranges']
new_basket = basket.copy()
new_basket2 = basket[:]

# Remove from List
[1,2,3].pop()    # 3 --> mutates original list, default index is -1 (last item)
[1,2,3].pop(1)   # 2 --> mutates original list
[1,2,3].remove(2) # None --> [1, 3] Removes first occurrence of item
[1,2,3].clear()  # None --> mutates original list to [] (empty list)
del [1,2,3][0]    # Removes first element

# Ordering
[1,2,5,3].sort()         # None --> Mutates list to [1, 2, 3, 5]
[1,2,5,3].sort(reverse=True) # None --> Mutates list to [5, 3, 2, 1]
[1,2,5,3].reverse()      # None --> Mutates list to [3, 5, 2, 1]
sorted([1,2,5,3])        # [1, 2, 3, 5] --> creates new list
list(reversed([1,2,5,3]))# [3, 5, 2, 1] --> reversed() returns an iterator

# Useful Operations
1 in [1,2,5,3]   # True
min([1,2,3,4,5]) # 1
max([1,2,3,4,5]) # 5
sum([1,2,3,4,5]) # 15

# Get First and Last Element of a List
mList = [63, 21, 30, 14, 35, 26, 77, 18, 49, 10]
first, *x, last = mList
print(first)  # 63
print(last)   # 10

# Matrix
matrix = [[1,2,3], [4,5,6], [7,8,9]]
matrix[2][0] # 7 --> Grab first element of the third row


# Looping through a matrix by rows:
mx = [[1,2,3],[4,5,6]]
for row in range(len(mx)):
    for col in range(len(mx[0])):
        print(mx[row][col]) # 1 2 3 4 5 6


# Transform into a list:
[mx[row][col] for row in range(len(mx)) for col in range(len(mx[0]))] # [1,2,3,4,5,6]

# Combine columns with zip and *:
[x for x in zip(*mx)] # [(1, 3), (2, 4)]

# List Comprehensions
a = [i for i in 'hello']              # ['h', 'e', 'l', 'l', 'o']
b = [i*2 for i in [1,2,3]]            # [2, 4, 6]
c = [i for i in range(0,10) if i % 2 == 0] # [0, 2, 4, 6, 8]

# Advanced Functions
list_of_chars = list('Helloooo')                                  # ['H', 'e', 'l', 'l', 'o', 'o', 'o', 'o']
sum_of_elements = sum([1,2,3,4,5])                                # 15
element_sum = [sum(pair) for pair in zip([1,2,3],[4,5,6])]        # [5, 7, 9]
sorted_by_second = sorted(['hi','you','man'], key=lambda el: el[1]) # ['man', 'hi', 'you']
sorted_by_key = sorted([
                         {'name': 'Bina', 'age': 30},
                         {'name':'Andy', 'age': 18},
                         {'name': 'Zoey', 'age': 55}],
                         key=lambda el: (el['name'])) # [{'name': 'Andy', 'age': 18}, {'name': 'Bina', 'age': 30}, {'name': 'Zoey', 'age': 55}]

Read Line of a File into a List

with open("myfile.txt") as f:
    lines = [line.strip() for line in f]
```

# Dictionaries
___

Also known as mappings or hash tables. They are key-value pairs that are guaranteed to retain order of insertion starting from Python 3.7.

```python
my_dict = {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False}
my_dict['name']                      # Andrei Neagoie
len(my_dict)                         # 3
list(my_dict.keys())                 # ['name', 'age', 'magic_power']
list(my_dict.values())               # ['Andrei Neagoie', 30, False]
list(my_dict.items())                # [('name', 'Andrei Neagoie'), ('age', 30), ('magic_power', False)]
my_dict['favourite_snack'] = 'Grapes' # {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False, 'favourite_snack': 'Grapes'}
my_dict.get('age')                   # 30 --> Returns None if key does not exist
my_dict.get('ages', 0)               # 0  --> Returns default (2nd param) if key is not found

# Remove Key
del my_dict['name']
my_dict.pop('name', None)
my_dict.update({'cool': True})                                          # {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False, 'favourite_snack': 'Grapes', 'cool': True}
{**my_dict, **{'cool': True}}                                          # {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False, 'favourite_snack': 'Grapes', 'cool': True}
new_dict = dict([['name','Andrei'],['age',32],['magic_power',False]])   # Creates dict from key-value pairs.
new_dict = dict(zip(['name','age','magic_power'],['Andrei',32, False])) # Creates dict from two collections.
new_dict = my_dict.pop('favourite_snack')                             # Removes item from dict.

# Dictionary Comprehension
{key: value for key, value in new_dict.items() if key == 'age' or key == 'name'} # {'name': 'Andrei', 'age': 32}
```  


# Tuples
___
Like lists, but they are used for **immutable** things (that don't change).

```python
my_tuple = ('apple', 'grapes', 'mango', 'grapes')
apple, grapes, mango, grapes = my_tuple  # Tuple unpacking
len(my_tuple)                            # 4
my_tuple[2]                              # 'mango'
my_tuple[-1]                             # 'grapes'

# Immutability
my_tuple[1] = 'donuts'  # TypeError
my_tuple.append('candy')# AttributeError

# Methods
my_tuple.index('grapes') # 1
my_tuple.count('grapes') # 2


# Zip
list(zip([1, 2, 3], [4, 5, 6])) # [(1, 4), (2, 5), (3, 6)]

# Unzip
z = [(1, 2), (3, 4), (5, 6), (7, 8)] # Some output of zip() function
unzip = lambda z: list(zip(*z))
unzip(z)
```

# Sets
___
An unordered collection of unique elements.
```python
my_set = set()
my_set.add(1)   # {1}
my_set.add(100) # {1, 100}
my_set.add(100) # {1, 100} --> no duplicates!


# Converting to Set
new_list = [1, 2, 3, 3, 3, 4, 4, 5, 6, 1]
set(new_list)  # {1, 2, 3, 4, 5, 6}

# Removing Elements
my_set.remove(100)   # {1} --> Raises KeyError if element not found
my_set.discard(100)  # {1} --> Doesn't raise an error if element not found
my_set.clear()       # {}

# Copying a Set
new_set = {1, 2, 3}.copy()  # {1, 2, 3}

# Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set3 = set1.union(set2)                # {1, 2, 3, 4, 5}
set4 = set1.intersection(set2)         # {3}
set5 = set1.difference(set2)           # {1, 2}
set6 = set1.symmetric_difference(set2) # {1, 2, 4, 5}

set1.issubset(set2)                    # False
set1.issuperset(set2)                  # False
set1.isdisjoint(set2)                  # False --> Returns True if two sets have no intersection.
```

### Frozenset

A hashable version of a set, which can be used as a key in a dictionary or as an element in another set.
```python
<frozenset> = frozenset(<collection>)
```

# `None`
***

`None` is used for the absence of a value and can indicate that nothing has been assigned to an object.

```python
type(None)  # NoneType
a = None
```

# Comparison Operators
***
```python
	•	== : equal values
	•	!= : not equal
	•	>  : left operand is greater than right operand
	•	<  : left operand is less than right operand
	•	>= : left operand is greater than or equal to right operand
	•	<= : left operand is less than or equal to right operand
	•	<element> is <element> : check if two operands refer to the same object in memory
```

# Logical Operators
***
```python
1 < 2 and 4 > 1  # True
1 > 3 or 4 > 1   # True
1 is not 4       # True
not True         # False
1 not in [2, 3, 4]  # True

Conditional Statements

if <condition that evaluates to boolean>:
    # perform action1
elif <condition that evaluates to boolean>:
    # perform action2
else:
    # perform action3
```

# Loops
***
Iterating through Lists, Tuples, Strings, and Dictionaries
```python
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_list2 = [(1, 2), (3, 4), (5, 6)]
my_dict = {'a': 1, 'b': 2, 'c': 3}

for num in my_list:
    print(num)  # 1, 2, 3

for num in my_tuple:
    print(num)  # 1, 2, 3

for num in my_list2:
    print(num)  # (1, 2), (3, 4), (5, 6)

for num in '123':
    print(num)  # 1, 2, 3

for k, v in my_dict.items():  # Dictionary Unpacking
    print(k)  # 'a', 'b', 'c'
    print(v)  # 1, 2, 3

While Loops

while <condition that evaluates to boolean>:
    # action
    if <condition that evaluates to boolean>:
        break  # break out of while loop
    if <condition that evaluates to boolean>:
        continue  # continue to the next line in the block

Example: Waiting Until User Quits

msg = ''
while msg != 'quit':
    msg = input("What should I do?")
    print(msg)
```
# Range
***
```python
range(10)           # range(0, 10) --> 0 to 9
range(1, 10)        # range(1, 10)
list(range(0, 10, 2))  # [0, 2, 4, 6, 8]
```

# Enumerate
***
```python
for i, el in enumerate('helloo'):
    print(f'{i}, {el}')
# Output:
# 0, h
# 1, e
# 2, l
# 3, l
# 4, o
# 5, o
```

# Counter
***

```python
# from collections import Counter
colors = ['red', 'blue', 'yellow', 'blue', 'red', 'blue']
counter = Counter(colors)  # Counter({'blue': 3, 'red': 2, 'yellow': 1})
counter.most_common()[0]  # ('blue', 3)
```

# Named Tuple
***

A `tuple` is an immutable and hashable list. 
A `namedtuple` is its subclass with named elements.

```python
from collections import namedtuple
Point = namedtuple('Point', 'x y')
p = Point(1, y=2)           # Point(x=1, y=2)
p[0]                        # 1
p.x                         # 1
getattr(p, 'y')             # 2
p._fields                   # Or: Point._fields -> ('x', 'y')

# Creating and using a named tuple:
from collections import namedtuple
Person = namedtuple('Person', 'name height')
person = Person('Jean-Luc', 187)
f'{person.height}'           # '187'
'{p.height}'.format(p=person) # '187'
``` 

# OrderedDict
***

An OrderedDict maintains the order of insertion.

```python
from collections import OrderedDict

# Store each person's languages, keeping track of who responded first.
programmers = OrderedDict()
programmers['Tim'] = ['python', 'javascript']
programmers['Sarah'] = ['C++']
programmers['Bia'] = ['Ruby', 'Python', 'Go']

for name, langs in programmers.items():
    print(name + '-->')
    for lang in langs:
        print('\t' + lang)
```

# Functions
***

*args and **kwargs

	•	* expands a collection into positional arguments.
	•	** expands a dictionary into keyword arguments.

```python
args = (1, 2)
kwargs = {'x': 3, 'y': 4, 'z': 5}
some_func(*args, **kwargs)  # same as some_func(1, 2, x=3, y=4, z=5)
```

Inside Function Definition

Splat combines zero or more positional arguments into a tuple, while splatty-splat combines zero or more keyword arguments into a dictionary.
```python
def add(*a):
    return sum(a)

add(1, 2, 3)  # 6

# Ordering of Parameters

def f(*args):                  # f(1, 2, 3)
def f(x, *args):               # f(1, 2, 3)
def f(*args, z):               # f(1, 2, z=3)
def f(x, *args, z):            # f(1, 2, z=3)

def f(**kwargs):               # f(x=1, y=2, z=3)
def f(x, **kwargs):            # f(1, y=2, z=3)

def f(*args, **kwargs):        # f(1, 2, z=3) | f(1, 2, 3)
def f(x, *args, **kwargs):     # f(1, 2, 3)
def f(*args, y, **kwargs):     # f(1, y=2, z=3)
def f(x, *args, z, **kwargs):  # f(1, 2, z=3)

# Other Uses of *

[*[1, 2, 3], *[4]]                # [1, 2, 3, 4]
{*[1, 2, 3], *[4]}                # {1, 2, 3, 4}
(*[1, 2, 3], *[4])                # (1, 2, 3, 4)
{**{'a': 1, 'b': 2}, **{'c': 3}}  # {'a': 1, 'b': 2, 'c': 3}
head, *body, tail = [1, 2, 3, 4, 5]
```

# Lambda
***

```python
Lambda syntax:

# lambda: <return_value>
# lambda <argument1>, <argument2>: <return_value>

# Factorial
from functools import reduce
n = 3
factorial = reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial)  # 6

# Fibonacci

fib = lambda n: n if n <= 1 else fib(n - 1) + fib(n - 2)
result = fib(10)
print(result)  # 55
```  

# Comprehensions
***

```python
# List Comprehension
[i + 1 for i in range(10)]         # [1, 2, ..., 10]

# Set Comprehension
{i for i in range(10) if i > 5}    # {6, 7, 8, 9}

# Generator Comprehension
(i + 5 for i in range(10))         # (5, 6, ..., 14)

# Dictionary Comprehension
{i: i * 2 for i in range(10)}      # {0: 0, 1: 2, ..., 9: 18}

# Nested Comprehension
output = [i + j for i in range(3) for j in range(3)]  # [0, 1, 2, 1, 2, 3, 2, 3, 4]
# Equivalent to:
output = []
for i in range(3):
    for j in range(3):
        output.append(i + j)
```

# Ternary Condition
***
```python
# <expression_if_true> if <condition> else <expression_if_false>
[a if a else 'zero' for a in [0, 1, 0, 3]]  # ['zero', 1, 'zero', 3]
```

# Map, Filter, Reduce
***

```python
from functools import reduce
list(map(lambda x: x + 1, range(10)))             # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x > 5, range(10)))          # [6, 7, 8, 9]
reduce(lambda acc, x: acc + x, range(10))         # 45
```

# Any, All
```python
any([False, True, False])  # True if at least one item in collection is truthy, False if empty.
all([True, 1, 3, True])    # True if all items in collection are true
```

# Closures
---

We have a closure in Python when:
A nested function references a value of its enclosing function and then
the enclosing function returns the nested function.
```python
def get_multiplier(a):
    def out(b):
        return a * b
    return out

>>> multiply_by_3 = get_multiplier(3)
>>> multiply_by_3(10)  # 30
```

If multiple nested functions within an enclosing function reference the same value, that value gets shared.

To dynamically access a function’s first free variable, use <function>.__closure__[0].cell_contents.

# Scope
***

If a variable is being assigned to anywhere in the scope, it is regarded as a local variable, unless it is declared as global or nonlocal.
```python
def get_counter():
    i = 0
    def out():
        nonlocal i
        i += 1
        return i
    return out

>>> counter = get_counter()
>>> counter(), counter(), counter()  # (1, 2, 3)
```

# Modules
***

```python
if __name__ == '__main__':  # Runs main() if file wasn't imported.
    main()

import <module_name>
from <module_name> import <function_name>
import <module_name> as m
from <module_name> import <function_name> as m_function
from <module_name> import *
```

# Iterators
***

In this cheatsheet, <collection> can also mean an iterator.
```python
<iter> = iter(<collection>)
<iter> = iter(<function>, to_exclusive)     # Sequence of return values until 'to_exclusive'.
<el>   = next(<iter> [, default])           # Raises StopIteration or returns 'default' on end.
```

# Generators
***
```python
Convenient way to implement the iterator protocol.

def count(start, step):
    while True:
        yield start
        start += step

>>> counter = count(10, 2)
>>> next(counter), next(counter), next(counter)  # (10, 12, 14)
```
