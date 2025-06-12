# Optimization
## This folder contains a basic outline necessary for optimizing your structures in Quantum Espresso.
* Before getting started, as you will see in the Kinetic Energy Cutoff README, the method I outline here is
inefficient and I suggest referring to the 'Co_Bi', 'Co_Mon' or 'MoS2' folders for a much more efficient workflow.

* I will soon explain why this workflow is inefficient, but first, I would like to briefly outline what optimization is
and why we need to optimize our structures in Quantum Espresso. A more detailed explanation can be found in Dr. Duy Le's
Github: https://github.com/zoowe/dlePy/tree/master/TUTORIALS. 

* Ideally, if we had unlimited computational power, optimization wouldn’t be necessary, because we could perform our calculations with parameters that would give us infinite accuracy. 
Of course, that is unrealistic, but we still want really good approximations. One of the parameters that determines the accuracy of our DFT calculations is the kinetic energy cutoff. 
Basically, the cutoff determines the number of modes that we allocate to the electronic wavefunctions. For those who know a little bit about Fourier Analysis, 
essentially, if we have enough Fourier modes, we can theoretically reconstruct any function (in this case, the electronic wavefunction). 

* Similarly, the K-Point analysis seeks to optimize the fineness of grid points used to analyze the reciprocal lattice. Due to the periodicity of the crystal lattice, 
we can approach physical calculations such as diffraction or electronic band structure in reciprocal space, which is the Fourier Transform of real space. 
As we increase the number of k-mesh points, we increase the accuracy with which we sample the reciprocal space (technically, the Brillouin Zone), leading to more accurate electronic structure calculations

* Lattice optimization is simply finding the minimal energy configuration for a variety of lattice constants

## Why this workflow is inefficient, but still useful
* In order to perform any of these optimizations, we need to choose a variety of Energies, k-points, and lattice constants, and perform the DFT calculation.
  The best way to do this would be to wrap them all up in a for loop and submit them to Artemis. In Weeks 1 and 2, I did not know
  how to do this, so I manually edited every file and job script for to have the proper naming convention -- very inefficient.
  In 'Co_Bi', 'Co_Mon' or 'MoS2' folders, I wrap everything up in a nice loop, including job submissions to Artemis. With that said,
  I generally use the scripts I developed here for all my optimizations and one can see the logic begind the optimization process.

  Best of Luck with your optimizations! :)
