import glob
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# 1) Gather filenames
files = sorted(glob.glob("scf_A_*.txt"))


latt_params = []
energies = []


# 2) Parse each file
for fname in files:

    with open(fname) as f:
        text = f.read()
    # extract Total Energy
    e = float(re.search(r"Total Energy.*:\s*([-\d\.]+)", text).group(1))
    # extract lattice parameters
    a = float(re.search(r"Lattice Parameter.*:\s*([-\d\.]+)", text).group(1))

    # append elements to appropriate arrays
    latt_params.append(a)
    energies.append(e)
    

# 3) Sort by number of grid points
idx = np.argsort(latt_params)
energies = np.array(energies)[idx]


# 3b) Convert 'energies' to ev to determine minimum threshold
# Minimum cutoff calculations will be done in 'min_A_cut.py'


energies_eV = energies*13.60569312299

energies_keV = energies_eV/1000

#3c) Convert lattice parameters in Bohr units to Angstrom
latt_params_arr = np.array(latt_params)
latt_params_Ang = latt_params_arr/1.88973

#WE WILL NEED THIS STEP TO DETERMINE THE OPTIMIZED LATTICE PARAMETER USING THE EQUATION OF STATES IN A SEPARATE FILE. THIS CAN BE DONE IN ANOTHER SCRIPT BUT FOR CONVENIENCE, I WILL DO IT HERE. ALL I AM DOING IS PRINTING THE LATTICE PARAMETERS AND CORRESPONDING ENERGY ARRAYS TO A 2 COLUMN TABULATED DATA FILE

with open('./Data_A.txt', 'w') as file:
    file.write('Lattice Parameter\tEnergy\n')

    for i in range(len(latt_params_arr)):
        file.write(f'{latt_params_Ang[i]}\t{energies_eV[i]}\n')


# 4) Plot Total Energy vs Lattice Parameters: Save as png
plt.figure()
plt.plot(latt_params_Ang, energies_keV,"o-", linewidth=1.5)

#Format graph for aesthetic purposes by removing default scientific notation in MATPLOTLIB
ax = plt.gca()
ax.yaxis.set_major_formatter(mticker.ScalarFormatter(useOffset=False, useMathText=False))
ax.ticklabel_format(style='plain', axis='y')

plt.xlabel("Lattice Parameters (Å)")
plt.ylabel("Total Energy (keV)")
plt.title("Total Energy vs. Lattice Parameters")
plt.grid(True)
plt.tight_layout()
plt.savefig("energy_vs_Lp.png")



#5) Show figures
plt.show()

