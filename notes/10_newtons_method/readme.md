# Lecture Notes

## table of contents
1. Newtons Method 
2. In Class Assignments 


## Newtons Method
Newton’s Method is a fast way to find approximate solutions (roots) of an equation like  
f(x) = 0. It is a great example to learn about iterative algorithms, which are a big part of 
computer science. 


### Steps
Start with a guess, then repeatedly improve it using the slope (derivative).

At each step, you:
- Draw the tangent line to the curve at your current guess
- See where that tangent hits the x-axis
- Use that point as your next guess

### The Formula:
$x_{n+1} = x_n - f(x_n)/f'(x_n)$

- $x_n:$ current guess  
- $x_{n+1}:$ next (better) guess  
- $f'(x_n):$ derivative at that point  

### Step-by-step example
Solve:
$f(x) = x^2 - 2 = 0$
(we know the answer is sqrt(2) ≈ 1.414)

* Step 1: Derivative: $f'(x) = 2x$

* Step 2: Pick a starting guess: Let’s try $x_0 = 1$

* Step 3: Iterate
    - Iteration 1: $x_1 = 1 - (1^2 - 2)/(2*1) = 1 + 1/2 = 1.5$
    - Iteration 2: $x_2 = 1.5 - (1.5^2 - 2)/(2*1.5) ≈ 1.4167$
    - Iteration 3: $x_3 ≈ 1.4142$ Already very close to the true value!

### Why it’s powerful
- Converges very fast (quadratic convergence)
- Widely used in:
  - root finding
  - optimization
  - machine learning
  - physics simulations

### When it can fail
Newton’s method is great, but not perfect:
- If $f'(x) = 0$ → division by zero
- Bad starting guess → may diverge
- Can jump to the wrong root
- Doesn’t work well for non-smooth functions


### Choosing a Good Starting Guess for Newton's Method-Strategies
The goal is to pick a point close enough to the root so the tangent line approximation works well.

1. Look for sign changes
- Find two points a and b such that f(a)*f(b) < 0
- This guarantees a root in [a, b] (Intermediate Value Theorem)
- Pick a starting guess inside this interval, often the midpoint: x0 = (a + b)/2

2. Use a graph
- Plot f(x) and see roughly where it crosses the x-axis
- Pick x0 close to the crossing point

3. Avoid flat slopes
- Don’t pick points where f'(x0) ≈ 0
- Flat slope → huge step → likely overshoot

4. Prefer smooth, gentle regions
- Avoid sharp bends, oscillations, or inflection points near the guess

5. Optional: combine with a safe method
- Use bisection or another reliable method to narrow down an interval first
- Then use Newton’s method to converge quickly

### Halting Criteria (When to Stop)
You want to stop when the guess is “good enough.”

1. Change in x is small
|x_{n+1} - x_n| < tolerance (e.g., 1e-6)
- Meaning the guesses aren’t moving much anymore

2. Function value is small
|f(x_{n+1})| < tolerance
- Meaning the current guess is close to zero

3. Maximum iterations
- Prevent infinite loops if the method fails to converge
- Example: stop after 100 iterations

**Recommended practical approach**
- Use both criteria together:
|x_{n+1} - x_n| < tol AND |f(x_{n+1})| < tol
- Ensures the guess is close to the root and the function value is nearly zero


### Code
```python 
def newtons_method(f, df, x0, tol=1e-7, max_iter=100):
    """
    Newton's Method for finding roots of f(x) = 0
    
    Parameters:
    f       : function, f(x)
    df      : function, derivative f'(x)
    x0      : float, initial guess
    tol     : float, tolerance for convergence
    max_iter: int, maximum number of iterations
    
    Returns:
    x       : approximate root
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            print("Derivative is zero. No solution found.")
            return None
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    print("Maximum iterations reached. No solution found.")
    return None

# Example usage: finding sqrt(2)
f = lambda x: x**2 - 2
df = lambda x: 2*x
root = newtons_method(f, df, x0=1.0)
print("Root:", root)
```

## In Class Assignments
### 1. 
Question:  

Use Newton’s Method to approximate a root of the equation:  

$f(x) = x^3 - x - 2 = 0$

Instructions:  
1. Choose an initial guess $x_0 = 1.5$  
2. Perform three iterations of Newton’s Method by hand  
3. Show all your calculations for each iteration  
4. Write the approximate root after the third iteration  

Hint:  
- The derivative is $f'(x) = 3x^2 - 1$
- Newton’s formula: $x_{n+1} = x_n - f(x_n)/f'(x_n)$