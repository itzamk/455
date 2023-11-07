'''
Andrew Kozempel
CMPSC 455
Lab 5
6 November 2023
'''

##### PART 1 #####

# interval [1,2]
t0 = 1 # start point
t = 2 # end point

dt = 0.1 # step size
n = int((t-t0) / dt) # number of steps
y0 = -1 # initial value of y

# function of y'
def f(r, s):
    return (1/s**2) - (r/s) - (r**2)

# x and y values
time = [t0 + i * dt for i in range(n+1)] # step/x values
y = [y0 for i in range(n+1)] # y values, initialized to y0

# calculate y values
for j in range(n):
    y[j+1] = y[j] + dt * f(time[j], y[j])

# print both values
for i in range(n+1):
    print(f'x value: {time[i]:.1f}\t y value: {y[i]:.5f}')


##### PART 2 #####

# error = abs(true-approx)

# interval [2,3]
p2_t0 = 2 # start
p2_t = 3 # end

p2_dt = 0.1 # step size
p2_n = int((t-t0) / dt) # number of steps
p2_y0 = 3 # initial value of y

# function of y'
def p2_f(x, y):
    return (1/x) * (2 - y)

# function for true value
def p2_true(x):
    return (2/x) + 2

# x and y values
x = [p2_t0 + i * p2_dt for i in range(n+1)] # step/x values
y = [p2_y0 for i in range(n+1)] # y values, initialized to y0

errors = ['']

# calculate x and y values
for j in range(n):

    y[j+1] = y[j] + dt * f(x[j], y[j]) # calculate approx y value
    y_true = p2_true(x[j]) # calculate true y value

    errors.append(abs(y[j+1]-y_true))

for i in range(n+1):

    print(f'X value: {x[i]}\t Y approximation: {y[i]}\t Y true: {p2_true(x[i])}\t Error: {errors[i]}')