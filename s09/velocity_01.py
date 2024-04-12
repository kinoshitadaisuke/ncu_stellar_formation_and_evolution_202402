#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/12 10:56:07 (UT+8) daisuke>
#

# importing scipy module
import scipy.constants

# standard acceleration of gravity
g = scipy.constants.physical_constants['standard acceleration of gravity']

# value of g
g_value = g[0]

# unit of g
g_unit = g[1]

# error of g
g_error = g[2]

# printing result
print (f'standard acceleration of gravity:')
print (f' g = {g_value} +/- {g_error} [{g_unit}]')
