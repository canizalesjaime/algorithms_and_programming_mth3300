# Lecture Notes

## table of contents
1. Conditional Statements
2. While Loops
3. For Loops
4. In Class Assignments

## Conditional Statements (Decision Making)

Conditional statements allow a program to make decisions based on conditions.

### Basic if statement

~~~python
x = 10

if x > 5:
    print("x is greater than 5")
~~~

The condition must evaluate to True or False.  
Indentation is required in Python.

### if – else

~~~python
x = 3

if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")
~~~

### if – elif – else

Used when checking multiple conditions.

~~~python
score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Fail")
~~~

### Comparison operators

| Operator | Meaning |
| == | equal to |
| != | not equal |
| > | greater than |
| < | less than |
| >= | greater than or equal to |
| <= | less than or equal to |

### Logical operators

~~~python
age = 20

if age >= 18 and age < 65:
    print("Working age")
~~~

and means both conditions must be true  
or means at least one condition must be true  
not reverses a condition

## While Loops

A while loop repeats as long as a condition remains true.

### Basic while loop

~~~python
count = 1

while count <= 5:
    print(count)
    count += 1
~~~

Output:

1  
2  
3  
4  
5  

If the condition never becomes false, the loop will run forever.

### Using break

~~~python
while True:
    user_input = input("Type 'q' to quit: ")

    if user_input == 'q':
        break
~~~

### Using continue

~~~python
num = 0

while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)
~~~

Output:

1  
2  
4  
5  

## For Loops

A for loop is used to iterate over a sequence such as a list, string, or range.

### Using range()

~~~python
for i in range(5):
    print(i)
~~~

Output:

0  
1  
2  
3  
4  

### range(start, stop, step)

~~~python
for i in range(1, 10, 2):
    print(i)
~~~

Output:

1  
3  
5  
7  
9  

### Looping through a list

~~~python
colors = ["red", "green", "blue"]

for color in colors:
    print(color)
~~~

### Looping through a string

~~~python
for letter in "robot":
    print(letter)
~~~

### For loop vs While loop

| For Loop | While Loop |
| Known number of iterations | Unknown number of iterations |
| Cleaner for sequences | More flexible |
| Lower risk of infinite loops | Higher risk if misused |


## In Class Assigments
Answer the questions and submit to brightspace by end of day 02/13/2026. 

### Question 1: Conditional Statements

Write a program that:
- Takes a number as input
- Prints "Positive" if the number is greater than 0
- Prints "Negative" if the number is less than 0
- Prints "Zero" if the number is 0

### Question 2: While Loop

Write a program that:
- Prints numbers from 1 to 20
- Stops early if the number reaches 13  
Hint: use break

### Question 3: For Loop

Write a program that:
- Loops through a list of numbers
- Prints only the even numbers

Example list:

~~~python
numbers = [3, 8, 12, 7, 5, 10, 6]
~~~



### Question 4:  
- Write a program to code the algorithm for converting a decimal number to a binary numbers.
- Write a program to code the algorithm for converting a hexadecimal number to a decimal number. 

