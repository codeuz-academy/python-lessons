---
layout: tutorial.njk
lang: en
title: Python Dictionary
description: "Learn Python Dictionary in Python with practical examples and clear explanations."
order: 17
permalink: /en/tutorial/python-dictionaries/
---

<img src="/img/tutorial/17-python-dictionary-data-type.webp" alt="Python Dictionary Data Type" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Python dictionary is different from List or Tuple. Because each sequence contains key and value. Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without items is written with just two curly braces, like this: `{}`.

Dictionary keys can be of any type, but keys must be of an immutable data type such as strings, numbers, or tuples.

### Accessing Values in Python Dictionary

To access Dictionary elements, you can use the familiar square brackets along with the key to obtain its value. Here is a simple example :

```python
#Example how to create Dictionary in Python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
```

### Updating Values in Python Dictionary

You can update a Dictionary by adding a new entry or a key-value pair, modifying an existing entry, or deleting an existing entry as shown in the simple example given below.

```python
#Update python dictionary

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # Modify existing entry
dict['School'] = "DPS School" # Add new entry

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
```

### Deleting Python Dictionary Elements

You can either remove individual dictionary elements or clear the entire contents of a dictionary. You can also delete entire dictionary in a single operation.

To explicitly remove an entire dictionary, just use the del statement. Here is a simple example :

```python
#Example how to delete in Python Dictionary

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name'] # remove entry with key 'Name'
dict.clear() # remove all entries in dict
del dict # delete entire dictionary

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
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
| `dict.items() ` | Returns a list of dict's (key, value) tuple pairs |
| `dict.keys() ` | Returns list of dictionary keys |
| ` dict.setdefault(key, default=None)` | Similar to get(), but will set dict[key]=default if key is not already in dict |
| `dict.update(dict2) ` | Adds dictionary dict2's key-values pairs to dict |
| `dict.values() ` | Returns list of dictionary values |
