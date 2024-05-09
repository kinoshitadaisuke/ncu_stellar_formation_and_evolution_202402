#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/09 17:01:22 (UT+8) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f(x)
f = sympy.sqrt (4 - x**2)

# integration of f(x) from 0 to 2
I = sympy.integrate (f, (x, 0, 2))

# printing result
print (f'I = {I}')
