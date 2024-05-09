#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/09 16:54:26 (UT+8) daisuke>
#

# importing sympy module
import sympy

# variable
x = sympy.symbols ('x')

# function y(x)
y = sympy.Function ('y')

# Lane-Emden equation of n=0
lane_emden_n0 = sympy.Eq (x**-2 * (x**2 * y(x).diff (x)).diff (x), -1)

# printing equation
print (f'equation: {lane_emden_n0}')

# solving Lane-Emden equation of n=0
sol = sympy.dsolve (lane_emden_n0, y(x))

# printing result
print (f'solution: {sol}')
