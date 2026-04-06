# Lecture Notes

## table of contents
1. Lists
2. Dictionaries
3. Tuples
4. In Class Assignments 

## Lists
A list is an ordered, mutable collection of items. Lists can contain any data type, including mixed types.

### Creating a list
numbers = [1, 2, 3, 4]  
mixed = [1, "hello", 3.5, True]  
empty = []

### Accessing Elements

numbers[0]  
Returns the first element in the list because Python uses zero-based indexing.

numbers[-1]  
Returns the last element. Negative indices count from the end:
-1 is last, -2 is second-to-last, etc.

---

### Common Operations

numbers.append(5)  
Adds the value 5 to the end of the list.  
The list grows by one element.

numbers.insert(1, 10)  
Inserts 10 at index 1.  
Elements at and after index 1 shift right.

numbers.remove(3)  
Removes the first occurrence of the value 3.  
Raises an error if 3 is not in the list.

numbers.pop()  
Removes and returns the last element.  
You can also pass an index: numbers.pop(2).

len(numbers)  
Returns the total number of elements in the list.  
Does not modify the list.

### Slicing
Slicing extracts a subsequence from a sequence (list, string, or tuple).

#### Syntax
sequence[start : stop : step]

- start: where to begin (inclusive)  
- stop: where to end (exclusive)  
- step: how much to move each time  

Key rule: the stop index is NOT included.

#### Basic Example
nums = [10, 20, 30, 40, 50]

nums[1:4] → [20, 30, 40]

#### Omitting Values
nums[:3]  → first three elements  
nums[2:]  → from index 2 to end  
nums[:]   → copy of the sequence  

#### Step
nums[::2] → every second element  
nums[1::2] → start at index 1, step by 2  

#### Negative Indices
nums[-3:] → last three elements  
nums[:-1] → all except the last  

#### Reverse
nums[::-1] → reversed sequence  

#### Works With
- lists  
- strings  
- tuples  


### Difference Between `list2 = list1` and `list2 = list1[:]`

Assume:
list1 = [1, 2, 3]

---

#### list2 = list1

This does NOT create a new list.  
Both variables point to the same list in memory.

list2 = list1
list2[0] = 99

Result:
list1 → [99, 2, 3]  
list2 → [99, 2, 3]

Explanation:
You copied the reference, not the data.  
Any change through one variable affects the other.

Think: two names for the same object.

---

#### list2 = list1[:]

This creates a NEW list with the same elements.

list2 = list1[:]
list2[0] = 99

Result:
list1 → [1, 2, 3]  
list2 → [99, 2, 3]

Explanation:
Slicing copies the elements into a new list,  
so modifying one list does not affect the other.

Think: a new container with the same contents.


#### Key Difference

list2 = list1  
→ same object, changes affect both

list2 = list1[:]  
→ new object, changes are independent


### Common Mistakes
- forgetting stop is exclusive  
- confusing negative indices  
- assuming slicing modifies the original (it returns a new object)

### Iterating
for n in numbers:  
    print(n)


## Dictionaries
A dictionary in Python is a mutable collection of key–value pairs. Each key maps to a specific value, allowing you to retrieve data quickly using the key instead of searching through the entire collection.

Dictionaries are useful for representing structured data where each piece of information has a label. For example, information about a student, configuration settings, or mappings between IDs and objects.

### Key properties of dictionaries

- Keys must be unique — if the same key is used again, the previous value will be overwritten.
- Keys must be immutable types (such as strings, numbers, or tuples).
- Values can be any Python type (numbers, strings, lists, dictionaries, etc.).
- Dictionaries are mutable, meaning they can be modified after creation.

### Creating a dictionary

Dictionaries are created using curly braces {} with key–value pairs separated by colons.

student = {
    "name": "Alex",
    "age": 21,
    "major": "CS"
}

Here:
- "name", "age", and "major" are the keys
- "Alex", 21, and "CS" are the values

### Accessing values

Values are retrieved using their key.

student["name"]
student.get("age")

student["name"] returns the value associated with the key "name".

The get() method is safer when you are unsure if a key exists.

student.get("gpa")

