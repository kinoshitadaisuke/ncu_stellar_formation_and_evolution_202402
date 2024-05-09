#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/09 14:48:30 (UT+8) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f
f = (x + 1)**2

# expansion of (x+1)**2
f2 = sympy.expand (f)

# printing result
print (f'{f} = {f2}')
