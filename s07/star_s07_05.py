#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/03/29 09:52:25 (UT+8) daisuke>
#

# importing nuclyr module
import nuclyr.mass

# mass excess of 4He (helium-4)
massexcess_4He, err_massexcess_4He = nuclyr.mass.massExcess (2, 4)

# mass excess of 12C (carbon-12)
massexcess_12C, err_massexcess_12C = nuclyr.mass.massExcess (6, 12)

# mass excess of 16O (oxygen-16)
massexcess_16O, err_massexcess_16O = nuclyr.mass.massExcess (8, 16)

# energy produced by oxygen formation
energy_oxygen = massexcess_4He + massexcess_12C - massexcess_16O

# printing result of calculation
print (f'mass excess of 4He =', \
       f'{massexcess_4He:6.3f} +/- {err_massexcess_4He:6.3f} [MeV]')
print (f'mass excess of 12C =', \
       f'{massexcess_12C:6.3f} +/- {err_massexcess_12C:6.3f} [MeV]')
print (f'mass excess of 16O =', \
       f'{massexcess_16O:6.3f} +/- {err_massexcess_16O:6.3f} [MeV]')
print (f'energy produced by oxygen formation:')
print (f'  E = {massexcess_4He:6.3f} + {massexcess_12C} - ({massexcess_16O:6.3f}) [MeV]')
print (f'    = {massexcess_4He + massexcess_12C:6.3f} - ({massexcess_16O:6.3f}) [MeV]')
print (f'    = {energy_oxygen:6.3f} [MeV]')
