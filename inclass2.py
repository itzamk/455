#bisection method
import math

def f(x):

    return math.exp(x) - x**2

a = 5
b = 6

fa = f(a)
fb = f(b)

er = 10**-6
k = int(math.ceil(((math.log10(b-a) - math.log(er)) / math.log10(2))))

for n in range(1,k):
  
    c = (a+b)/2
    fc = f(c)

    print('\nc is', c)
    print('error is', abs(b-a))

    if (fc==0):
        print('root is', c)

    elif(fc*fb>0):
        b=c
        fb=fc

    else:
        a=c
        fa=fc

    if(abs(b-a)<er):
        print(f"Root is approximately: {c}")
        break