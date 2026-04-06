# Lecture Notes

## table of contents
1. Join
2. Files
3. In Class Assignments 



## Join
`join()` takes a **list (or iterable) of strings** and combines them into a single string, using a separator(`join()` is the *opposite* of `split()`).

```python
words = ["a", "b", "c"]
result = ",".join(words)
# "a,b,c"
```

Think of it as:
> “Put this string **between every element**”

---

### Basic syntax

```python
separator.join(iterable_of_strings)
```

- `separator` → what goes between elements
- iterable → list, tuple, etc. (must contain strings)

---

### Join with spaces(Example)
```python
words = ["hello", "world"]
print(" ".join(words))
# "hello world"
```

---

### Join with commas(Example)
```python
items = ["apple", "banana", "cherry"]
print(", ".join(items))
# "apple, banana, cherry"
```

---

### Join with no separator(Example)
```python
chars = ["P", "y", "t", "h", "o", "n"]
print("".join(chars))
# "Python"
```

---

### Important: elements must be strings

```python
nums = [1, 2, 3]
",".join(nums)   # ERROR
```

Fix:
```python
",".join(str(n) for n in nums)
# "1,2,3"
```

---

### Join works on any iterable

```python
print("-".join(("a", "b", "c")))
# "a-b-c"

print("".join({"x", "y", "z"}))  # order not guaranteed
```

---


### Convert list → sentence(Common patterns)
```python
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
```

---

### Build CSV line(Common patterns)
```python
data = ["John", "25", "Engineer"]
csv_line = ",".join(data)
```

---

### Efficient string building
```python
chars = []
for c in "hello":
    chars.append(c.upper())

result = "".join(chars)
```

This is faster than repeatedly doing:
```python
result += c
```

---

### Empty iterable behavior

```python
",".join([])   # ""
```

Returns an empty string, not an error.

---

### Single element

```python
",".join(["hello"])
# "hello"
```

No separator added.

---


### Putting separator in wrong place(Common mistakes)
```python
join(",", ["a", "b"])  # WRONG
```

Correct:
```python
",".join(["a", "b"])
```

---

### Mixing types(Common mistakes)
```python
["a", 1, "b"]  # join will fail
```

---

### Mental model (this helps a lot)
Think of `join()` as:

> “Glue these pieces together, using this string as the glue”

- `" ".join(...)` → glue with spaces  
- `",".join(...)` → glue with commas  
- `"".join(...)` → glue with nothing  

---

### Relationship with `split()`

```python
text = "a,b,c"

parts = text.split(",")
rejoined = ",".join(parts)

# rejoined == "a,b,c"
```


## Files
In Python, you don’t explicitly “create” a file first—opening a file in write mode creates it automatically.

### Basic example:
```python
    file = open("example.txt", "w")
    file.write("Hello, world!")
    file.close()
```
Key points:

- "w" = write mode  
- If file doesn’t exist → it is created  
- If file exists → it is overwritten  

---

### Safer option (recommended): with
```python
    with open("example.txt", "w") as file:
        file.write("Hello, world!")
```
- Automatically closes the file  
- Cleaner and safer  

---

### Opening Files

Python uses different modes depending on what you want to do:

| Mode | Meaning |
|------|--------|
| "r"  | Read (default) |
| "w"  | Write (overwrite) |
| "a"  | Append (add to end) |
| "x"  | Create (fails if exists) |

---

### Read example:
```python
with open("example.txt", "r") as file:
    content = file.read() # read method puts the whole file into a string
    print(content)
```

---

### Read line-by-line:
```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
```
---

### Read into a list:
```python
with open("example.txt", "r") as file:
    lines = file.readlines()
```
---

### Parsing Files (Extracting Data)

Parsing = reading structured data and turning it into usable variables

---

#### Example 1: Parsing a CSV (manual way)

**File (data.txt):**
```
    Alice,25
    Bob,30
    Charlie,22
```
**Code:**
```python
    with open("data.txt", "r") as file:
        for line in file:
            name, age = line.strip().split(",")
            age = int(age)
            print(name, age)
```
What’s happening:

- strip() removes newline \n  
- split(",") separates values  
- Converts string to int  

---

### Example 2: Parsing key-value data

**File:**
```
    x=10
    y=20
    z=30
```
**Code:**
```python
    data = {}

    with open("config.txt", "r") as file:
        for line in file:
            key, value = line.strip().split("=")
            data[key] = int(value)

    print(data)
```
---


### Example 3: Parsing numbers into a list

**File:**
```
    10 20 30 40
```
**Code:**
```python
    with open("numbers.txt", "r") as file:
        numbers = list(map(int, file.read().split()))

    print(numbers)
```
---


### Example 4: Appending to an existing file
**File:**
```
    Line 1
    Line 2
```

**Code:**
```python 
with open("example.txt", "a") as file:
    # Append new lines at the end
    file.write("Appended Line 3\n")
    file.write("Appended Line 4\n")

# Step 3: Read file normally to verify (using "r")
with open("example.txt", "r") as file:
    final_content = file.read()

print(final_content)
```

---

### Common Mistakes

1. Forgetting to close file
```python
        file = open("test.txt")
        # forgot file.close()
```
2. Not stripping newline
```python
        line = "Alice,25\n"
        line.split(",")  # gives ['Alice', '25\n']
```
   Fix:
```python
        line.strip().split(",")
```
3. Wrong mode
```python
        open("file.txt", "r")  # crashes if file doesn't exist
```
---


## In Class Assignments
### 1
What does the `join()` method do in Python, and how is it related to `split()`?

---

### 2
What is wrong with the following code, and how would you fix it?

```python
nums = [1, 2, 3]
result = ",".join(nums)
```

---

### 3
What is the output of this code?

```python
words = ["Python", "is", "awesome"]
print("-".join(words))
```

---

### 4 
What happens when you open a file using mode `"w"` in Python if:
- the file does not exist?
- the file already exists?

---

### 5
Given a file containing:

```
John,25
Jane,30
```

Write a short Python snippet to read the file and print:

```
John is 25 years old
Jane is 30 years old
```

### 6
Building on the previous question, modify your Python code so that it adds 3 to each person’s age before printing.
* Do not edit the file manually.
* Use a sequence of reads and writes in your script to update the ages.