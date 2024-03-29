#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/03/29 10:15:35 (UT+8) daisuke>
#

#
# specific energy of oxygen burning
#

# importing scipy module
import scipy.constants

# atomic mass unit
amu_name = 'atomic mass unit-kilogram relationship'
amu_kg   = scipy.constants.physical_constants[amu_name][0]

# electron volt
eV_name = 'electron volt'
eV_J    = scipy.constants.physical_constants[eV_name][0]

# printing 1 amu in kg
print (f'1 amu = {amu_kg:g} kg')

# energy of 1 eV in J
print (f'1 eV  = {eV_J:g} J')

# mass of 1 oxygen-16 nucleus
mass_o16 = amu_kg * 15.9949

# printing mass of carbon-12
print (f'mass of oxygen-16 nucleus = {mass_o16:g} kg')

# energy generation of oxygen burning in Mev
Eo_MeV = 16.0

# energy generation of oxygen burning in J
Eo_J = 16.0 * 10**6 * eV_J

# printing energy generation of oxygen burning
print (f'energy produced by oxygen burning = {Eo_MeV:g} MeV = {Eo_J:g} J')

# specific energy of oxygen burning
Eo_J_per_kg = Eo_J / (mass_o16 * 2)

# printing specific energy of oxygen burning
print (f'specific energy of oxygen burning = {Eo_J_per_kg:g} J kg^-1')
