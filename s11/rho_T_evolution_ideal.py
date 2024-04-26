#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2024/04/26 10:08:22 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy

# importing scipy module
import scipy.constants

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# construction of parser object for argparse
descr  = 'evolution of stars'
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

# constants
G  = scipy.constants.G
pi = scipy.constants.pi
K0 = 1.36 * 10**4  # for solar composition
Bn = 0.206         # for n=1.5
Ms = 1.99 * 10**30 # solar mass

# number of data points
n = 10000

# border of ideal gas and degenerate gas
ideal_deg_logx = numpy.linspace (5.0, 9.0, n)
ideal_deg_logy = 1.5 * ideal_deg_logx - 4.13

# border of ideal gas and relativistic degenerate gas
ideal_rdeg_logx = numpy.linspace (9.0, 10.0, n)
ideal_rdeg_logy = 3.0 * ideal_rdeg_logx - 17.60

# border of degenerate gas and relativistic degenerate gas
deg_rdeg_logx = numpy.linspace (5.0, 9.0, n)
deg_rdeg_logy = numpy.array ([9.34] * n)

# border of ideal gas and radiation
ideal_rad_logx = numpy.linspace (5.5, 10.0, n)
ideal_rad_logy = 3.0 * ideal_rad_logx - 20.73

# evolutionary track of 0.1 solar mass star
M = 0.1 * Ms
evo_001_logx = numpy.linspace (5.0, 7.05, n)
evo_001_logy = 3.0 * evo_001_logx - 2.0 * numpy.log10 (M) \
    + numpy.log10 (K0**3 / (4.0 * pi * Bn**3 * G**3) )

# evolutionary track of 0.3 solar mass star
M = 0.3 * Ms
evo_003_logx = numpy.linspace (5.0, 7.65, n)
evo_003_logy = 3.0 * evo_003_logx - 2.0 * numpy.log10 (M) \
    + numpy.log10 (K0**3 / (4.0 * pi * Bn**3 * G**3) )

# evolutionary track of 1 solar mass star
M = 1.0 * Ms
evo_010_logx = numpy.linspace (5.0, 8.35, n)
evo_010_logy = 3.0 * evo_010_logx - 2.0 * numpy.log10 (M) \
    + numpy.log10 (K0**3 / (4.0 * pi * Bn**3 * G**3) )

# evolutionary track of 3 solar mass star
M = 3.0 * Ms
evo_030_logx = numpy.linspace (5.0, 9.0, n)
evo_030_logy = 3.0 * evo_030_logx - 2.0 * numpy.log10 (M) \
    + numpy.log10 (K0**3 / (4.0 * pi * Bn**3 * G**3) )

# evolutionary track of 10 solar mass star
M = 10.0 * Ms
evo_100_logx = numpy.linspace (5.0, 10.0, n)
evo_100_logy = 3.0 * evo_100_logx - 2.0 * numpy.log10 (M) \
    + numpy.log10 (K0**3 / (4.0 * pi * Bn**3 * G**3) )

# evolutionary track of 30 solar mass star
M = 30.0 * Ms
evo_300_logx = numpy.linspace (5.0, 10.0, n)
evo_300_logy = 3.0 * evo_300_logx - 2.0 * numpy.log10 (M) \
    + numpy.log10 (K0**3 / (4.0 * pi * Bn**3 * G**3) )

ideal1_x  = numpy.linspace (5.00, 6.91, n)
ideal1_y1 = 1.5 * ideal1_x - 4.13

ideal2_x  = numpy.linspace (6.91, 9.00, n)
ideal2_y1 = 3.0 * ideal2_x - 20.73
ideal2_y2 = 1.5 * ideal2_x - 4.13

ideal3_x  = numpy.linspace (9.00, 10.00, n)
ideal3_y1 = 3.0 * ideal3_x - 20.73
ideal3_y2 = 3.0 * ideal3_x - 17.60

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel (r"$\log (T_c)$")
ax.set_ylabel (r"$\log (\rho_c)$")
ax.set_xlim (6.0, 10.0)
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
ax.plot (ideal_deg_logx,  ideal_deg_logy, '--')
ax.plot (ideal_rdeg_logx, ideal_rdeg_logy, '--')
ax.plot (deg_rdeg_logx,   deg_rdeg_logy, '--')
ax.plot (ideal_rad_logx,  ideal_rad_logy, '--')
ax.plot (evo_001_logx, evo_001_logy, '-', label=r"0.1 $M_\odot$", lw=3)
ax.plot (evo_003_logx, evo_003_logy, '-', label=r"0.3 $M_\odot$", lw=3)
ax.plot (evo_010_logx, evo_010_logy, '-', label=r"1 $M_\odot$",   lw=3)
ax.plot (evo_030_logx, evo_030_logy, '-', label=r"3 $M_\odot$",   lw=3)
ax.plot (evo_100_logx, evo_100_logy, '-', label=r"10 $M_\odot$",  lw=3)
ax.plot (evo_300_logx, evo_300_logy, '-', label=r"30 $M_\odot$",  lw=3)
ax.text (8.1,  5.0, "ideal gas", horizontalalignment='center')
ax.text (7.0,  8.0, "degenerate gas", horizontalalignment='center')
ax.text (8.0, 11.0, "relativistic degenerate gas", horizontalalignment='center')
ax.text (9.0,  2.5, "radiation pressure", horizontalalignment='center')
ax.set_title (r"evolutionary track on $T$-$\rho$ plane")
ax.legend (bbox_to_anchor=(1.01, 1.0), alignment='left')

# saving file
fig.savefig (file_output, dpi=resolution)
