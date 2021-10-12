# 5

from numpy import *
import matplotlib.pyplot as plt

def function(x):
    return cos(x**4)/x
    
x = linspace(0.01, 1)
y = function(x)
plt.plot(x, y, 'b-.', label='Y(x)=cos(x^4)/x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()