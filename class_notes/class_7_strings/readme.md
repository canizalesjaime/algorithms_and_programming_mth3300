# Lecture Notes

## table of contents
1. Strings
2. String Comparison 
3. Split
4. In Class Assignments 

## Strings
A **string in Python** is a sequence of characters used to represent text. It’s one of the most commonly used data types.

---

### Creating Strings
You can define strings using single, double, or triple quotes:

```python
s1 = 'hello'
s2 = "world"
s3 = """this is
a multi-line string"""
```

All of these are of type `str`.

---

### Basic Properties
- Strings are **immutable** → you cannot change individual characters
- Indexed starting at **0**
- Can contain letters, numbers, symbols, spaces

```python
s = "python"

print(s[0])  # 'p'
print(s[-1]) # 'n'
```

---

### Common Operations

### 1. Concatenation (joining)
```python
a = "hello"
b = "world"
print(a + " " + b)  # "hello world"
```

### 2. Repetition
```python
print("ha" * 3)  # "hahaha"
```

### 3. Length
```python
len("python")  # 6
```

---

### 4. Slicing 
Extract parts of a string:

```python
s = "python"

print(s[0:3])  # "pyt"
print(s[2:])   # "thon"
print(s[:4])   # "pyth"
print(s[::-1]) # "nohtyp" (reverse)
```

Format:
```
[start : end : step]
```

---

### String Methods
Python provides many built-in methods(What do they do ?):

```python
s = "  Hello World  "

s.lower()      # "  hello world  "
s.upper()      # "  HELLO WORLD  "
s.strip()      # "Hello World"
s.replace("World", "Python")  # "  Hello Python  "
s.split()      # ["Hello", "World"]
```

---

### Immutability 
Immutability means you can't change the state of the object, but you can changbe the object itself

```python
s = "hello"
s[0] = "H"   # ERROR
```

Instead, you must create a new string:

```python
s = "H" + s[1:]  # "Hello"
```

---


### f-strings (modern formatting)
Allow you to use varaibles inside a string, with the {} operator
```python
name = "Jane"
age = 25

print(f"My name is {name} and I am {age}")
```

---

### Escape characters
Escape characters in Python are special sequences that start with a backslash `\` and represent characters that are hard to type directly or have special meaning.


#### Common escape characters

```python
\'   # Single quote
\"   # Double quote
\\   # Backslash
```

---

#### Whitespace / control characters

```python
\n   # New line
\t   # Tab (horizontal tab)
\r   # Carriage return
\b   # Backspace
\f   # Form feed
\v   # Vertical tab
```


---

#### Example usage

```python
print("Hello\nWorld")
# Hello
# World

print("Column1\tColumn2")
# Column1    Column2

print("He said \"Hello\"")
# He said "Hello"
```

---

#### Raw strings (important)

```python
print(r"C:\new\folder")
# C:\new\folder
```

👉 `r""` tells Python:
> “Do NOT interpret escape characters”

---

# 🔹 Common mistakes

### Forgetting to escape backslashes
```python
"C:\new\test"   #  \n and \t are interpreted
```

**Fix:**
```python
"C:\\new\\test"
# or
r"C:\new\test"
```

## String Comparison
String comparison in Python is how you check if strings are equal, different, or ordered relative to each other.

---

### Basic comparisons

```python
"a" == "a"   # True
"a" == "b"   # False
"a" != "b"   # True
```

`==` checks if contents are the same <br> 
`!=` checks if they are different  

---

### Lexicographical (alphabetical) comparison

Python compares strings **character by character using ASCII/Unicode values**.

```python
"apple" < "banana"   # True
"cat" > "car"        # True
```

Comparison happens left to right:
- Compare first different character
- Decide based on that

Example:
```python
"cat" vs "car"
# 'c' == 'c'
# 'a' == 'a'
# 't' > 'r' → result is True
```

---

### ASCII / Unicode matters

```python
"A" < "a"   # True
```

👉 Because:
- `'A'` = 65
- `'a'` = 97

So uppercase letters come **before** lowercase.

---

#### Comparing different lengths

```python
"app" < "apple"   # True
```

👉 If one string is a prefix of another, the shorter one is smaller.

---

#### Case sensitivity

```python
"hello" == "Hello"   # False
```

Comparisons are **case-sensitive**

To ignore case:
```python
"hello".lower() == "Hello".lower()   # True
```

---

#### Using `ord()` to understand comparisons

```python
ord("a")  # 97
ord("b")  # 98
```
Helps explain why comparisons behave the way they do.

---

#### Comparing multiple strings

```python
"a" < "b" < "c"   # True
```

Python supports chaining comparisons.

---

### Membership comparison

```python
"app" in "apple"     # True
"z" in "apple"       # False
```

This checks **substring presence**, not ordering.

---

#### Identity vs equality (important distinction)

```python
a = "hello"
b = "hello"

