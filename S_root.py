from scipy.optimize import fsolve
from sympy import *
import math


def func(x):
    return -12*(x**4)*math.sin(math.cos(x))-18*(x**3)+5*(x**2)+10*x-30

x0 = fsolve(func, 0)
print(x0)

# x = Symbol('x')
# a=-12*(0.45519539*0.45519539)*sin(cos(0.45519539))-18*0.45519539-5
# b=10
# c=-30
# D=b*b-4*a*c
# print(D)









