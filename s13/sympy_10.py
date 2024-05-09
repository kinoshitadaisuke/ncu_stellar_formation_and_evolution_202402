#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/09 15:21:18 (UT+8) daisuke>
#

# importing sympy module
import sympy

# function y
y = sympy.Function ('y')

# variable x
x, k = sympy.symbols ('x k')

# dy/dx
dy_dx = sympy.diff (y(x), x)

# differential equation
eq = sympy.Eq (dy_dx, -k*y(x))

# solving dy/dx = -ky
sol = sympy.dsolve (eq, y(x))

# printing result
print (f'equation: {eq}')
print (f'solution: {sol}')
