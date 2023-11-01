'''
Andrew Kozempel
Lab 4
'''

import math

##################
##### part 1 #####
##################

print('\n--------PART 1--------\n')

def f1(x):
    return math.log(x) - 5 + x

def bisection(a, b):

    for i in range(10):

        c = (a + b) / 2.0

        if f1(c) == 0:
            break

        elif f1(a) * f1(c) < 0:
            b = c

        else:
            a = c

    return c

a, b = 3, 4
approximation = bisection(a, b)
error_bound = (b - a) / (2**11)

print(f"Approximation 10 steps: {approximation}")
print(f"Error bound after 10 steps: {error_bound}")

##################
##### part 2 #####
##################
print('\n--------PART 2--------\n')

def f2(x):
    return x * math.exp(-x)

def f2_prime(x):
    return math.exp(-x) - (x * math.exp(-x))

def newtons(x):
    iterations = 0
    x_prev = x + 1
    
    while abs(x - x_prev) >= 0.001:
        iterations += 1
        x_prev = x
        x = x - (f2(x)/f2_prime(x))

    print(f"Root is {x} after {iterations} iterations")
    return x

print(f'Starting with p0 = 0.2:\n\t {newtons(0.2)}')
#print(f'Starting with p0 = 2:\n\t {newtons(2)}')

##################
##### part 3 #####
##################
print('\n--------PART 3--------\n')

# function and 
def f3(x):
    return math.exp(math.sin(x))

def f3_prime(x):
    return math.cos(x) * math.exp(math.sin(x))

def f3_2prime(x):
    return (math.cos(x)**2 - math.sin(x)) * math.exp(math.sin(x))

# 3 point forward
def forward_difference(x, h):
    return (-3*f3(x) + 4*f3(x+h) - f3(x+2*h)) / (2*h)

# 3 point backward
def backward_difference(x, h):
    return (f3(x-2*h) - 4*f3(x-h) + 3*f3(x)) / (2*h)

# on the interval of [0, pi/2]
x0 = 0
x1 = math.pi/2

actual_derivative_x0 = f3_prime(x0)
fw_prev_error = 0

print('FORWARD DIFFERENCE:\n')
print(f'Actual Derivative: {actual_derivative_x0}')
for i in range(1, 11):
    h = (1/2)**i
    
    forward_approx = forward_difference(x0, h)
    forward_error = abs(forward_approx - actual_derivative_x0)

    if fw_prev_error != 0:
        fw_ratio = round(forward_error / fw_prev_error, 2)
    else:
        fw_ratio = ''

    print(f'h = {h:.5f}\t Approximation: {forward_approx:.5f}\t Error: {forward_error:.5f}\t Error Ratio: {fw_ratio}')
    fw_prev_error = forward_error