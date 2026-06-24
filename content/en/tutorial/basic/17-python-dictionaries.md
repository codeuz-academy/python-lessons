---
layout: tutorial.njk
lang: en
title: Python Dictionary
description: "Map keys to values with dictionaries and learn the safe ways to read, update, and loop over them."
order: 17
permalink: /en/tutorial/python-dictionaries/
---

<img src="/img/tutorial/17-python-dictionary-data-type.webp" alt="Python Dictionary Data Type" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Python dictionary is different from List or Tuple. Because each sequence contains key and value. Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without items is written with just two curly braces, like this: `{}`.

Dictionary keys can be of any type, but keys must be of an immutable data type such as strings, numbers, or tuples.

### Accessing Values in Python Dictionary

To access Dictionary elements, you can use the familiar square brackets along with the key to obtain its value. Here is a simple example :

Avoid naming a variable `dict`, because that shadows Python's built-in `dict()`. Use a descriptive name instead:

```python
#Example how to create Dictionary in Python

person = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("person['Name']: ", person['Name'])
print("person['Age']: ", person['Age'])
```

### Safe Access with `get()`

Reading a missing key with square brackets raises a `KeyError`. The `get()` method returns `None` (or a default you choose) instead, which is safer:

```python
person = {'Name': 'Zara', 'Age': 7}

print(person.get('Name'))          # Zara
print(person.get('City'))          # None
print(person.get('City', 'N/A'))   # N/A
```

### Checking if a Key Exists

Use the `in` operator to test for a key before accessing it:

```python
person = {'Name': 'Zara', 'Age': 7}

print('Name' in person)       # True
print('City' in person)       # False
print('City' not in person)   # True
```

### Looping Over a Dictionary

You can iterate over keys, values, or both key-value pairs at once:

```python
person = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

for key in person:                 # keys by default
    print(key)

for value in person.values():      # values
    print(value)

for key, value in person.items():  # key and value together
    print(key, "->", value)
```

### Updating Values in Python Dictionary

You can update a Dictionary by adding a new entry or a key-value pair, modifying an existing entry, or deleting an existing entry as shown in the simple example given below.

```python
#Update python dictionary

person = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
person['Age'] = 8  # Modify existing entry
person['School'] = "High School"  # Add new entry

print("person['Age']: ", person['Age'])
print("person['School']: ", person['School'])
```

### Deleting Python Dictionary Elements

You can either remove individual dictionary elements or clear the entire contents of a dictionary. You can also delete entire dictionary in a single operation.

To explicitly remove an entire dictionary, just use the del statement. Here is a simple example :

```python
#Example how to delete in Python Dictionary

person = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del person['Name']  # remove a single entry by key
print("After deleting 'Name': ", person)

person.clear()  # remove all entries, keeping the empty dictionary
print("After clear(): ", person)

del person  # delete the dictionary object entirely
# Referencing `person` after this line would raise a NameError.
```

### Built-in Functions on Python Dictionary

Python includes built-in functions as follows :

| Python Function | Explanation |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `len(dict)` | Gives the total length of the dictionary. This would be equal to the number of items in the dictionary. |
| `str(dict) ` | Produces a printable string representation of a dictionary |
| `type(variable)` | Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type. |

### Built-in Methods on Python Dictionary

Python includes built-in methods as follows :

| Python Method | Explanation |
| ------------------------------------- | ----------------------------------------------------------------------------------------- |
| `dict.clear() ` | Removes all elements of dictionary |
| `dict.copy() ` | Returns a shallow copy of dictionary |
| `dict.fromkeys() ` | Create a new dictionary with keys from seq and values set to value. |
| `dict.get(key, default=None) ` | For key, returns value or default if key not in dictionary |
| `dict.items() ` | Returns a view of the dictionary's (key, value) tuple pairs |
| `dict.keys() ` | Returns a view of the dictionary's keys |
| ` dict.setdefault(key, default=None)` | Similar to get(), but will set dict[key]=default if key is not already in dict |
| `dict.update(dict2) ` | Adds dictionary dict2's key-values pairs to dict |
| `dict.values() ` | Returns a view of the dictionary's values |
