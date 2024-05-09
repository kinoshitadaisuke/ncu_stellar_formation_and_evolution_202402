#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/09 17:05:42 (UT+8) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f(x)
func = 1 / sympy.sqrt (1/x - 1)

# integration of f(x) from x=0 to x=1
I = sympy.integrate (func, (x, 0, 1))

# printing result
print (f'I = {I}')
