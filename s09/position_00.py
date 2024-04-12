#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/12 11:15:04 (UT+8) daisuke>
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
file_output = 'position_00.png'

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

# initial conditions (z_0 = 0.0 m, v_0 = 100 m/s)
z_0 =   0.0
v_0 = 100.0
y_init = (z_0, v_0)

# equation to solve
def eqmo (t, y):
    # numpy array "dy"
    dy = numpy.zeros_like (y)
    # equation
    dy[0] = y[1]
    dy[1] = -g_value
    # returning value
    return dy

output_t = numpy.linspace (0.0, 25.0, 25001)

# solving differential equation using Runge-Kutta method
sol = scipy.integrate.solve_ivp (eqmo, [0.0, 25.0], y_init, \
                                 dense_output=True, t_eval=output_t, \
                                 rtol=10**-6, atol=10**-9)

# x and y
list_t = sol.t
list_z = sol.y[0]
list_v = sol.y[1]

# printing result
print (f't: {list_t}')
print (f'z: {list_z}')
print (f'v: {list_v}')

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_title (r'height of a thrown ball')
ax.set_xlabel (r'$t$')
ax.set_ylabel (r'$z$')
ax.set_ylim ([0.0, numpy.amax (list_z) * 1.1])
ax.grid ()

# plotting data
ax.plot (list_t, list_z, 'b-', label='numerical solution', linewidth=5)
ax.legend ()

# writing figure to file
fig.savefig (file_output, dpi=150)
