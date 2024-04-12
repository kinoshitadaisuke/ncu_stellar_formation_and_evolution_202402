#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/12 10:48:28 (UT+8) daisuke>
#

# importing numpy module
import numpy

# coefficient
k = 0.1

# initial condition
y_0 = 100.0

# x values
output_x = numpy.linspace (0.0, 50.0, 50001)

# analytical solution
ana_x = output_x
ana_y = y_0 * numpy.exp (-k * ana_x)

# printing result
print (f'analytical solution:')
print (f'x: {ana_x}')
print (f'y: {ana_y}')
