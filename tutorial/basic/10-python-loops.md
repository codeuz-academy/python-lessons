---
layout: tutorial.njk
title: Python Loop
order: 10
permalink: /tutorial/python-loops/
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

Below is an example of using Nested Loop.

```python
#Example of using Nested Loop
#Note: Use of modulo on conditional assumes non-zero value as True and zero as False

i = 2
while(i < 100):
  j = 2
while(j <= (i/j)):
  if not(i%j): break
  j = j + 1
  if (j > i/j) : print(i, " is prime")
    i = i + 1

print("Good bye!")
```
