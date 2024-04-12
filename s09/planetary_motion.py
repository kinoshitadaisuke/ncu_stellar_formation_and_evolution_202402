#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/12 12:25:25 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing sys module
import sys

# importing pathlib module
import pathlib

# importing numpy module
import numpy

# importing scipy module
import scipy.integrate

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg
import matplotlib.animation

# initialising a parser
desc   = 'solving equation of motion for a planet around a star'
parser = argparse.ArgumentParser (description=desc)

# adding arguments
parser.add_argument ('-x0', '--x0', type=float, default=1.0,
                     help='initial position in X (default: 1 au)')
parser.add_argument ('-y0', '--y0', type=float, default=0.0,
                     help='initial position in Y (default: 0 au)')
parser.add_argument ('-vx0', '--vx0', type=float, default=0.0,
                     help='initial velocity in X (default: 0 sqrt(GM) au/yr')
parser.add_argument ('-vy0', '--vy0', type=float, default=1.0,
                     help='initial velocity in Y (default: 1 sqrt(GM)) au/yr')
parser.add_argument ('-M', '--M', type=float, default=1.0,
                     help='mass of star (default: 1 solar mass)')
parser.add_argument ('-t', '--time', type=float, default=5.0,
                     help='time of simulation (default: 5 yr)')
parser.add_argument ('-i', '--interval', type=float, default=0.01,
                     help='time interval of image creation (default: 0.01 yr)')
parser.add_argument ('-r', '--resolution', type=int, default=225, \
                     help='resolution of output file (default: 225 dpi)')
parser.add_argument ('-o', '--output', default='', \
                     help='output directory name')

# parsing arguments
args = parser.parse_args ()

# parameters
qx0        = args.x0
qy0        = args.y0
vx0        = args.vx0
vy0        = args.vy0
Mstar      = args.M
time_end   = args.time
dt         = args.interval
resolution = args.resolution
dir_output = args.output

# check of dir_output
if (dir_output == ''):
    print ("ERROR: output directory name must be given!")
    sys.exit ()

# making a pathlib object
path_dir = pathlib.Path (dir_output)

# existence check of output directory
if not (path_dir.exists ()):
    # create a directory if it does not exist
    path_dir.mkdir ()
    
#
# constants
#

# unit of time: year
# unit of distance: au

# pi
pi = numpy.pi

# gravitational constant
GM = 4.0 * pi * pi

#
# equation of motion
#
def eqmo (t, y):
    dy = numpy.zeros_like (y)
    r_cubed = ( y[0]**2 + y[2]**2 )**1.5
    dy[0] = y[1]
    dy[1] = -GM * y[0] / r_cubed
    dy[2] = y[3]
    dy[3] = -GM * y[2] / r_cubed
    return dy

# time to write position and velocity
n_step = int (time_end / dt) + 1
t_eval = numpy.linspace (0.0, time_end, n_step)

# initial values
y_init = (qx0, vx0  * numpy.sqrt (GM), qy0, vy0 * numpy.sqrt (GM))

# orbital integration
sol = scipy.integrate.solve_ivp (eqmo, [0.0, time_end * 2.0 * pi], y_init, \
                                 t_eval=t_eval, dense_output=True, \
                                 rtol=10**-6, atol=10**-9)

# results (positions and velocities)
qx = sol.y[0]
qy = sol.y[2]
vx = sol.y[1]
vy = sol.y[3]

# finding maximum and minimum values
qx_min        = numpy.amin (qx)
qx_max        = numpy.amax (qx)
qy_min        = numpy.amin (qy)
qy_max        = numpy.amax (qy)
list_maxmin   = [abs (qx_min), abs (qx_max), abs (qy_min), abs (qy_max)]
sorted_maxmin = sorted (list_maxmin)
x_min         = -1.0 * sorted_maxmin[-1] * 1.2
x_max         = +1.0 * sorted_maxmin[-1] * 1.2
y_min         = -1.0 * sorted_maxmin[-1] * 1.2
y_max         = +1.0 * sorted_maxmin[-1] * 1.2

# making plots
for i in range ( len (qx) ):
    print (f'{i:08d} {qx[i]:8.4f} {qy[i]:8.4f} {vx[i]:8.4f} {vy[i]:8.4f}')

    # output file name
    file_output = f'{dir_output}/{dir_output}_{i:08d}.png'
    
    #
    # plotting using Matplotlib
    #
    
    # making objects "fig" and "ax"
    fig    = matplotlib.figure.Figure ()
    canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
    ax     = fig.add_subplot (111)

    # axes
    ax.set_title ('Planetary Motion')
    ax.set_xlabel ('X [au]')
    ax.set_ylabel ('Y [au]')
    ax.set_xlim (x_min, x_max)
    ax.set_ylim (y_min, y_max)
    ax.set_aspect ('equal')

    # plotting a figure
    ax.plot (0.0, 0.0, linestyle='None', color='yellow', \
             marker='o', markersize=10, label='star')
    if (i < 100):
        for j in range (i):
            ax.plot (qx[j], qy[j], linestyle='None', color='cyan', \
                     marker='o', markersize=3, alpha=j/i)
    else:
        for j in range (100):
            ax.plot (qx[i-j], qy[i-j], linestyle='None', color='cyan', \
                     marker='o', markersize=3, alpha=1.0-j/100.0)
    ax.plot (qx[0:i], qy[0:i], linestyle='-', color='black', \
             marker=',', alpha=0.5)
    ax.plot (qx[i], qy[i], linestyle='None', color='green', \
             marker='o', markersize=5, label='planet')
    text_time    = f'Time: {i * dt:8.2f} year'
    text_initial = f'Initial conditions'
    text_mass    = f'mass of star = {Mstar:5.2f} solar mass'
    text_iq      = f'(qx0, qy0) = ({qx0:4.2f} au, {qy0:4.2f} au)'
    vx0_auyr     = vx0 * numpy.sqrt (GM)
    vy0_auyr     = vy0 * numpy.sqrt (GM)
    text_iv      = f'(vx0, vy0) = ({vx0_auyr:4.2f} ay/yr, {vy0_auyr:4.2f} au/yr)'
    ax.text (0.03, 0.95, text_time, transform=ax.transAxes)
    ax.text (0.03, 0.18, text_initial, transform=ax.transAxes)
    ax.text (0.05, 0.13, text_mass, transform=ax.transAxes)
    ax.text (0.05, 0.08, text_iq, transform=ax.transAxes)
    ax.text (0.05, 0.03, text_iv, transform=ax.transAxes)
    ax.legend ()

    # saving the figure to a file
    fig.savefig (file_output, dpi=resolution)
