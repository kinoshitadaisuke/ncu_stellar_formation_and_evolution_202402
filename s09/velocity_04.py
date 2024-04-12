#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/12 11:04:44 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants
import scipy.integrate

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'velocity_04.png'

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

# initial condition (v_0 = 100 m/s)
v_0 = 100.0

# equation to solve
def dydt (t, y):
    # dy/dx = -g
    dy = -g_value
    # returning value
    return dy

output_t = numpy.linspace (0.0, 25.0, 25001)

# solving differential equation using Runge-Kutta method
sol = scipy.integrate.solve_ivp (dydt, [0.0, 25.0], [v_0], \
                                 dense_output=True, t_eval=output_t, \
                                 rtol=10**-6, atol=10**-9)

# x and y
list_t = sol.t
list_v = sol.y[0]

# printing result
print (f't: {list_t}')
print (f'v: {list_v}')

# analytical solution
ana_t = output_t
ana_v = -g_value * ana_t + v_0

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_title (r'velocity change')
ax.set_xlabel (r'$t$')
ax.set_ylabel (r'$v$')
ax.grid ()

# plotting data
ax.plot (list_t, list_v, 'b-', label='numerical solution', linewidth=5)
ax.plot (ana_t, ana_v, 'r--', label='analytical solution', linewidth=2)
ax.legend ()

# writing figure to file
fig.savefig (file_output, dpi=150)
