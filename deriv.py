import sympy

# Define the variable
x = sympy.symbols('x')

# Define the function
#f = (x - sympy.sin(x)) / x**3

f = 4*sympy.exp(-2*x)

# Compute the derivative
f_prime = sympy.diff(f, x)

# Evaluate the derivative at x = 2
f_prime_at_2 = f_prime.subs(x, 0)

print(f_prime_at_2)