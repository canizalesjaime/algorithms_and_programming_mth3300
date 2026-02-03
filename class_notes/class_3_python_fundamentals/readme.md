# Lecture Notes

## table of contents
1. Type Converter Functions
2. Order of Operations (PEMDAS + Logic)
3. Modulus Operator (%)
4. Binary Numbers
5. Function Composition - Circle Area
6. In class assignments

## Type Converter Functions
These functions transform data from one type to another. Common ones include:
- `int()` - converts to integer (whole numbers)
- `float()` - converts to decimal numbers
- `str()` - converts to text/string
- `bool()` - converts to True/False

Example: `int("42")` turns the text "42" into the number 42

## Order of Operations (PEMDAS + Logic)
Programming follows mathematical order, **plus** rules for comparison and logical operators:

1. **P**arentheses first
2. **E**xponents (powers)
3. **M**ultiplication and **D**ivision (left to right)
4. **A**ddition and **S**ubtraction (left to right)
5. **Comparison operators** (`<`, `>`, `<=`, `>=`, `==`, `!=`)
6. **not** (logical NOT)
7. **and** (logical AND)
8. **or** (logical OR)

**Example:**
```python
5 + 3 > 7 and not False or 2 < 1
```
This evaluates as:
- First: `5 + 3` → 8
- Then: `8 > 7` → True
- Then: `not False` → True
- Then: `True and True` → True
- Finally: `True or False` → True

**Pro tip:** When in doubt, use parentheses to make your logic crystal clear! `(5 + 3 > 7) and (not False)` is much easier to read.

## String Concatenation with +
The `+` operator joins strings together:
```python
"Hello" + " " + "World"  # Results in "Hello World"
```

## Modulus Operator (%)
Returns the **remainder** after division. Think of it as "what's left over" after dividing.

**How it works:**
- `10 % 3` equals 1 (because 10 ÷ 3 = 3 remainder 1)
  - 3 goes into 10 three times (3 × 3 = 9)
  - 10 - 9 = 1 left over
- `15 % 4` equals 3
  - 4 goes into 15 three times (4 × 3 = 12)
  - 15 - 12 = 3 left over
- `7 % 7` equals 0 (divides evenly, no remainder)
- `5 % 10` equals 5 (10 doesn't go into 5 at all, so 5 is left over)

**Common use cases:**
- **Check if a number is even or odd:**
  - `x % 2 == 0` means x is even
  - `x % 2 == 1` means x is odd
- **Check if a number is divisible by another:**
  - `x % 5 == 0` means x is divisible by 5
- **Wrap around values (like a clock):**
  - Hour 15 on a 12-hour clock: `15 % 12 = 3` (3 o'clock)
- **Get the last digit of a number:**
  - `1234 % 10 = 4`
- **Cycle through a list:**
  - If you have 5 items and an index of 7: `7 % 5 = 2` (wraps back to index 2)

## Binary Numbers
Binary numbers are important because they are the language all our computers use. Knowing what they are will help us better understand exactly how computers work. <br><br>
Binary uses only 0s and 1s (base-2). Each position represents a power of 2.

**Converting decimal to binary (Algorithm):**
To convert a decimal number to binary, repeatedly divide by 2 and track the remainders:

1. Divide the number by 2
2. Record the remainder (0 or 1)
3. Use the quotient for the next division
4. Repeat until the quotient is 0
5. Read the remainders from bottom to top

Example: Convert 13 to binary
- 13 ÷ 2 = 6 remainder **1**
- 6 ÷ 2 = 3 remainder **0**
- 3 ÷ 2 = 1 remainder **1**
- 1 ÷ 2 = 0 remainder **1**
- Reading bottom to top: **1101**

Verification: (1×2³) + (1×2²) + (0×2¹) + (1×2⁰) = 8 + 4 + 0 + 1 = 13 ✓

**Converting binary to decimal (Algorithm):**
To convert a binary number to decimal, multiply each digit by its position's power of 2:

1. Start from the rightmost digit (position 0)
2. Multiply each digit by 2 raised to its position
3. Add all the results together

Example: Convert 1010 to decimal
- Position 3: 1 × 2³ = 1 × 8 = 8
- Position 2: 0 × 2² = 0 × 4 = 0
- Position 1: 1 × 2¹ = 1 × 2 = 2
- Position 0: 0 × 2⁰ = 0 × 1 = 0
- Sum: 8 + 0 + 2 + 0 = **10**

## Function Composition - Circle Area
**Step-by-step approach:**
```python
import math

radius = 5
area = math.pi * radius ** 2
print(area)
```

**One-line version (composition):**
```python
print(math.pi * 5 ** 2)
```


The idea of composition is nesting operations together instead of storing intermediate values. You're "composing" multiple operations into a single expression!


## in class assigments
1. Take the sentence: The quick brown fox jumps over the lazy dog. Store each word in a separate variable, then print out the sentence on one line using print.

2. Add parentheses to the expression 8 + 2 * 3 - 4 to change its value from 10 to 26.

3. Start the Python interpreter and enter temperature + 32 at the prompt. This will give you an error:

   NameError: name 'temperature' is not defined

   Assign a value to temperature so that temperature + 32 evaluates to 100.

4. The formula for converting Celsius to Fahrenheit is: F = (9/5) * C + 32
   Write a Python program that assigns a temperature in Celsius to variable C (use 25 as the starting value). Then have the program prompt the user for a different Celsius temperature. Calculate and print the Fahrenheit equivalent for the user's input.

5. Evaluate the following numerical expressions in your head, then use the Python interpreter to check your results:
   1. >>> 8 % 3
   2. >>> 17 % 5
   3. >>> 20 % 4
   4. >>> 7 % 10
   5. >>> 9 % 9
   6. >>> 5 % 1
   
   What pattern do you notice? When is the result 0? When is the result equal to the first number? Make up 3 more examples to test your understanding.

6. You start reading a book on page 47. If the book has 203 pages total, how many pages do you have left to read? Now solve this: if you're on page P in a book with T total pages, write the expression to calculate pages remaining.

7. Write a Python program to calculate someone's age in days. Ask the user for their age in years, then calculate and print approximately how many days old they are. (Assume 365 days per year for simplicity. Bonus: account for leap years!)