from sympy import *
import matplotlib.pyplot as plt
import math
# a=float(input('X1: '))
# b=float(input('X2: '))
# y1 = -12*(a**4)*math.sin(math.cos(a))-18*(a**3)+5*(a**2)+10*a-30
# y2 = -12*(b**4)*math.sin(math.cos(b))-18*(b**3)+5*(b**2)+10*b-30

# if a>b and y1>y2:
#     print(f'Функция в промежутке от {b} до {a} возростает')
# elif a<b and y1>y2:
#     print(f'Функция в промежутке от {a} до {b} убывает')
# else:
#     print('Введите промежуток поменьше')
# print(y1,y2)


# def roots(a, b, c):
#     D = b ** 2 - 4 * a * c
#     d = D ** 0.5
#     x1 = (-b + d) / (2 * a)
#     x2 = (-b - d) / (2 * a)
#     print(d)
#     if D > 0:
#         return x1, x2
#     elif x1 == x2:
#         return x1
#     else:
#         exit('Complex roots')

# x=Symbol('x')

# k1, k2, k3 = 12*(x*x)*sin(cos(x))-18*x+5, 10, -30

# roots = roots(k1, k2, k3)
# print(roots)

list_x = list(range(-200, 0))
f = lambda x: x/100
list_x = list(map(f, list_x))
print(f'(x)= {list_x} \n')

f = lambda x: -12*(x**4)*math.sin(math.cos(x))-18*(x**3)+5*(x**2)+10*x-30
list_y = list(map(f, list_x))
# list_y=list(list_y)
# list_y.sort()
print(f'f(x)= ',list_y)








