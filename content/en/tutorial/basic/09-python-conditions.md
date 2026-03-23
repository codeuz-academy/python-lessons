---
layout: tutorial.njk
lang: en
title: Python Conditions
description: "Learn Python Conditions in Python with practical examples and clear explanations."
order: 9
permalink: /en/tutorial/python-conditions/
---

<img src="/img/tutorial/9-python-if-else-conditions.webp" alt="Python If Else Conditions" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

### `if` Condition

Decision making (`if` condition) is used to anticipate conditions that occur during program execution and determine what actions will be taken according to the conditions.

In Python there are several statements/conditions including `if`, `else` and `elif`. `if` condition is used to execute code if the condition is true `True`.

If the condition is false `False` then the `if` statement/condition will not be executed.

Below is an example of using `if` condition in Python

```python
#If condition is a condition that will be executed by program if it is true or TRUE

score = 9

#if condition is true/TRUE then program will execute command below it
if(score > 7):
    print("Nine is Greater Than Seven") # True Condition, Executed

#if condition is false/FALSE then program will not execute command below it
if(score > 10):
    print("Nine is Greater Than Ten") # False Condition, Not Executed
```

From the example above, if the program is run it will print string `"Nine is Greater Than Seven"` once which is in the first if. In the second if, the statement is false, so the command `print("Nine is Greater Than Seven")` will not be executed.

### `if` `else` Condition

Decision making (`if` `else` condition) is not only used to determine what action will be taken according to the condition, but also used to determine what action will be taken/run if the condition is not suitable.

In Python there are several statements/conditions including `if`, `else` and `elif`. `if` condition is used to execute code if the condition is true.

`if` `else` condition is a condition where if the statement is true `True` then the code in if will be executed, but if it is false `False` then it will execute code in else.

Below is an example of using `if` `else` condition in Python

```python
# If else condition is if condition is TRUE then it will be executed generally in if,
# but if it is FALSE then it will be executed code in else

score = 3
# If statement in if is TRUE then if will be executed,
# but if FALSE code in else will be executed.
if(score > 7):
    print("Congratulations You Passed")
else:
    print("Sorry You Did Not Pass")
```

In the example above, if the program is run it will print string `"Sorry You Did Not Pass"` because the statement in if is `False`.

### `elif` Condition

Decision making (`if` `elif` condition) is a continuation/logical branching of "`if` condition". With elif we can create program code that will select several possibilities that could happen. Almost the same as "else" condition, the difference is "elif" condition can be many and not just one.

Below is an example of using `elif` condition in Python

```python
#Example of using elif condition

today = "Sunday"

if(today == "Monday"):
    print("I will go to college")
elif(today == "Tuesday"):
    print("I will go to college")
elif(today == "Wednesday"):
    print("I will go to college")
elif(today == "Thursday"):
    print("I will go to college")
elif(today == "Friday"):
    print("I will go to college")
elif(today == "Saturday"):
    print("I will go to college")
elif(today == "Sunday"):
    print("I will be on vacation")
```

In the example above, if the program is run it will print string `"I will be on vacation"`.

### Match Case (Python 3.10+)

Starting from Python 3.10, **Structural Pattern Matching** feature is available with `match-case` which is similar to `switch-case` in other programming languages. This is very useful to replace long `elif` chains.

```python
# Create match-case example(Python 3.10+)

today = "Sunday"

match today:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("I will go to college")
    case "Saturday":
        print("I will do homework")
    case "Sunday":
        print("I will be on vacation")
    case _:
        print("Invalid day")
```

Pattern matching can also be used to match more complex data structures:

```python
# Match with data structure
def process_command(command):
    match command.split():
        case ["quit"]:
            print("Exit program")
        case ["hello", name]:
            print(f"Hello, {name}!")
        case ["add", x, y]:
            print(f"Result: {int(x) + int(y)}")
        case _:
            print("Unknown command")

process_command("hello Bob")  # Output: Hello, Bob!
process_command("add 5 3")  # Output: Result: 8
```

### Ternary Operator (One Line Condition)

Python also supports writing conditions in one line called ternary operator or conditional expression:

```python
# Ternary operator
age = 20
status = "Adult" if age >= 18 else "Child"
print(status)  # Output: Adult

# Another example
score = 85
result = "Pass" if score >= 60 else "Fail"
print(result)  # Output: Pass
```
