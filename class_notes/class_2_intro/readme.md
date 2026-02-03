# Lecture Notes

## table of contents
1. What is a program, a computer and an algorithm
2. How Programs Use CPU, RAM, and Hard Drive
3. Variables, expressions and statements


## What is a program, a computer and an algorithm ? 
### Computer
A computer is an electronic system made up of hardware and software that accepts input, processes data, stores information, and produces output according to instructions.
At its core:

* CPU (Central Processing Unit): the “brain” of the computer that executes instructions, performs calculations, and controls all operations.
* RAM (Random Access Memory): short-term, fast memory that temporarily holds programs and data currently in use by the CPU.
* Hard Drive (HDD/SSD): long-term storage that permanently stores the operating system, programs, and files even when the computer is powered off.

Together, these components allow a computer to run programs, follow algorithms, and deliver results to the user.

### Program
A program is a set of instructions written in a programming language that tells a computer what to do and how to do it.

### Algorithm
An algorithm is a step-by-step logical procedure for solving a problem, independent of any programming language.

How they connect:
* An algorithm is the idea or logic.
* A program is the implementation of that idea in code.
* A computer is the machine that executes the program.


## How Programs Use CPU, RAM, and Hard Drive

### Hard Drive (Permanent Storage)
- Stores:
  - Python programs (.py files)
  - The Python interpreter
  - Data files(files, images, videos, etc)
- Nothing executes directly from the hard drive

---

### RAM (Working Memory)
- When you run a Python program:
  - The program is loaded from the hard drive into RAM
  - Variables and intermediate results live here
- RAM is fast but temporary (cleared when the program ends)

---

### CPU (Execution)
- The CPU executes instructions one by one:
  - Reads code and data from RAM
  - Evaluates expressions
  - Executes statements
- The CPU does all calculations and decision-making

---

## 3. Input and Output Devices

### Keyboard and Mouse (Input)
- Provide data to the program from the user 
- Input is passed through the operating system to the program in RAM

user_input = input("Enter a number: ")

---

### Display (Output)
- Shows results produced by the program

print("Result:", x)

- Output is sent from the CPU to the display

---

## 4. Putting It All Together

x = 5 + 3<br>
print(x)

What happens:
1. Program is loaded from hard drive → RAM
2. CPU evaluates 5 + 3 (expression)
3. Result 8 is stored in RAM as variable x
4. print(x) sends output to the display

---

## Key Idea
Programming is telling the CPU how to process data in RAM, using instructions that are stored on the hard drive, while interacting with users through input and output devices.


## Variables, expressions and statements

### Variables
A variable is a name that refers to a value stored in memory (RAM).

x = 10<br>
name = "Albert"

- x and name are variables
- The values they refer to are stored in RAM while the program runs
- Python uses dynamic typing (the type comes from the value)
- Variable names can be arbitrarily long. They can contain both letters, digits, and underscores.
- Note, there are certain words considered **keywords**(if, and, or for, while, class, etc). Which can not be used as variable names. Python interpretor will complain and forbid if you try to use these.

Common data types:
- int → 10
- float → 3.14
- str → "hello"
- bool → True, False

---

### Expressions
An expression is code that evaluates to a value.

x + 5<br>
len(name)<br>
x > 5

- Expressions are evaluated by the CPU
- The result is temporarily stored in RAM

---

### Statements
A statement is a complete instruction that performs an action.

x = 10
print(x)

- Assignment statements store values in RAM
- Output statements send results to the display
- Control statements (if, while, for) guide execution flow

---


## In class assignments
1. Make sure all the software mentioned from last class is installed on your computer
2. Write a python program that creates a variable x, and another variable y. Set x equal to 2.718 and y equal to 3.14. Have the user enter an integer value for another variable z, 
then print to the display the result of x squared plus four times y minus z.  