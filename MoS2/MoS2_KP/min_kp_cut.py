import glob
import re
import numpy as np

# 1) Gather filenames
files = sorted(glob.glob("scf_kp_*.txt"))

num_grid = []
energies = []

# 2) Parse each file for number of grid points  and total energy
for fname in files:
    
    with open(fname) as f:
        text = f.read()
    energy_match = re.search(r"Total Energy.*:\s*([-\d\.]+)", text)
    grid_count = re.search(r"Number of grid points.*:\s*([-\d\.]+)", text)
    
    if energy_match:
        e = float(energy_match.group(1))
        gc = float(grid_count.group(1))

        num_grid.append(gc)
        energies.append(e)

# 3) Sort by cutoff
num_grid = np.array(num_grid)
energies = np.array(energies)
idx = np.argsort(num_grid)

num_grid = num_grid[idx]
energies = energies[idx]

# 3b) Convert total energies to eV
energies_eV = energies*13.60569312299

# 4) Define convergence threshold (1 meV)
threshold_eV = 0.001 

# 5) Reference energy at the highest cutoff
E_ref = energies_eV[0]
optimal_cutoff = None


# 6) Find the smallest cutoff where |E - E_ref| <= threshold
for i in range(1,len(num_grid)):
    diff_En = abs(energies_eV[i] - E_ref)

    if diff_En <= threshold_eV:

        optimal_cutoff = num_grid[i]
        print(f"Converges @ cutoff = {optimal_cutoff} points")
        
        optimal_energy = energies_eV[i]

        optimal_En_diff = diff_En

        break

    else:

        #Update reference energy and proceed
        E_ref = energies_eV[i]

if optimal_cutoff is None:
    print("No kinetic energy cutoff satisfied the 1 meV threshold.")




# 7) Write to output file
with open("min_k_cutoff.txt", "w") as out:
    out.write(f"Converged cutoff @: {int(optimal_cutoff)} points \n")
    out.write(f"Total Energy at cutoff: {optimal_energy} eV \n")
    out.write(f"Total Energy difference between subsequent grid point cutoffs: {optimal_En_diff} eV \n")







