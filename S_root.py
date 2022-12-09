import scipy
import numpy as np

list_roots=[]

def func1(x,x1):
    return (-12*(x**4)*np.sin(np.cos(x))-18*(x**3)+5*(x**2)+10*x-30)
t0=1
min=-10
max=0
x1=scipy.optimize.brentq(func1, min,max,args=(t0))


def func2(x,x2,):
    return (-12*(x**4)*np.sin(np.cos(x))-18*(x**3)+5*(x**2)+10*x-30)
t0=1
min=0
max=10
x2=scipy.optimize.brentq(func2, min,max,args=(t0))


list_roots.append(x1)
list_roots.append(x2)
f = lambda x: round(x,2)
list_roots = list(map(f,list_roots))
print(list_roots)
# list_roots=list(list_roots)

roots=[]
roots.append(list_roots[0]-1)
roots.append(round((list_roots[0]+list_roots[1])/2,2))
roots.append(list_roots[1]+1)
print(roots)

new_list=list(map(f,roots))
print(new_list)
sign=lambda x:'f(x)>=0' if x>0 else 'f(x)<0'
sign=list(map(sign,roots))
print(sign)

print(f)
