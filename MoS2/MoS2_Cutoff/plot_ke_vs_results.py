import glob
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# 1) Gather filenames
files = sorted(glob.glob("scf_KE*.txt"))

cutoffs = []
energies = []
runtimes = []

# 2) Parse each file
for fname in files:
    # extract the number after "KE" in the filename
    m = re.search(r"scf_KE(\d+)\.txt", fname)
    if not m:
        continue
    ke = float(m.group(1))
    with open(fname) as f:
        text = f.read()
    # extract Total Energy
    e = float(re.search(r"Total Energy.*:\s*([-\d\.]+)", text).group(1))
    # extract Run Time
    rt = float(re.search(r"Run Time.*:\s*([\d\.]+)", text).group(1))
    cutoffs.append(ke)
    energies.append(e)
    runtimes.append(rt)

# 3) Sort by cutoff
idx = np.argsort(cutoffs)
cutoffs = np.array(cutoffs)[idx]
energies = np.array(energies)[idx]
runtimes = np.array(runtimes)[idx]

# 3b) Convert 'energies' to ev to determine minimum threshold
# Minimum cutoff calculations will be done in 'min_KE_cut.py'


energies_eV = energies*13.60569312299
energies_keV = energies_eV/1000
print(energies_eV)
# 4a) Plot Total Energy vs Cutoff: Save as png
plt.figure()
plt.plot(cutoffs, energies_keV, "o-", linewidth=1.5)

ax = plt.gca()
ax.yaxis.set_major_formatter(mticker.ScalarFormatter(useOffset=False, useMathText=False))
ax.ticklabel_format(style='plain', axis='y')

plt.xlabel("Kinetic‐energy Cutoff (Ry)")
plt.ylabel("Total Energy (keV)")
plt.title("Total Energy vs. KE Cutoff")
plt.grid(True)
plt.tight_layout()
plt.savefig("energy_vs_ke.png")

# 4b) Plot Run Time vs Cutoff: Save as png
plt.figure()
plt.plot(cutoffs, runtimes, "s--", linewidth=1.5)
plt.xlabel("Kinetic‐energy Cutoff (Ry)")
plt.ylabel("Run Time (s)")
plt.title("Run Time vs. KE Cutoff")
plt.grid(True)
plt.tight_layout()
plt.savefig("runtime_vs_ke.png")

#5) Show figures
plt.show()

