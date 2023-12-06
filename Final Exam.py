'''
Andrew Kozempel
CMPSC 455
Fall 2023
Final Exam
'''

import math

'''
Question 1
'''

def g(x):

    return (math.exp(x)-1) / x

for i in range(1,16):

    x = 10 ** -i

    print(f'x = 10^{-i}\tAnalytical Limit: {g(x)}')

'''
Question 2
'''

def f(x):

    return x**2 - 8

def df(x):

    return 2*x

def newton(f, df, x, tol=10e-6, max_iter=100):

    for i in range(max_iter):
        
        dx = f(x) / df(x)
        x -= dx
        
        if abs(dx) < tol:
            return x, i
        
    return x

x,i = newton(f, df, 3)

print(f'Root Approximation is {x:.5f} after {i} iterations.\tError = {abs(x-math.sqrt(8)):.5f}')