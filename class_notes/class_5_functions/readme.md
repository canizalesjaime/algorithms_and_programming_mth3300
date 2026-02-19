# Lecture Notes

## table of contents
1. Functions
2. Truth Tables
3. In Class Assignments


## Functions
A **function** in Python is a reusable block of code that performs a specific task. Instead of rewriting the same logic multiple times, you define it once and call it whenever you need.

---

### Why functions are useful

- **Reuse code** → write once, use many times  
- **Organize programs** → break big problems into smaller pieces  
- **Improve readability** → easier to understand and debug  

---

### Basic syntax

```python
def function_name(parameters):
    # code to run
    return value  # optional
```

### Example

```python
def greet(name):
    print("Hello", name)

greet("James")
```

**What happens**

1. `def` defines the function  
2. `name` is a parameter (input)  
3. Calling `greet("James")` runs the code  

---

### Parameters vs Arguments

- **Parameter** → variable in the function definition  
- **Argument** → actual value you pass in  

```python
def add(a, b):   # a and b are parameters
    return a + b

result = add(2, 3)  # 2 and 3 are arguments
```

---

### Return values

Functions can send data back using `return`.

```python
def square(x):
    return x * x

print(square(4))  # 16
```

If there’s no `return`, Python returns `None`.

---

### Types of functions

### No parameters

```python
def say_hi():
    print("Hi")
```

### Multiple parameters

```python
def power(base, exp):
    return base ** exp
```

### Default parameters

```python
def greet(name="friend"):
    print("Hello", name)

greet()        # Hello friend
greet("Alex")  # Hello Alex
```

### Keyword arguments

```python
def describe(name, age):
    print(name, age)

describe(age=25, name="Sam")
```

---

## Functions as building blocks

You can call functions inside other functions.

```python
def area_circle(r):
    return 3.14 * r * r

def print_area(r):
    print("Area:", area_circle(r))
```

## Scope (important concept)

Variables created inside a function are **local**.

```python
def test():
    x = 10

test()
# x is not accessible here
```

Global variables exist outside functions but should be used sparingly.

### Python built-in math helpers

These are very common built-in functions you’ll see in everyday code.

---

### `abs()` — absolute value

Returns the **distance from zero** (always non-negative).

```python
abs(-5)   # 5
abs(3.2)  # 3.2
```

Useful for:
- Distances  
- Error magnitudes  
- Comparing differences  

---

### `max()` — largest value

Returns the biggest item from arguments or an iterable.

```python
max(3, 7, 2)        # 7
max([1, 9, 4])      # 9
```

You can also use a key function:

```python
max(["cat", "elephant", "dog"], key=len)  # "elephant"
```

---

### `min()` — smallest value

Opposite of `max()` — returns the smallest item.

```python
min(3, 7, 2)        # 2
min([1, 9, 4])      # 1
```

---

### `pow()` — exponentiation

Raises a number to a power.

```python
pow(2, 3)   # 8
```

With modulus:

```
pow(base, exp, mod)
```

Computes:
```
(base ** exp) % mod
```

Example:

```python
pow(2, 5, 3)  # 2
```

Used in:
- Cryptography  
- Modular arithmetic  
- Efficient large exponent calculations  

---

### Quick comparison

| Function | Purpose | Example | Result |
|---|---|---|---|
| `abs(x)` | Distance from zero | `abs(-4)` | `4` |
| `max()` | Largest value | `max(1,5,2)` | `5` |
| `min()` | Smallest value | `min(1,5,2)` | `1` |
| `pow(a,b)` | Exponent | `pow(2,3)` | `8` |


## Truth Tables

A **truth table** is a table used in logic (and computer science) to show **all possible combinations of inputs** and the **resulting output** of a logical expression.  

It’s basically a systematic way to answer:  
*“What does this statement evaluate to for every possible case?”*

In Python, truth tables correspond to boolean expressions:

```python
A and B
A or B
not A
```

They help you reason about:
- `if` statements  
- complex conditions  
- debugging logic  

---

### Why truth tables matter

- Help understand logical expressions  
- Used in **digital circuits** (AND, OR, NOT gates)  
- Important in **programming conditions**  
- Used in **mathematical logic proofs**  

---

### Basic logical values

| Symbol | Meaning | Programming equivalent | 
|---|---|---| 
| **T** | True | `True` | 
| **F** | False | `False` | 

---

### Common logical operators

### NOT (¬ or !)
Negates a value.

| A | NOT A |  
|---|---|  
| T | F |  
| F | T |  

---

### AND (∧ or &&)
True only if **both** are true.

| A | B | A AND B |  
|---|---|---| 
| T | T | T | 
| T | F | F | 
| F | T | F | 
| F | F | F | 

---

### OR (∨ or \|\|)
True if **at least one** is true.

| A | B | A OR B | 
|---|---|---| 
| T | T | T | 
| T | F | T | 
| F | T | T | 
| F | F | F | 

---

### XOR (exclusive OR)
True if **exactly one** is true.

| A | B | A XOR B | 
|---|---|---| 
| T | T | F | 
| T | F | T | 
| F | T | T | 
| F | F | F | 

---

### How to build a truth table (step-by-step)

Example expression:

```
(A AND B) OR NOT A
```

### List all input combinations  
For **n variables → 2ⁿ rows**

| A | B | 
|---|---| 
| T | T | 
| T | F | 
| F | T | 
| F | F | 

### Add intermediate columns  

| A | B | A AND B | NOT A | Final |
|---|---|---|---|---|
| T | T | T | F | T |
| T | F | F | F | F |
| F | T | F | T | T |
| F | F | F | T | T |


## In class Assignments
### 1
Write a Python function `can_vote(age, citizen)` that returns `True` if a person is eligible to vote. A person can vote if their age is 18 or older and they are a citizen. Test the function with different values for age and citizenship.

### 2
Write a function `is_even(n)` that returns `True` if a number is even and `False` otherwise. Test the function for numbers from 1 to 10.

### 3
Given a set of numbers such as 3, -7, 0, 5, and -2, find the maximum value, the minimum value, and the absolute value of each number.

### 4
Write a function `powers_list(base, n)` that returns the first n powers of a given base using `pow()`. For example, if the base is 2 and n is 5, the output should be 2, 4, 8, 16, and 32.

### 5
Construct a truth table for the expression `(A OR B) AND (NOT B)`. Include columns for A, B, A OR B, NOT B, and the final result, using `True` and `False` values.
