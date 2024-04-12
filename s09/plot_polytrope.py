#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/12 12:53:57 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing sys module
import sys

# importing pathlib module
import pathlib

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# initialising a parser
desc   = 'plotting polytropes'
parser = argparse.ArgumentParser (description=desc)

# adding arguments
parser.add_argument ('-d', '--density', \
                     default='polytrope_density.png', \
                     help='output file name for radius-density plot')
parser.add_argument ('-p', '--pressure', \
                     default='polytrope_pressure.png', \
                     help='output file name for radius-pressure plot')
parser.add_argument ('-t', '--temperature', \
                     default='polytrope_temperature.png', \
                     help='output file name for radius-temperature plot')
parser.add_argument ('-r', '--resolution', \
                     default=225, \
                     help='resolution of output image (default: 225 DPI)')
parser.add_argument ('files', nargs='+', help='data files')

# parsing arguments
args = parser.parse_args ()

# parameters
list_files       = args.files
file_density     = args.density
file_pressure    = args.pressure
file_temperature = args.temperature
resolution       = args.resolution

# check of output files
path_density     = pathlib.Path (file_density)
path_pressure    = pathlib.Path (file_pressure)
path_temperature = pathlib.Path (file_temperature)
if not ( (path_density.suffix == '.eps') \
         or (path_density.suffix == '.pdf') \
         or (path_density.suffix == '.png') \
         or (path_density.suffix == '.ps') ):
    # printing message
    print (f'ERROR: output file must be either EPS, PDF, PNG, or PS!')
    # exit
    sys.exit ()
if not ( (path_pressure.suffix == '.eps') \
         or (path_pressure.suffix == '.pdf') \
         or (path_pressure.suffix == '.png') \
         or (path_pressure.suffix == '.ps') ):
    # printing message
    print (f'ERROR: output file must be either EPS, PDF, PNG, or PS!')
    # exit
    sys.exit ()
if not ( (path_temperature.suffix == '.eps') \
         or (path_temperature.suffix == '.pdf') \
         or (path_temperature.suffix == '.png') \
         or (path_temperature.suffix == '.ps') ):
    # printing message
    print (f'ERROR: output file must be either EPS, PDF, PNG, or PS!')
    # exit
    sys.exit ()

#
# plotting using Matplotlib
#

def plot_polytrope (y_data):
    # making objects "fig" and "ax"
    fig    = matplotlib.figure.Figure ()
    canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
    ax     = fig.add_subplot (111)

    # axes
    ax.set_title ('Polytropic models')
    ax.set_xlabel ('r/R')
    if (y_data == 'density'):
        text_ylabel = r'$\rho/\rho_c$'
    elif (y_data == 'pressure'):
        text_ylabel = r'$P/P_c$'
    elif (y_data == 'temperature'):
        text_ylabel = r'$\theta$'
    ax.set_ylabel (text_ylabel)
    ax.set_aspect ('equal')
    ax.set_xlim (-0.01, 1.01)
    ax.set_ylim (-0.01, 1.01)

    # processing each data file
    for file_data in list_files:
        # making pathlib object
        path_data = pathlib.Path (file_data)
        # existence check
        if not (path_data.exists ()):
            # printing message
            print (f'ERROR: data file "{file_data}" does not exist!')
            print (f'ERROR: skipping...')
            # skip
            continue
        # preparing empty list to store data
        list_xi             = []
        list_theta          = []
        list_r_over_R       = []
        list_rho_over_rho_c = []
        list_P_over_P_c     = []
        # opening data file
        with open (file_data, 'r') as fh:
            # reading data file line-by-line
            for line in fh:
                # reading polytropic index n
                # '# polytropic index n = 4.500000'
                if (line[:12] == '# polytropic'):
                    index = float (line[23:31])
                # if line stars with '#', then skip
                if (line[0] == '#'):
                    continue
                # splitting line
                (xi, theta, r_over_R, rho_over_rho_c, P_over_P_c) \
                    = line.split ()
                # appending data to lists
                list_xi.append ( float (xi) )
                list_theta.append ( float (theta) )
                list_r_over_R.append ( float (r_over_R) )
                list_rho_over_rho_c.append ( float (rho_over_rho_c) )
                list_P_over_P_c.append ( float (P_over_P_c) )

        # plotting data
        text_label = f'n = {index:4.2f}'
        if (y_data == 'density'):
            ax.plot (list_r_over_R, list_rho_over_rho_c, '-', \
                     label=text_label)
        elif (y_data == 'pressure'):
            ax.plot (list_r_over_R, list_P_over_P_c, '-', \
                     label=text_label)
        elif (y_data == 'temperature'):
            ax.plot (list_r_over_R, list_theta, '-', \
                     label=text_label)
        ax.legend (loc=(1.02, 0.4))

        # writing file
        if (y_data == 'density'):
            fig.savefig (file_density, dpi=resolution)
        elif (y_data == 'pressure'):
            fig.savefig (file_pressure, dpi=resolution)
        elif (y_data == 'temperature'):
            fig.savefig (file_temperature, dpi=resolution)

plot_polytrope ('density')
plot_polytrope ('pressure')
plot_polytrope ('temperature')
