import re
import glob
import os

def extract_parameter(pattern, content, group=1, default="Not found"):
    match = re.search(pattern, content)
    return match.group(group).strip() if match else default

# 1) Find all scf_A_3.??.out files (?? = exactly two digits)
for infile in glob.glob("scf_A_3.??.out"):
    # 2) Extract the two-digit number from the filename
    m = re.search(r"scf_A_3.(\d{2})\.out$", infile)
    if not m:
        continue  # skip anything that doesn't match exactly

    cutoff = m.group(1)  # e.g. "18", "20", etc.

    # Read the SCF output
    with open(infile, "r") as file:
        content = file.read()

    # Extract lattice parameter, Total Energy, and CPU Runtime

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

    outfile = f"scf_{latt_param}.txt"
    with open(outfile, "w") as out:
    
        for key, val in params.items():
            out.write(f"{key}: {val}\n")

        print(f"Parameters written to {outfile}")

