def bisection(f, a, b, tol=1e-5, max_iter=1000):
    """
    Finds the root of a function f using the bisection method.
    
    Parameters:
    - f: the function for which the root is sought.
    - a, b: two initial points such that f(a)*f(b) < 0.
    - tol: the stopping tolerance. The method will stop when the width of the interval is less than tol.
    - max_iter: the maximum number of iterations.
    
    Returns:
    - The root of the function f within the interval [a, b].
    """
    
    if f(a) * f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")
    
    iter_count = 0
    while (b - a) / 2.0 > tol and iter_count < max_iter:
        c = (a + b) / 2.0
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    return (a + b) / 2.0

# Test
f = lambda x: x**2 - 4
root = bisection(f, 0, 3)
print(f"The root is approximately: {root}")
