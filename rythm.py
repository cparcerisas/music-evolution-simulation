import math 
import numpy as np


class Rythm:
    def __init__(self):
        self.IOIs = []
        self.intensity = []

    
    def density(self):
        """ Return the density (IOI / its adjacentss) ratio """ 
        density = {}
        for i in range(len(self.IOIs)):
            # Compute the mean of the ratio with the adjacent values
            if i == 0:
                ratio = self.IOIs[i+1]/self.IOIs[i]
            elif i == len(self.IOIs):
                ratio = self.IOIs[i-1]/self.IOIs[i]
            else:
                ratio = (self.IOIs[i-1]/self.IOIs[i] + self.IOIs[i+1]/self.IOIs[i]) / 2

            ratio = round(ratio, 2)
            if ratio not in density.keys():
                density[ratio] = 1
            else:
                density[ratio] += 1

        return density

    
    def random_rythm(self, duration, mean, dev):
        """ Create a random rythm """ 
        self.IOIs = []
        recorded = 0
        while recorded < duration:
            IOI = random.uniform(dev)
            i = random.uniform(dev)
            self.IOIs.append(IOI)
            self.intensity.append(i)
            recorded += IOI


    def rythm_from_distr(self, duration, distr):
        """ Create a rythm from a distribution pattern """ 
        self.IOIs = []
        recorded = 0
        while recorded < duration: 
            # Get a one of the IOIs using a random selector according to probablity (roulette?)
            IOI = 1
            i = random.uniform(dev)
            self.IOIs.append(IOI)
            self.intensity.append(i)
            recorded += IOI


    def G(self):
        """ Calculate the modified entropy """ 
        # TO BE DEFINED
        return np.mean(self.IOIs)

    
    def is_equal_to(self, rythm, dev):
        """ Evaluate if the two rythms are the same with a certain dev """
        if np.sum(self.IOIs - rythm.IOIs) > dev:
            return False
        else:
            return True
