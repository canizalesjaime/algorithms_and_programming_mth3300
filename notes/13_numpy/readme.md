# Lecture Notes

## table of contents
1. Numpy
2. In Class Assignments 


## Numpy

Regular Python lists are flexible, but slow for heavy numerical computations.

NumPy stores numbers in compact memory blocks and performs operations using optimized C code internally, making it much faster.

Example:

```python
# Python list
a = [1, 2, 3]
b = [4, 5, 6]

# This does NOT do element-wise addition
print(a + b)
# [1, 2, 3, 4, 5, 6]
```

With NumPy:

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
# [5 7 9]
```

---

### Core Concept: ndarray

The main object in NumPy is the **ndarray** (N-dimensional array).

You can think of it as:
- 1D → vector
- 2D → matrix/table
- 3D+ → tensors

Example:

```python
import numpy as np

arr = np.array([1, 2, 3])
print(arr)
```

2D example:

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix)
```

---

### Array Properties(attributes)

```python
print(matrix.shape)   # dimensions
print(matrix.ndim)    # number of dimensions
print(matrix.size)    # total elements
print(matrix.dtype)   # data type
```

For:

```python
[[1,2,3],
 [4,5,6]]
```

- shape = `(2,3)`
- ndim = `2`
- size = `6`

---

### Fast Mathematical Operations

NumPy performs operations element-wise.

```python
a = np.array([1,2,3])

print(a * 2)
# [2 4 6]

print(a ** 2)
# [1 4 9]
```

---

### Broadcasting

One of NumPy’s most powerful features.

It allows operations between arrays of different sizes when dimensions are compatible.

```python
matrix = np.array([
    [1,2,3],
    [4,5,6]
])

print(matrix + 10)
```

Result:

```python
[[11 12 13]
 [14 15 16]]
```

NumPy “broadcasts” the scalar across the matrix.

---

### Indexing and Slicing

Similar to Python lists 

```python
a = np.array([10,20,30,40])

print(a[1])      # 20
print(a[1:3])    # [20 30]
```

2D indexing:

```python
matrix[2,1]
```

means:
- row 2
- column 1

---

### Useful Array Creation Functions

```python
np.zeros((2,3))
```

Creates:

```python
[[0. 0. 0.]
 [0. 0. 0.]]
```

Other common ones:

```python
np.ones((2,2))
np.eye(3)          # identity matrix
np.arange(0,10,2)
np.linspace(0,1,5)
```


### Matrix Multiplication
Example matrix multiplication:

```python
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print(A @ B)
```

Or:

```python
np.matmul(A,B)
```

**NOTE:**<br>
the \* operator does not do matrix multiplication, it does element wise multiplaication

Example:
```python
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print(A * B) 
```

results in:
```
[
 [1*5, 2*6],
 [3*7, 4*8]
]
 =
[
 [5, 12],
 [21, 32]
]
```

### Statistics

```python
a = np.array([1,2,3,4])

print(np.mean(a))
print(np.std(a))
print(np.min(a))
print(np.max(a))
```

---

### Random Numbers

Useful in simulations and ML.

```python
np.random.rand(3)
np.random.randint(0,10,size=5)
```


### Conclusion
Think of NumPy as:
> “Python’s high-performance matrix and numerical computation system.”

It gives Python capabilities similar to:
- MATLAB
- basic matrix algebra systems
- scientific computing tools

but inside normal Python programs.


## In Class Assignments
### 1. 