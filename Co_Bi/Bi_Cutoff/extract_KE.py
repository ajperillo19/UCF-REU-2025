
import re
import glob
import os

def extract_parameter(pattern, content, group=1, default="Not found"):
    match = re.search(pattern, content, flags=re.MULTILINE)
    return match.group(group).strip() if match else default

# 1) Find all scf_XX.out files (XX = exactly two digits)
for infile in glob.glob("scf_??.out"):
    # 2) Extract the two-digit number from the filename
    m = re.search(r"scf_(\d{2})\.out$", infile)
    if not m:
        continue  # skip anything that doesn't match exactly
    
    cutoff = m.group(1)  # e.g. "20", "25", etc.
    
    # 3) Read the output file
    with open(infile, "r") as f:
        content = f.read()
    
    # 4) Extract Kinetic Energy Cutoff, Total Energy, Runtime
    ecutwfc      = extract_parameter(r"kinetic-energy cutoff\s*=\s*([\d\.]+)", content)
    total_energy = extract_parameter(r"!\s+total energy\s*=\s*([-\d\.Ee]+)", content)
    runtime      = extract_parameter(r"PWSCF\s*:\s*([\d\.]+)s\s*CPU", content)
    
    # 5) Pack into a dictionary
    params = {
        "Kinetic-energy Cutoff (Ry)": ecutwfc,
        "Total Energy (Ry)"         : total_energy,
        "Run Time (sec)"            : runtime,
    }
    
    # 6) Write to scf_KEXX.txt
    outfile = f"scf_KE{cutoff}.txt"
    with open(outfile, "w") as out:
        for key, val in params.items():
            out.write(f"{key}: {val}\n")
    
    print(f"Wrote parameters for cutoff={cutoff} → {outfile}")


