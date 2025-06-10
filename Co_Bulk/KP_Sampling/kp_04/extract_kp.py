import re

def extract_parameter(pattern, content, group=1, default="Not found"):
    match = re.search(pattern, content)
    return match.group(group).strip() if match else default

# Read the SCF output
with open("scf_kp_04.out", "r") as file:
    content = file.read()

# Extract Number of k-points, Total Energy, and CPU Runtime

num_k            = extract_parameter(r"number of k points\s*=\s*(\d+)", content)
total_energy       = extract_parameter(r"!\s+total energy\s+=\s+([\d\.\-Ee+]+)", content)
runtime           = extract_parameter( r"PWSCF\s*:\s*([\d\.]+)s\s*CPU", content)

# Pack into a dictionary for efficiency
params = {
    "Number of k-ponts"          : num_k,
    "Total Energy (Ry)"          : total_energy,
    "Run Time (sec)"             : runtime,
}

# Write to text file
with open("scf_kp_04.txt", "w") as out:
    out.write("Number of grid points: 4\n")
    for key, val in params.items():
        out.write(f"{key}: {val}\n")

print("Parameters written to scf_kp_04.txt")

