# Optimization for a Cobalt Mono-Layer Structure

* Within this directory, you will find three folders, 'Mon_Cutoff', 'Mon_CKP', 'Mon_Latt', which contain scripts necessary
to perform relevant optimizations for the Cobalt mono-layer.

* Each folder contains at least: a job script, denoted by the file tag .sh, and extraction script that extracts the relevant data,
a make script that generates QE input files, a minimizing script that finds the minimum parameter needed for an energy convergence of 1 meV,
and a plotting script to visualize the parameters vs. energy and runtime vs. parameters. A detailed step-by-step description of what
the scripts perform is provided in Python comments within each script.
