#trying out input functions
def inputadd():
    q_i=int(input('Enter initial position: '))
    #notice, a numerical input has to be handled
    q=q_i+3
    print(q)
 
#inputadd()

#now I'll try accepting 5 inputs

initial_position=int(input('Enter the starting position'))
velocity=int(input('Enter velocity'))
temperature=float(input('Enter temperature'))
damping_coefficient=int(input('Enter damping coefficient'))

print("Initial Position equals %s, Velocity equals %s, Temperature equals %.2f " %(initial_position,velocity,temperature))

