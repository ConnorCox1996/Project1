# Project1

This program takes uses the Langevin equation to model the position, velocity and acceleration of a particle in 1-dimension. The 1 dimensional position of the particle is limited by walls present at positions of 0 & 5.
The model considers a particle immersesed in a fluid of smaller particless, where the position, velocity, and acceleration of that considered particle  cahanges due to Brownian Motion.

To Use the Program:
Input the Temperature, Total Time, Timestep, Initial Position, Initial Velocity, & Damping Coefficient with in the following format:
-T 1 -tt 1 -ts 1 -ip 0 -iv 1 -d 0.1

based on the input temperature (-T), total time (-tt), timestep (-ts), initial position (-ip), initial velocity (-ip) and damping coefficient (-d)
particle motion will be modeled.

The model will be run 100 times, and  a histogram will be produced, displaying the time it took for teh particle to hit one of the walls.
Particle trajectory will be plotted for one run of the model, displaying particle position vs. time
