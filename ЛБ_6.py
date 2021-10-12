import math
from scipy import optimize

x0 = 0.05
y0 = 0.8

def f1(y):
    return (1 - math.cos(y - 1))
    
def f2(x):
    return (0.8 - 0.5 * math.sin(x))

def iter(e, x, y):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1
    while((abs(xn1 - xn) >= e) & (abs(yn1-yn) >= e)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn1)
        n = n + 1
    print("Solution iteration method:")
    print("x =", xn1, "\ny =", yn1,"\niteration count:", n)

iter(x0, y0, 0.0001)
    
def function(x):
    return math.sin(x[0]) + 2 * x[1] - 1.6, math.cos(x[1] - 1) + x[0] - 1

s = optimize.root(function, [x0, y0], method = 'hybr')
print("\nCheck")
print(s.x)