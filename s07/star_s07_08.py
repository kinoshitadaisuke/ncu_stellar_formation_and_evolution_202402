#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/03/29 10:15:17 (UT+8) daisuke>
#

#
# specific energy of carbon burning
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

# mass of 1 carbon-12 nucleus
mass_c12 = amu_kg * 12

# printing mass of carbon-12
print (f'mass of carbon-12 nucleus = {mass_c12:g} kg')

# energy generation of carbon burning in Mev
Ec_MeV = 13.0

# energy generation of carbon burning in J
Ec_J = 13.0 * 10**6 * eV_J

# printing energy generation of carbon burning
print (f'energy produced by carbon burning = {Ec_MeV:g} MeV = {Ec_J:g} J')

# specific energy of carbon burning
Ec_J_per_kg = Ec_J / (mass_c12 * 2)

# printing specific energy of carbon burning
print (f'specific energy of carbon burning = {Ec_J_per_kg:g} J kg^-1')
