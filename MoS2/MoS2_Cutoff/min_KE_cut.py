import glob
import re
import numpy as np

# 1) Gather filenames
files = sorted(glob.glob("scf_KE*.txt"))

cutoffs = []
energies = []

# 2) Parse each file for cutoff and total energy
for fname in files:
    m = re.search(r"scf_KE(\d+)\.txt", fname)
    if not m:
        continue
    ke = float(m.group(1))
    with open(fname) as f:
        text = f.read()
    energy_match = re.search(r"Total Energy.*:\s*([-\d\.]+)", text)
    if energy_match:
        e = float(energy_match.group(1))
        cutoffs.append(ke)
        energies.append(e)

# 3) Sort by cutoff
cutoffs = np.array(cutoffs)
energies = np.array(energies)
idx = np.argsort(cutoffs)
cutoffs = cutoffs[idx]
energies = energies[idx]

# 3b) Convert total energies to eV
energies_eV = energies*13.60569312299

# 4) Define convergence threshold (1 meV)
threshold_eV = 0.0015 

# 5) Reference energy at the highest cutoff
E_ref = energies_eV[0]
optimal_cutoff = None


# 6) Find the smallest cutoff where |E - E_ref| <= threshold
for i in range(1,len(cutoffs)):
    diff_En = abs(energies_eV[i] - E_ref)

    if diff_En <= threshold_eV:

        optimal_cutoff = cutoffs[i]
        print(f"Converges @ cutoff = {optimal_cutoff} Ry")
        
        optimal_energy = energies_eV[i]

        optimal_En_diff = diff_En

        break

    else:

        #Update reference energy and proceed
        E_ref = energies_eV[i]

if optimal_cutoff is None:
    print("No kinetic energy cutoff satisfied the 1 meV threshold.")



# 7) Write to output file
with open("min_cutoff.txt", "w") as out:
    out.write(f"Converged cutoff Kinetic Energy: {int(optimal_cutoff)} Ry \n")
    out.write(f"Total Energy at cutoff: {optimal_energy} eV \n")
    out.write(f"Total Energy difference between subsequent KE cutoffs: {optimal_En_diff} eV \n")