a == b   # True  (same content)
a is b   # True or False (same object in memory?)
```

`==` → compares values<br>  
`is` → compares memory identity  


## Split
`split()` breaks a string into a **list of substrings** based on a separator.

```python
text = "a,b,c"
result = text.split(",")
# ['a', 'b', 'c']
```

---

### Default behavior
If you **don’t pass anything**, Python splits on **whitespace** (spaces, tabs, newlines) — *and it collapses multiple spaces*.

```python
text = "  hello   world  "
print(text.split())
# ['hello', 'world']
```

Notice:
- Leading/trailing spaces are ignored
- Multiple spaces act like one separator

---

### Using a custom separator
You can specify exactly what to split on:

```python
text = "apple|banana|cherry"
print(text.split("|"))
# ['apple', 'banana', 'cherry']
```

---

### Important difference: `" "` vs default

```python
text = "  hello   world  "

print(text.split())     # ['hello', 'world']
print(text.split(" "))  # ['', '', 'hello', '', '', 'world', '', '']
```

Why?
- `" "` means *split exactly on one space*
- default means *split on ANY whitespace and clean it up*

---

### maxsplit parameter
You can limit how many splits happen:

```python
text = "a,b,c,d"

print(text.split(",", 1))
# ['a', 'b,c,d']

print(text.split(",", 2))
# ['a', 'b', 'c,d']
```

After `maxsplit` splits, the rest stays as one piece.

---

### Splitting lines
Very common use case:

```python
text = "line1\nline2\nline3"
print(text.split("\n"))
# ['line1', 'line2', 'line3']
```

Better alternative:

```python
text.splitlines()
```

---

### When separator is not found

```python
text = "hello world"
print(text.split(","))
# ['hello world']
```

You just get the original string as a single element.

---

### Empty string behavior

```python
"".split(",")   # ['']
"".split()      # []
```

Subtle but important difference.

---

### Use Cases
#### Parse CSV-like data
```python
data = "John,25,Engineer"
name, age, job = data.split(",")
```

---

#### Extract words
```python
sentence = "Python is awesome"
words = sentence.split()
```

---

#### File parsing
```python
line = "ERROR 404 PageNotFound"
parts = line.split(" ", 2)
```

## Find method
The `find()` method in Python is used to **search for a substring inside a string** and return its position.

---

### Basic idea

```python
text = "hello world"
text.find("world")
# 6
```

It returns the **index of the first occurrence** of the substring.

---

### Syntax

```python
string.find(substring, start, end)
```

- `substring` → what you’re searching for
- `start` (optional) → where to begin searching
- `end` (optional) → where to stop searching

---

### Return value (very important)

```python
text = "hello"

text.find("e")   # 1
text.find("z")   # -1
```

If not found → returns **-1** (NOT an error)

---

### Searching with start and end

```python
text = "banana"

text.find("a", 2)      # 3
text.find("a", 2, 4)   # 3
text.find("a", 4)      # 5
```

Only searches within that slice of the string.

---

### First occurrence only

```python
text = "banana"
text.find("a")   # 1
```

Even though there are multiple `'a'`, it returns the **first one**.

---

### Finding multiple occurrences

```python
text = "banana"
index = text.find("a")

while index != -1:
    print(index)
    index = text.find("a", index + 1)
```

Keeps searching from the next position.

---

### Case sensitivity

```python
"Hello".find("h")   # -1
```

`find()` is **case-sensitive**

Fix:
```python
"Hello".lower().find("h")  # 0
```

---


### Extract part of a string
```python
email = "user@gmail.com"
at_index = email.find("@")

username = email[:at_index]
```

---

### Parse data
```python
line = "key=value"
pos = line.find("=")

key = line[:pos]
value = line[pos+1:]
```



## In Class Assignments
###
Given:
```python
s = "python"
```
What is the output of:
```python
print(s[1:4])
```

---

###
What is the difference in output between:
```python
text = "  hello   world  "

print(text.split())
print(text.split(" "))
```
Explain why they are different.

---

###
Write a Python expression using `.split()` and indexing to extract the word `"world"` from:
```python
text = "hello world python"
```

---

###
What will this code output and why?
```python
print("Apple" < "apple")
```

---

###
Given:
```python
text = "banana"
```
What does the following return?
```python
text.find("a", 2)
```
Explain how the result is determined.

