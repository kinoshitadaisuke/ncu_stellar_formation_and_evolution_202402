#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/09 16:59:14 (UT+8) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f(x)
f = -x + 1

# integration of f(x) from 0 to 1
I = sympy.integrate (f, (x, 0, 1))

# printing result
print (f'I = {I}')