If the key does not exist:
- student["gpa"] would raise an error
- student.get("gpa") returns None

You can also provide a default value:

student.get("gpa", 0.0)

### Adding and updating values

Because dictionaries are mutable, you can add new key–value pairs or update existing ones.

Adding a new key:

student["gpa"] = 3.8

Updating an existing key:

student["age"] = 22

If the key already exists, its value will be replaced.

### Removing elements

Items can be removed using pop() or del.

student.pop("major")

This removes the key "major" and returns its value.

del student["age"]

This deletes the key "age" from the dictionary.

### Iterating through a dictionary

You can loop through the key–value pairs using items().

for key, value in student.items():
    print(key, value)

Example output:

name Alex
age 22
gpa 3.8

Other useful iteration methods:

student.keys()    # iterate over keys
student.values()  # iterate over values


---

## Tuples

A tuple is an ordered, immutable collection of elements. Tuples are similar to lists, but their contents cannot be changed after creation.

Tuples are often used to represent fixed data structures such as coordinates, database records, or function return values.

### Key properties of tuples

- Ordered — elements have a defined position
- Immutable — elements cannot be modified, added, or removed
- Allow duplicate values
- Can contain multiple data types

### Creating tuples

Tuples are created using parentheses ().

point = (3, 4)

This tuple might represent a 2D coordinate.

A single-element tuple must include a comma:

single = (5,)

Without the comma:

single = (5)

Python interprets it as just the integer 5.

An empty tuple:

empty = ()

### Accessing elements

Tuple elements are accessed using indexing.

point[0]
point[-1]

point[0] returns the first element.
point[-1] returns the last element.

### Tuple unpacking

Tuple unpacking allows elements of a tuple to be assigned directly to variables.

x, y = point

Now:
x = 3
y = 4

This is useful when working with structured data.

Example swapping variables:

a, b = 10, 20
a, b = b, a

### Returning multiple values from a function

Python functions can return multiple values by returning a tuple.

def min_max(values):
    return min(values), max(values)

The returned tuple can be unpacked:

low, high = min_max([1, 5, 2])

Results:
low = 1
high = 5


---

## When to Use Each

Use a list when:
- You need an ordered collection that may change
- Items will be added, removed, or modified

Use a dictionary when:
- You need fast lookup by key
- Data has labeled attributes

Use a tuple when:
- The data should remain constant
- The structure represents a fixed record

Summary:

List
- Ordered
- Mutable
- Good for general collections

Dictionary
- Key-based lookup
- Mutable
- Good for structured labeled data

Tuple
- Ordered
- Immutable
- Good for fixed data structures

## In Class Assignments

### Lists
1. Create a list of the numbers 1 through 10 and print the third element.
2. Given a list of numbers, write code to compute the sum of all elements.
3. Write a program that removes all even numbers from a list.
4. Given a list of words, create a new list containing the length of each word.
5. Write a function that returns the largest value in a list without using `max()`.

### Dictionaries (Maps)
1. Create a dictionary representing a book with keys: title, author, and year.
2. Given a dictionary of student scores, print all students who scored above 90.
3. Write code to count how many times each letter appears in a string (frequency map).
4. Given a dictionary, swap its keys and values.
5. Write a function that merges two dictionaries. If a key appears in both, sum their values.

### Tuples
1. Create a tuple with three numbers and print the second element.
2. Write code that swaps two variables using tuple unpacking.
3. Given a list of coordinate tuples `(x, y)`, compute the average x value.
4. Write a function that returns both the minimum and maximum of a list as a tuple.
5. Given a tuple, check whether a value exists inside it.

### Mixed / Conceptual
1. Convert a list of pairs into a dictionary.  
   Example: `[("a", 1), ("b", 2)] → {"a": 1, "b": 2}`

2. Given a list of numbers, return a dictionary where:
   - keys = numbers  
   - values = their squares

3. Given a dictionary of items and prices, return a list of items that cost more than 20.

4. You have a list of tuples representing `(name, score)`.  
   Return the name of the person with the highest score.

5. Explain when you would choose:
   - a list instead of a tuple  
   - a dictionary instead of a list
