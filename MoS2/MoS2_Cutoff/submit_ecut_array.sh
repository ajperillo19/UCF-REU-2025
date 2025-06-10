#!/bin/bash
#SBATCH --job-name=ecut_scf
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --time=10:00:00
#SBATCH --error=%A_%a.err
#SBATCH --output=%A_%a.out
#SBATCH --array=0-12       # indices 0 through 12 (13 tasks total)

# 1) Define your list of cutoffs in the same order as --array indices:
Cut_Values=(35 40 45 50 55 60 65 70 75 80 85 90 95)

# 2) Pick the correct cutoff based on the array task ID
ecut=${Cut_Values[$SLURM_ARRAY_TASK_ID]}

# 3) Load modules and set up environment
module purge
module load qe/7.2
export OMP_NUM_THREADS=1

# 4) Build the input/output filenames
#    Note: zero-pad to two digits if needed (e.g. 05, 20, 80)
ecut_str=$(printf "%02d" $ecut)
input_file="scf_${ecut_str}.inp"
output_file="scf_${ecut_str}.out"

# 5) Run pw.x for this cutoff
mpirun pw.x < $input_file > $output_file

