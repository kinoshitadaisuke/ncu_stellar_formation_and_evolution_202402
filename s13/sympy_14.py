#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/09 17:03:14 (UT+8) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f(x)
f = sympy.exp (-x**2)

# positive infinity
pinf = sympy.oo

# negative infinity
ninf = -sympy.oo

# integration of f(x)
I = sympy.integrate (f, (x, ninf, pinf))

# printing result
print (f'I = {I}')
