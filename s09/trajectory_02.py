#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/12 11:42:49 (UT+8) daisuke>
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
file_output = 'trajectory_02.png'

# pi
pi = numpy.pi

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

# initial conditions
#   x_0 = 0.0 m, z_0 = 0.0 m,
#   vx_0 = 100 * cos (angle) m/s, vz_0 = 100 * sin (angle) m/s)
angle  = 30.0 * pi / 180.0
x_0    =   0.0
z_0    =   0.0
vx_0   = 100.0 * numpy.cos (angle)
vz_0   = 100.0 * numpy.sin (angle)
y_init = (x_0, vx_0, z_0, vz_0)

# equation to solve
def eqmo (t, y):
    # numpy array "dy"
    dy = numpy.zeros_like (y)
    # equation
    dy[0] = y[1]
    dy[1] = 0.0
    dy[2] = y[3]
    dy[3] = -g_value
    # returning value
    return dy

output_t = numpy.linspace (0.0, 25.0, 25001)

# solving differential equation using Runge-Kutta method
sol = scipy.integrate.solve_ivp (eqmo, [0.0, 25.0], y_init, \
                                 dense_output=True, t_eval=output_t, \
                                 rtol=10**-6, atol=10**-9)

# x and y
list_t  = sol.t
list_x  = sol.y[0]
list_vx = sol.y[1]
list_z  = sol.y[2]
list_vz = sol.y[3]

# printing result
print (f't: {list_t}')
print (f'x: {list_x}')
print (f'vx: {list_vx}')
print (f'z: {list_z}')
print (f'vz: {list_vz}')

# analytical solution
ana_t = output_t
ana_x = vx_0 * ana_t + x_0
ana_z = -0.5 * g_value * ana_t**2 + vz_0 * ana_t + z_0

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_title (r'trajectory of a thrown ball')
ax.set_xlabel (r'$x$')
ax.set_ylabel (r'$z$')
ax.set_xlim ([0.0, 1200.0])
ax.set_ylim ([0.0, 500.0])
ax.grid ()

# plotting data
ax.plot (list_x, list_z, 'b-', label='numerical solution', linewidth=5)
ax.plot (ana_x, ana_z, 'r--', label='analytical solution', linewidth=2)
ax.legend ()

# writing figure to file
fig.savefig (file_output, dpi=150)
