#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/03/29 08:52:57 (UT+8) daisuke>
#

# importing nuclyr module
import nuclyr.mass

# mass excess of 1H (proton)
massexcess_1H, err_massexcess_1H = nuclyr.mass.massExcess (1, 1)

# printing mass excess of 1H (proton)
print (f'mass excess of 1H  =', \
       f'{massexcess_1H:6.3f} +/- {err_massexcess_1H:6.3f} [MeV]')
