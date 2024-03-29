#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2024/03/29 08:54:28 (UT+8) daisuke>
#

# importing nuclyr module
import nuclyr.mass

# mass excess of 1H (proton)
massexcess_1H, err_massexcess_1H = nuclyr.mass.massExcess (1, 1)

# printing mass excess of 1H (proton)
print (f'mass excess of 1H  =', \
       f'{massexcess_1H:6.3f} +/- {err_massexcess_1H:6.3f} [MeV]')

# mass excess of 4He (helium-4)
massexcess_4He, err_massexcess_4He = nuclyr.mass.massExcess (2, 4)

# printing mass excess of 4He (helium-4)
print (f'mass excess of 4He =', \
       f'{massexcess_4He:6.3f} +/- {err_massexcess_4He:6.3f} [MeV]')

# energy produced by p-p chain
energy_ppchain = massexcess_1H * 4 - massexcess_4He

# printing result of calculation
print (f'energy produced by p-p chain:')
print (f'  E = {massexcess_1H:6.3f} x 4 - {massexcess_4He:6.3f} [MeV]')
print (f'    = {massexcess_1H * 4:6.3f} - {massexcess_4He:6.3f} [MeV]')
print (f'    = {energy_ppchain:6.3f} [MeV]')
