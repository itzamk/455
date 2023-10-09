# Andrew Kozempel
# CMPSC 455
# Fall 2023
# 10 October 2023 In Class Practice

def f(x):
    
    return x**3 - x - 3

def f_prime(x):

    return 3*x**2 - 1

def bisection(a, b, steps):

    for i in range(steps):

        c = (a + b) / 2.0

        if f(c) == 0:
            return c
        
        elif f(c) * f(a) < 0:
            b = c

        else:
            a = c

    return (a + b) / 2.0

def newton(x0, steps):

    for i in range(steps):

        x0 = x0 - f(x0) / f_prime(x0)
        print(x0)

    return x0

bisect = bisection(-5, 5, 10)
print(f"\nBisection Method: {bisect}")

newt = newton(0, 10)
print(f"Newton's Method:  {newt}\n")