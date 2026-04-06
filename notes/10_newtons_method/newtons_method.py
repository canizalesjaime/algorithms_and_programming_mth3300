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