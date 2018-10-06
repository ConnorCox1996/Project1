#Project 1 
#Import packages: numpy, scipy,& math packages 
import numpy as np
import scipy.constants
import math
import matplotlib.pyplot as plt
#Import argparse
import argparse

# "ref" function parses arguments from command line
#saves input temperature, total time, timestep, intial position & velocity inptuts as variables
def ref():
    #input parameters using argparse
    parser = argparse.ArgumentParser(description='arguments')
    parser.add_argument('-T', '--temperature', metavar='temperature', type=float,  default=1, nargs='?', help=' ')
    parser.add_argument('-tt', '--total_time', metavar='total_time', type=float, default=10, nargs='?', help=' ')
    parser.add_argument('-ts', '--time_step', metavar='time_step', type=float, default=1, nargs='?', help=' ')
    parser.add_argument('-ip','--initial_position', metavar='initial_position', type=float, default=1, nargs='?', help=' ')
    parser.add_argument('-iv', '--initial_velocity', metavar='initial_velocity', type=float, default=1, nargs='?', help=' ')
    parser.add_argument('-d', '--damping_coefficient', metavar='damping_coefficient', type=float, default=1, nargs='?', help=' ')
    
    args = parser.parse_args()
    temperature=args.temperature
    totaltime=args.total_time
    timestep=args.time_step
    initialposition=args.initial_position
    initialvelocity=args.initial_velocity
    gamma=args.damping_coefficient
    
    return temperature,totaltime,timestep,initialposition,initialvelocity,gamma


#Set input values equal to Variables
temperature,totaltime,timestep,initialposition,initialvelocity,gamma=ref()
Temperature=temperature
Gamma=gamma
TimeStep=timestep
TotalTime=totaltime
InitialPosition=initialposition
InitialVelocity=initialvelocity

#num_steps calculates the total number of steps taken 
#calculated from total time and timestep inputs
def num_steps(TotalTime, TimeStep):
        number_steps= TotalTime / TimeStep
        return number_steps
number_Steps=num_steps(TotalTime,TimeStep)
Number_Steps=int(number_Steps)

#Solve for Standard Deviation
#finds Standard deviation, stored as "sigma", from temperature & gamma inputs 
#boltzmann constant is in reduced units, =1
boltzmann_constant=1
#Temperature=int(args.temperature)
def std(Temperature, Gamma):
    sig= math.sqrt(2 * Temperature * Gamma * boltzmann_constant)
    return sig

sigma=std(Temperature,Gamma)

#using the standard deviation calculated above,
#random force is simulated by distribution of normally distributed random numbers
#this distribution models the random force because the standard deviation of the distribution is equal to the
#square root of the variance between random force at time=t & time=t+1
def rand_num_gen(mu, Sigma, Number_Steps):
    xi= np.random.normal(mu, Sigma, Number_Steps)
    return xi

dist=rand_num_gen(0,sigma,Number_Steps)

#The random force can be used in the position, velocity, and acceleration integrator
#Create lists for position & velocity iterations starting with their initial values (@t=0)
#posi=[InitialPosition]
#vel= [InitialVelocity]
#specify mass
mass=1
# Calculate initial acceleration, according to Langevin equation 
def initial_acceleration(distro):
    a0=((1/mass)*((-Gamma*InitialVelocity)+distro[0]))
    return a0
InitialAcceleration=initial_acceleration(dist)
#Create list for acceleration iterations starting with initial acceleration value (@t=0)
#acc=[InitialAcceleration]

#Iterate position, velocity and acceleration at each timestep
#Walls at position of 0 and 5 limit the particle movement
finalpos=[]
def particle_motion(Number_Steps):
    posi=[InitialPosition]
    vel= [InitialVelocity]
    acc=[InitialAcceleration]
    dist=rand_num_gen(0,sigma,Number_Steps)
    for i in range(1, Number_Steps, 1):
        vadd=(vel[i-1]+(acc[i-1]*TimeStep))
        vel.append(vadd)
        padd=posi[i-1]+(vel[i-1]*(TimeStep))
        posi.append(padd)
        aadd=(1/mass)*((-gamma*vel[i])+(dist[i]))
        acc.append(aadd)
        if posi[i] < 0:
            break
        elif posi[i] >= 5.0:
            break
    steps_taken_at_collision=(i*0.1)
  
    return steps_taken_at_collision, posi, vel

#multi-run simulator
#runs the particle_motion function for a specified number of runs
#used when generating a Histogram of the time required for particle to hit a wall
#based on a number of runs
def multi_run_simulator(runs):
    steps_at_collision_for_each_run=[]
    for j in range(runs):
        r=particle_motion(Number_Steps)
        steps_at_collision_for_each_run.append(r[0])
    return steps_at_collision_for_each_run

multrun=multi_run_simulator(100)   

def hist_generator(data):
    bins=[0,0.25,0.5,0.75,1,1.25,1.5,1.75,2.0]
    plt.hist(data, bins)
    plt.xlabel('Time for particle to hit wall')
    plt.ylabel('Number of runs (out of 100 runs total)')
    plt.title("Histogram")
    plt.show()

def write_output(steps_taken_at_collision, posi, vel,TimeStep):
    
    header = "#Index    Time      Position      Velocity"
    #make a text file called "Output"
    Output = open('Output.txt', "w")
    Output.write(header)
    Output.write("\n")
    #except for the header, it writes index,time,position line by line
    
    for i in range(len(posi)):
        Output.write('{}            {:.2f}            {:.2f}              {:.2f}'.format(i, (i*TimeStep), posi[i], vel[i]))
        Output.write('\n')
    Output.close()

#Store variables which are returned from the particle_motion function 
#Call the write_output function, actually write the output
#Call the hit_generator function, actaully generate the histogram
steps_at_collision_for_each_run, posi, vel=particle_motion(Number_Steps)
write_output(steps_at_collision_for_each_run,posi,vel,TimeStep)
test3=hist_generator(multrun)

#Use the list of positions and times returned by the particle_motion function,
#Plot the trajectory of the particle, by plotting particle position vs time *Note: time is assumed to be in seconds, but this is not specified
timelist=range(0,(len(posi)))
plt.plot(timelist,posi)
plt.xlabel("time")
plt.ylabel("particle position")
plt.title("Particle Trajectory")
plt.show()