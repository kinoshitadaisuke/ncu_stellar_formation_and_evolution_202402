#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/26 09:31:54 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# construction of parser object for argparse
descr  = 'zones of different physical states on rho-T diagram'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-o', '--output', help='output file name')
parser.add_argument ('-r', '--resolution', type=float, default=150.0, \
                     help='resolution of output file in DPI (default: 150)')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
file_output = args.output
resolution  = args.resolution

# making pathlib object
path_output = pathlib.Path (file_output)

# existence check of output file
if (path_output.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: file "{file_output}" exists!')
    print (f'ERROR: stopping...')
    print (f'ERROR:')
    # exit
    sys.exit (0)

# check of suffix of output file
if not ( (path_output.suffix == '.eps') \
         or (path_output.suffix == '.pdf') \
         or (path_output.suffix == '.png') \
         or (path_output.suffix == '.ps') ):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: output file type "{path_output.suffix}" is not supported!')
    print (f'ERROR: choose one either from EPS, PDF, PNG, or PS.')
    print (f'ERROR: stopping...')
    print (f'ERROR:')
    # exit
    sys.exit (0)

# number of data points
n = 10000

# border of ideal gas zone and degenerate gas zone
ideal_deg_logx = numpy.linspace (5.0, 9.0, n)
ideal_deg_logy = 1.5 * ideal_deg_logx - 4.13

# border of ideal gas zone and relativistic degenerate gas zone
ideal_rdeg_logx = numpy.linspace (9.0, 10.0, n)
ideal_rdeg_logy = 3.0 * ideal_rdeg_logx - 17.60

# border of degenerate gas zone and relativistic degenerate gas zone
deg_rdeg_logx = numpy.linspace (5.0, 9.0, n)
deg_rdeg_logy = numpy.array ([9.34] * n)

# border of ideal gas zone and radiation zone
ideal_rad_logx = numpy.linspace (6.5, 10.0, n)
ideal_rad_logy = 3.0 * ideal_rad_logx - 20.73

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

ideal1_x  = numpy.linspace (5.00, 6.91, n)
ideal1_y1 = 1.5 * ideal1_x - 4.13

ideal2_x  = numpy.linspace (6.91, 9.00, n)
ideal2_y1 = 3.0 * ideal2_x - 20.73
ideal2_y2 = 1.5 * ideal2_x - 4.13

ideal3_x  = numpy.linspace (9.00, 10.00, n)
ideal3_y1 = 3.0 * ideal3_x - 20.73
ideal3_y2 = 3.0 * ideal3_x - 17.60

# axes
ax.set_xlabel (r"$\log (T_c)$")
ax.set_ylabel (r"$\log (\rho_c)$")
ax.set_xlim (5.0, 10.0)
ax.set_ylim (0.0, 13.0)
ax.set_box_aspect (1)

# plotting data
ax.fill_between (x=ideal_rad_logx, y1=0.0, y2=ideal_rad_logy, \
                 color='red', alpha=0.2, linewidth=0.0)
ax.fill_between (x=ideal_deg_logx, y1=ideal_deg_logy, y2=deg_rdeg_logy, \
                 color='blue', alpha=0.2, linewidth=0.0)
ax.fill_between (x=deg_rdeg_logx, y1=deg_rdeg_logy, y2=100.0, \
                 color='green', alpha=0.2, linewidth=0.0)
ax.fill_between (x=ideal_rdeg_logx, y1=ideal_rdeg_logy, y2=100.0, \
                 color='green', alpha=0.2, linewidth=0.0)
ax.fill_between (x=ideal1_x, y1=ideal1_y1, \
                 color='orange', alpha=0.2, linewidth=0.0)
ax.fill_between (x=ideal2_x, y1=ideal2_y1, y2=ideal2_y2, \
                 color='orange', alpha=0.2, linewidth=0.0)
ax.fill_between (x=ideal3_x, y1=ideal3_y1, y2=ideal3_y2, \
                 color='orange', alpha=0.2, linewidth=0.0)
ax.plot (ideal_deg_logx,  ideal_deg_logy,  '-', label=r"$P_{ideal}=P_{deg}$")
ax.plot (ideal_rdeg_logx, ideal_rdeg_logy, '-', label=r"$P_{ideal}=P_{r-deg}$")
ax.plot (deg_rdeg_logx,   deg_rdeg_logy,   '-', label=r"$P_{deg}=P_{r-deg}$")
ax.plot (ideal_rad_logx,  ideal_rad_logy,  '-', label=r"$P_{ideal}=10 P_{rad}$")
ax.text (7.5,  5.0, "ideal gas", horizontalalignment='center')
ax.text (6.0,  7.0, "degenerate gas", horizontalalignment='center')
ax.text (7.0, 11.0, "relativistic degenerate gas", horizontalalignment='center')
ax.text (9.0,  3.0, "radiation pressure", horizontalalignment='center')
ax.set_title (r"$\rho$-$T$ diagram")
ax.legend (loc='lower left')

# saving file
fig.savefig (file_output, dpi=resolution)
