import re

def extract_parameter(pattern, content, group=1, default="Not found"):
    match = re.search(pattern, content)
    return match.group(group).strip() if match else default

# Read the SCF output
with open("scf_20.out", "r") as file:
    content = file.read()

# Extract Kinetic Energy cutoff, Total Energy, and CPU Runtime

ecutwfc            = extract_parameter(r"kinetic-energy cutoff\s+=\s+([\d.]+)", content)
total_energy       = extract_parameter(r"!\s+total energy\s+=\s+([\d\.\-Ee+]+)", content)
runtime           = extract_parameter( r"PWSCF\s*:\s*([\d\.]+)s\s*CPU", content)

# Pack into a dictionary for efficiency
params = {
    "Kinetic-energy Cutoff (Ry)" : ecutwfc,
    "Total Energy (Ry)"          : total_energy,
    "Run Time (sec)"             : runtime,
}

# Write to text file
with open("scf_KE20.txt", "w") as out:
    for key, val in params.items():
        out.write(f"{key}: {val}\n")

print("Parameters written to scf_KE20.txt")

