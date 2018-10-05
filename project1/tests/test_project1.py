#Test Project 1
import unittest
import pytest
import function1

import numpy as np

#Can't get parser to work...
#class Testref(unittest.TestCase):
    #def test_ref(self):
        #self.parser = NewProj1.ref()
        #parsed = self.parser.parse_args(['--temperature', '300.0','--total_time', '1000.0','--time_step', '0.1','--initial_position', '0.0','--initial_velocity', '0.0','--damping_coefficient', '0.1'])
        #self.assertEqual([parsed.temperature,parsed.total_time, parsed.time_step, parsed.initial_position, parsed.initial_velocity,   parsed.damping_coefficient], [[300.0], [1000.0], [0.1], [0.0], [0.0], [0.1]] )
#if __name__ == '__main__':
    #unittest.main()



class TestNumSteps(unittest.TestCase):
    def test_num_steps(self):
        TotalTime=10
        TimeStep=1
        self.assertEqual(NewProj1.num_steps(TotalTime,TimeStep),10.0)
 

class TestStd(unittest.TestCase):
    def test_std(self):
        self.assertAlmostEqual(NewProj1.std(1,1),1.4142135623730951)
 

class TestRandNumGen(unittest.TestCase):
    def test_rand_rum_gen(self):
        distr=NewProj1.rand_num_gen(0,NewProj1.sigma,10)
        dif_in_means=abs(0-np.mean(distr))
        self.assertLess(abs(0-np.mean(NewProj1.rand_num_gen(0,0.1,10))),.05)
        dif_in_variance=NewProj1.sigma-np.std(distr, ddof=1)
        self.assertLess(dif_in_variance,0.05)



class TestInitialAcceleration(unittest.TestCase):
    def test_initial_acceleration(self):
        distr=[2,1,3]
        self.assertEqual(NewProj1.initial_acceleration(distr),1)
#if __name__ == '__main__':
    #unittest.main()

#class TestParticleMotion(unittest.TestCase):
    #def test_particle_motion(self):
    #    posi=[0]
    #    vel=[1]
    #    acc=[0]
    #    dist=[1,1,1]
    #    Number_Steps=2
    #    NewProj1.particle_motion(Number_Steps)
    #    print(posi)
    #    self.assertEqual(posi,[0,1,2])
#if __name__ == '__main__':
#    unittest.main()


#ewProj1.particle_motion(3)
#print(posi)



def iteration_until_particle_collision_with_wall(runs,Number_Steps,store_place):
    for j in range (0,runs):
        dist=rand_num_gen(0,sigma,Number_Steps)
        place=[]
        for i in range(1, Number_Steps, 1):
            
            vadd=(vel[i-1]+(acc[i-1]*TimeStep))
            vel.append(vadd)
            padd=posi[i-1]+(vel[i-1]*(TimeStep))
            posi.append(padd)
            aadd=(1/mass)*((-gamma*vel[i])+(dist[i]))
            acc.append(aadd)
            if posi[i] <= 0:
                break
            elif posi[i] >= 5.0:
                break
        print("posi")
        print(posi)
        l=len(posi)
        val=l-1
        place.append(val)
        print("place")
        print(place)
        print("val")
        print(val)
        del posi[1:(Number_Steps-1)]
        del vel[1:(Number_Steps-1)]
        del acc[1:(Number_Steps-1)]
        return place,val
    store_placev=place.append
    print("place")
    print(place)
    store_place.append(store_placev)