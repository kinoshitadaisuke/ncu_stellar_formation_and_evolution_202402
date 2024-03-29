#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/03/29 10:15:42 (UT+8) daisuke>
#

#
# energy of photons produced by annihilation of electron and positron
#

# importing scipy module
import scipy.constants

# speed of light
c = scipy.constants.c

# Planck constant
h = scipy.constants.h

# mass of electron
m_e = scipy.constants.m_e

# electron volt
eV_name = 'electron volt'
eV_J    = scipy.constants.physical_constants[eV_name][0]

# printing speed of light in vacuum
print (f'speec of light in vacuum = {c:g} m/s')

# printing Planck constant
print (f'Planck constant = {h:g} J Hz^-1')

# printing electron mass in kg
print (f'1 electron mass = {m_e:g} kg')

# energy of 1 eV in J
print (f'1 eV  = {eV_J:g} J')

# energy produced by annihilation of electron and positron in J
E2_J = 2 * m_e * c**2

# energy of a photon created by annihilation of electron and positron in J
E1_J = E2_J / 2

# energy of a photon created by annihilation of electron and positron in eV
E1_eV = E1_J / eV_J
E1_kev = E1_eV / 10**3

# printing energy of a photon created by annihilation of electron and positron
print (f'E_photon  = {E1_eV:g} eV')
print (f'          = {E1_kev:g} keV')

# frequency of a photon created by annihilation of electron and positron
nu1 = E1_J / h

# printing freq. of a photon created by annihilation of electron and positron
print (f'nu_photon = {nu1:g} Hz')

# wavelength of a photon created by annihilation of electron and positron
lambda1 = c / nu1

# printing wl of a photon created by annihilation of electron and positron
print (f'wl_photon = {lambda1:g} m')

