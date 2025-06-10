#!/bin/bash
#SBATCH --job-name=ecut_scf
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --time=10:00:00
#SBATCH --error=%A_%a.err
#SBATCH --output=%A_%a.out
#SBATCH --array=0-12       # indices 0 through 12 (13 tasks total)

# 1) Define your list of cutoffs in the same order as --array indices:
Latt_Values=(3.12 3.13 3.14 3.15 3.16 3.17 3.18 3.19 3.20 3.21 3.22 3.23 3.24)

# 2) Pick the correct cutoff based on the array task ID
latt=${Latt_Values[$SLURM_ARRAY_TASK_ID]}

# 3) Load modules and set up environment
module purge
module load qe/7.2
export OMP_NUM_THREADS=1

# 4) Build the input/output filenames
 
latt_str=$latt
input_file="scf_A_${latt_str}.inp"
output_file="scf_A_${latt_str}.out"

# 5) Run pw.x for this cutoff
mpirun pw.x < $input_file > $output_file

