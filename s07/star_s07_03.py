#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/03/29 09:00:12 (UT+8) daisuke>
#

# importing nuclyr module
import nuclyr.mass

# mass excess of 12C (carbon-12)
massexcess_12C, err_massexcess_12C = nuclyr.mass.massExcess (6, 12)

# printing mass excess of 12C (carbon-12)
print (f'mass excess of 12C =', \
       f'{massexcess_12C:6.3f} +/- {err_massexcess_12C:6.3f} [MeV]')
