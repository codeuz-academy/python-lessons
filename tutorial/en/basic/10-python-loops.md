---
layout: tutorial.njk
title: Python Loop
order: 10
permalink: /tutorial/en/python-loops/
---

<img src="/img/tutorial/10-tutorial-loop-pada-python.webp" alt="Python Loops - While, For, Nested Loop" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

In general, statements in programming languages will be executed sequentially. The first statement in a function is run first, followed by the second, and so on. But there will be situations where you have to write a lot of code, where the code is very much. If done manually then you will only waste energy by writing hundreds or even thousands of codes. For that you need to use repetition (loop) in the Python programming language.

In Python programming language repetition is divided into 3 types, namely:

- While Loop
- For Loop
- Nested Loop

### While Loop

While Loop repetition in Python programming language executes statement many times as long as condition is true or `True`.

Below is an example of using While Loop repetition.

```python
#Example of using While Loop
#Note: Determining scope in Python can use tabs instead of using brackets

count = 0
while (count < 9):
  print("The count is: ", count)
  count = count + 1

print("Good bye!")
```

### For Loop

`for` repetition in Python has the ability to repeat items from any sequence, such as `list` or `string`.

Below is an example of using For Loop repetition.

```python
#Example of simple for loop
numbers = [1,2,3,4,5]
for x in numbers:
  print(x)

#Example of for loop
fruits = ["pineapple", "apple", "orange"]
for food in fruits:
  print("I like to eat", food)
```

### Nested Loop

Python programming language allows using one loop inside another loop. The following section shows some examples to illustrate the concept.

#### Nested `for` Loop

```python
# Example: print coordinate pairs
for row in range(1, 4):
  for col in range(1, 4):
    print(f"({row},{col})", end=" ")
  print()
```

#### Nested `while` Loop

```python
# Example: multiplication table 1..3
row = 1
while row <= 3:
  col = 1
  while col <= 3:
    print(f"{row}x{col}={row * col}", end="  ")
    col += 1
  print()
  row += 1

print("Good bye!")
```
