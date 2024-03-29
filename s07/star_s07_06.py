#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/03/29 10:03:42 (UT+8) daisuke>
#

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# files
file_data   = 'binding_energy.data'
file_output = 'binding_energy_025.png'

# lists for storing data
data_x = []
data_y = []
names  = []

# opening data file
with open (file_data, 'r') as fh:
    # reading data file
    for line in fh:
        # splitting line
        list_record    = line.split ()
        # data
        mass_number    = int (list_record[2])
        binding_energy = float (list_record[6])
        isotope_name   = "%s-%s" % (list_record[3], list_record[2])
        # printing data
        print ("%d %f %s" % (mass_number, binding_energy, isotope_name) )
        # appending data to lists
        data_x.append (mass_number)
        data_y.append (binding_energy)
        names.append (isotope_name)

# printing data read
print (f'{data_x}')
print (f'{data_y}')
print (f'{names}')

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel ('Atomic Weight [amu]')
ax.set_ylabel ('Binding Energy per Nucleon [keV]')
ax.set_xlim (1.0, 110.0)
ax.set_ylim (0.0, 9000.0)
ax.set_xticks (range (10, 110, 10) )
ax.grid ()

# making a plot
ax.plot (data_x, data_y, marker='o', markersize=8, \
         color='black', markerfacecolor='blue')
ax.set_xlim (1.0, 25.0)
ax.set_xticks (range (2, 25, 2) )
ax.arrow (4.0, 8800.0, 0.0, -1200.0, length_includes_head=True, width=0.5, \
          head_length=500, color='red')
ax.text (6.0, 8400, r"$\sf {}^4He$", fontsize=24, \
         horizontalalignment='center', verticalalignment='center')
ax.arrow (8.0, 4500.0, 0.0, 1200.0, length_includes_head=True, width=0.5, \
          head_length=500, color='red')
ax.text (8.0, 3700, r"$\sf {}^8Be$", fontsize=24, \
         horizontalalignment='center', verticalalignment='center')
ax.arrow (12.0, 5500.0, 0.0, 1200.0, length_includes_head=True, width=0.5, \
          head_length=500, color='red')
ax.text (12.0, 4700, r"$\sf {}^{12}C$", fontsize=24, \
         horizontalalignment='center', verticalalignment='center')
ax.arrow (16.0, 6000.0, 0.0, 1200.0, length_includes_head=True, width=0.5, \
          head_length=500, color='red')
ax.text (16.0, 5200, r"$\sf {}^{16}O$", fontsize=24, \
         horizontalalignment='center', verticalalignment='center')
fig.savefig (file_output, dpi=150)
