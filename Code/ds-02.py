## Code for note DS-02Py ##

# General introduction #
2 + 2               # In [1]
a = 2 + 2           # In [2]
a                   # In [3]
b = 2 * 3           # In [4]
b - 1
b**2
import math         # In [5]
math.sqrt(2)        # In [6]

# Numbers and strings #
type(a)             # In [7]
b = math.sqrt(2)    # In [8]
type(b)             # In [9]
type(2)             # In [10]
type(2.0)           # In [11]
c = 'Messi'         # In [12]
type(c)             # In [13]
d = 5 < a           # In [14]
d                   # In [15]
type(d)             # In [16]
a == 4              # In [17]

# Lists #
x = ['Messi', 'Cristiano', 'Neymar', 'Coutinho']    # In [18]
y = x + [2, 3]                                      # In [19]
y                                                   # In [20]
len(y)                                              # In [21]
y[0:2]                                              # In [22]
y[3:]                                               # In [23]
y[:23]                                              # In [24]
set(y)                                              # In [25]
list(set([1, 0, 1, 0, 7]))                          # In [26]

# For loops #
squares = [0]                               # In [26]
for i in range(1, 4):                       # In [27]
    squares = squares + [i**2]
squares                                     # In [28]
[len(name) for name in x]                   # In [29]
fib = [1, 1]                                # In [30]
for i in range(2, 10):                      # In [31]
    fib = fib + [fib[i-1] + fib[i-2]]
fib                                         # In [32]

# Functions #
def f(x):                                   # In [33]
    y = 1/(1 - x**2)
    return(y)
f(2)                                        # In [34]
def f(x, y):                                # In [35]
    z = x*y/(x**2 + y**2)
    return(z)
f(1, 1)                                     # In [36]
