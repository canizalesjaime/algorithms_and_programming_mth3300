# Lecture Notes

## table of contents
1. Classes in Python
2. In Class Assignments 

## Classes in Python

A **class** is a **blueprint** for creating objects. It combines **data (attributes)** and **behavior (methods)** in one place.

---

### 1. Attributes
- Variables that store data for an object
- Example: position, color, speed

### 2. Methods
- Functions that define behavior for an object
- Example: move, print, calculate distance

### 3. `self`
- Refers to the **current object**
- Needed to access the object’s attributes and methods

---

### Basic Class Structure
```python
class Dog:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age    # attribute

    def bark(self):
        print(f"{self.name} says woof!")

### Create objects (instances)

dog1 = Dog("Buddy", 3)
dog2 = Dog("Bella", 5)

dog1.bark()  # Buddy says woof!
dog2.bark()  # Bella says woof!
```
---

### Special Method: `__init__`
- Runs automatically when an object is created
- Initializes attributes
```python
def __init__(self, name, age):
    self.name = name
    self.age = age
```
---

### Example: Point3D Class

We can model a 3D point with `x`, `y`, `z` coordinates:
```python
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def move(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz

    def display(self):
        print(f"Point at ({self.x}, {self.y}, {self.z})")

### Using the Point3D class

p1 = Point3D(1, 2, 3)
p1.display()      # Point at (1, 2, 3)

p1.move(5, -1, 2)
p1.display()      # Point at (6, 1, 5)


p2 = Point3D(2,2,2)
p1.display() #(6,1,5)
p2.display() #(2,2,2)
```
---

### Analogy

| Concept | Real Life Example |
|---------|-----------------|
| Class | Blueprint of a car |
| Object | Actual car |
| Attribute | Color, size |
| Method | Drive, brake, honk |


## In Class Assignments
### 1.
Consider the points class, add the following two methods:
* A method for scaling the point. For example, consider p3 = (2,3,4),
      if you call the method p3.scale(3), p3 should then be (6,9,12).
* Another method for computing the magnitude of the point, use pythagoreas thereom.

### 2. 
Write a Python class called ComplexNumber that represents a complex number of the form a + bi, where a is the real part and b is the imaginary part. Your class should have the following features:

1. Attributes  
   - real → stores the real part a.  
   - imag → stores the imaginary part b.

2. Methods  
   - __init__(self, real, imag) → initialize the real and imaginary parts.  
   - display(self) → print the complex number in the format "a + bi" (or "a - bi" if the imaginary part is negative).  
   - add(self, other) → return a new ComplexNumber that is the sum of self and other.  
   - multiply(self, other) → return a new ComplexNumber that is the product of self and other.  
   - magnitude(self) → return the magnitude (absolute value) of the complex number, sqrt(a^2 + b^2).

Example Usage:

c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, -2)

c1.display()           # 3 + 4i
c2.display()           # 1 - 2i

c3 = c1.add(c2)
c3.display()           # 4 + 2i

c4 = c1.multiply(c2)
c4.display()           # 11 - 2i

print(c1.magnitude())  # 5.0