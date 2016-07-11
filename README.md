################################################################################################################
################################################################################################################
########################################### McGill Physics Hackathon ###########################################
###########################################  2D Quantum Simulation   ###########################################
################################################################################################################
################################################################################################################

Version:    1.0.0
Date:       July 10, 2016
Autors:     Lennart Doöppenschmitt and Yuan Yao


In classical mechanics everything about the particle is known once we solve to the trajectory of the particle using Newton's equations. in the quantum world (which is the correct model whereas newton's is just an approximation) this picture is false. we solve for a wave equation, the amplitude of the wave at certain point represents the probability of finding the particle at said point. This is a significant conceptional difference to a point-like particle in classical mechanics, since we are not familiar with the notion of a particle being probably here, but maybe over there. Hence the equation that governs the behaviour of the wave equation is quite different and does not bode well with our intuition. Here we try to use plots to illustrate some of these counterintuitive properties of the schrodinger equation.

We numerically solve the 2 dimension Schroedinger equation with the Fourier method (or also called splitstep). As a spectral method it is much better than time stepping. We start with different potentials and initial states. the time evolution of each potential is recorded in Youtube videos, the potential is shown in the photos with the same name. We include both scattering and bound states, and try to simulate realistic atomic models. For example the central potential bound state simulates the time evolution of polarized electron, whereas the double potential simulates a molecular bond. Similar things can be said about our scattering models, since classically a particle can't be split this way.
Due to its remarkable stability (after 2000 iterations sometimes the norm of wave function is the same up to 10**-7). The next step is to further understand these solutions, start with different initial conditions and look more carefully at the accuracy of the model (which we expect to be good). We use this program as a guide to build our understanding of the quantum world.
We could run simulations with finer a mesh, however the current simulations are starting to reach our upper bound of comupational (speed/memory) limits of our laptops. we could use better computers for further simulations and or optimize the code more which we did not have the time to do this event. (numba, C++, GPU computations).
I learned to not leave uploading to last minute my hands are shaking. 
We used a powerful technique, which we learned, and hope to have more opportunities to play around with it, further possibilities are endless.

IMPORTANT: in the github link we specialize in the 2D cases. 1D was written mostly for trial. in the folder for 2D case the files are exactly the python files.
