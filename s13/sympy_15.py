#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/09 17:05:22 (UT+8) daisuke>
#

# importing sympy module
import sympy

# variable
x = sympy.symbols ('x')

# function f(x)
f = x**4 * sympy.exp (-x**2)

# positive infinity
pinf = sympy.oo

# integration of f(x) from 0 to infinity
I = sympy.integrate (f, (x, 0, pinf))

# printing result
print (f'I = {I}')
