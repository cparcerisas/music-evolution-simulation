import math, random
import numpy as np 

import rythm
import functions


class Agent:
    def __init__(self, initial_density):
    self.density = initial_density
    self.success_communication = 0
    self.success_repetition = 0


    def learn(self, rythm_list):
        """ Learn the rythm list""" 
        for rythm in rythm_list:
            # Get the rythm density, add it to the agent's density
            # distribution and then normalize it
            for ratio, d in rythm.density():
                if ratio not in self.density.keys():
                    self.density[ratio] = d
                else:
                    self.density[ratio] += d
            
            # NORMALIZE! 


    def create_rythm(self, dev):
        """ Create a rythm. It will use all the rythms it learns combined """
        new_rythm = rythm.Rythm()
        new_rythm.rythm_from_distr(duration, self.density)

        return new_rythm


    def repeat_rythm(self, rythm, dev):
        """ Try to repeat a rythm with a certain deviation """
        return rythm


    def create_rational(self, dev, listerner):
        """ Create a rythm rationally trying to make the listener like it """
        # TO BE IMPLEMENTED
        rythm = []
        return rythm
    

    def punctuate_rythm(self, rythm):
        """ Say how much it has liked it according to what it knows """ 
        # TO BE IMPLEMENTED
        return 0.5

    
    def fitness(self):
        """ Calculate the fitness of an agent and return it """
        # TO BE DECIDED
        return 1

        