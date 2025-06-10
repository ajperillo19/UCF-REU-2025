# Kinetic Energy Cutoff Optimization
This directory contains the fundamental steps necessary to perform a 
Kinetic Energy Cutoff Optimization using the Atomic Simulation Environment (ASE) and Quantum Espresso.

Within it you will find two folders: 'EN_20' and 'KE_DA'. EN_** is the naming convention
I utilized to track the Kinetic Energy Cutoff (KEC) I was performing SCF calculations with.

In this case, the '20' refers to a KEC of 20 Rydberg, the standard units used by Quantum Espresso. 

Please look through the files in 'EN_20' and notice fields that contain 'scf_20'.

This is the naming convention I developed my workflow for. 

The naming convention is important if you decide to follow my script. The make files, job files, extraction files, and eventually, 
the plotting scripts parse files with that specific naming convention.

The 'KE_DA' folder performs the bulk of the data analysis for the KEC optimization. 

Within it, you will find 'plot_ke_vs_results.py' and 'min_KE_cut.py'. The plotting script parses through data (txt)
files generated from 'extract_KE.py' with the aforementioned naming convention. Running it should produce two plots: 

"Total Energy vs. KE Cutoff" & "Run Time vs. KE Cutoff". They will also write
to .png files.


***** NOTE *****
The KEC prescription outlined here is an outdated and inefficient way to perform optimization in Quantum Espresso.
I am creating the repository as I go along in my research. Therefore, I am learning as I go.
Look to my 'Co_Bi', 'Co_Mon', and 'MoS2' folders for better ways to perform optimization.
