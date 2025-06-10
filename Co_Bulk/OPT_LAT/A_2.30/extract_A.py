import re

def extract_parameter(pattern, content, group=1, default="Not found"):
    match = re.search(pattern, content)
    return match.group(group).strip() if match else default

# Read the SCF output
with open("scf_A_230.out", "r") as file:
    content = file.read()

# Extract Number of k-points, Total Energy, and CPU Runtime

latt_param       = extract_parameter(r"""lattice\s+parameter\s+\(alat\)\s*=\s*([-+]?\d*\.?\d+(?:[Ee][+-]?\d+)?)\s*a\.u\.""", content)
total_energy     = extract_parameter(r"!\s+total energy\s+=\s+([\d\.\-Ee+]+)", content)
runtime          = extract_parameter( r"PWSCF\s*:\s*([\d\.]+)s\s*CPU", content)

#Note: The lattice parameter object is printed to the output file in units of Bohr Radius by default. With that said, let's wait to do the conversion until we develop our graphing scripts. Alternatively, I believe one could edit their input file script to output the lattice parameter in Angstrom, or manually input their lattice parameter in desired units to their data file


# Pack into a dictionary for efficiency
params = {
    "Lattice Parameter (Bohr)"   : latt_param ,
    "Total Energy (Ry)"          : total_energy,
    "Run Time (sec)"             : runtime,
}


# Write to text file
with open("scf_A_230.txt", "w") as out:
    
    for key, val in params.items():
        out.write(f"{key}: {val}\n")

print("Parameters written to scf_A_230.txt")

