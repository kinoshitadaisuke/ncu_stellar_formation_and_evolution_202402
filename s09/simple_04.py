#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/12 10:49:14 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.integrate

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# coefficient
k = 0.1

# initial condition
y_0 = 100.0

# output file name
file_output = 'simple_04.png'

# equation to solve
def dydx (t, y):
    # dy/dx = -ky
    dy = -k * y
    # returning value
    return dy

# x values
output_x = numpy.linspace (0.0, 50.0, 50001)

# solving differential equation using Runge-Kutta method
sol = scipy.integrate.solve_ivp (dydx, [0.0, 50.0], [y_0], \
                                 dense_output=True, t_eval=output_x, \
                                 rtol=10**-6, atol=10**-9)

# x and y
list_x = sol.t
list_y = sol.y[0]

# printing results
print (f'numerical solution:')
print (f'x: {list_x}')
print (f'y: {list_y}')

# analytical solution
ana_x = output_x
ana_y = y_0 * numpy.exp (-k * ana_x)

# printing result
print (f'analytical solution:')
print (f'x: {ana_x}')
print (f'y: {ana_y}')

# printing status
print (f'now, generating a plot using Matplotlib...')

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_title (r'$dy/dx = -ky$')
ax.set_xlabel (r'$x$')
ax.set_ylabel (r'$y$')
ax.set_yscale ('log')
ax.grid ()

# plotting data
ax.plot (list_x, list_y, 'b-', label='numerical solution', linewidth=5)
ax.plot (ana_x, ana_y, 'r--', label='analytical solution', linewidth=2)
ax.legend ()

# writing figure to file
fig.savefig (file_output, dpi=150)

# printing status
print (f'finished generating a plot using Matplotlib!')
