import re
import glob
import os

def extract_parameter(pattern, content, group=1, default="Not found"):
    match = re.search(pattern, content)
    return match.group(group).strip() if match else default

for infile in glob.glob("scf_kp_??.out"):

    m = re.search(r"scf_kp_(\d{2})\.out$", infile)
    #Grab number of grid points from file name
    grid = m.group(1)
    
    # Read the SCF output
    with open(infile, "r") as file:
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
    out_filename = f"scf_kp_{grid}.txt"
    with open(out_filename, "w") as out:
        out.write(f"Number of grid points: {grid}\n")
        for key, val in params.items():
            out.write(f"{key}: {val}\n")

    print(f"Parameters written to {out_filename}")

