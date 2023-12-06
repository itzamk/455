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