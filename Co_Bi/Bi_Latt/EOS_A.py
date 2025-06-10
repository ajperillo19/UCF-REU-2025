from ase.eos import calculate_eos
from ase.eos import EquationOfState
from ase.units import kJ
import numpy as np

# 1) Load Data and retrieve the lattice parameters and energy
data = np.loadtxt('Data_A.txt', skiprows = 1, delimiter = '\t')

latt_params = data[ :, 0]
energies = data[ :, 1]

# 2) Perform EOS fitting calculation using ASE Libraries
volumes = latt_params**3
eos = EquationOfState(volumes, energies)

v0, e0, B = eos.fit()

#2b) Compute the optimizes lattice constant from EOS volume
a0 = v0**(1/3)

#Convert Bulk Modulus to SI units
B_GPa = B / kJ *1.0e24

#Convert all values into strings to be written out to a text file
B_GPa_str = str(B_GPa)
v0_str = str(v0)
e0_str = str(e0)
a0_str = str(a0)

# Pack into a dictionary for efficiency
params = {
    "Optimal Volume (Å³)"          : v0_str,
    "Total Energy (eV)"            : e0_str,
    "Bulk Modulus (GPa)"           : B_GPa_str,
    "Optimal lattice constant (Å)" : a0_str,
}

# Write to text file
with open("Optml_params.txt", "w") as out:
    
    for key, val in params.items():
        out.write(f"{key}: {val}\n")
print('Optimal parameters written to: Optml_params.txt')
