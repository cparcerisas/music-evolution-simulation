import random
import matplotlib.pyplot as plt
from copy import deepcopy
from IPython.display import set_matplotlib_formats


import population
import rythm


# Set the parameters to the desired values

method = 'replacement'          # method of population. Either 'chain', 'replacement' or 'closed'
initial_rythm_type = 'random'        # either 'optimal' or 'random'
learning = 'sample'             # The type of learning ('map' or 'sample')

mutation_rate = 0.001           # probability of mutation per weight
mutation_max = 1                # maximum value of a random weight

send_weighting = 10             # weighting factor for a send score
receive_weighting = 10          # weighting factor for receive score

duration = 60                   # duration of all the rythms
interactions = 1000             # number of interactions per generation
size_population = 100           # size of population
generations = 100               # number of generations
report_every = 5                # number of generatios between reports

rule = [1, 0, 0, 0]             # learning rule (alpha, beta, gamma, delta)

inhibition = False              # apply lateral inhibition (can be True or False)
communication = False           # speaker tries to avoid ambiguity (can be True or False)


bias = log(0.6)                 # The preference for regular rythms
noise = log(0.05)               # The probability of producing the wrong variant 


def simulation():
    # STILL TO BE DEFINED
    pop = population.Population(size, initial_rythm_type)
    data_accumulator = []
    for i in range(generations + 1):
        if (i % report_every == 0):
            data_accumulator.append(pop.ca_monte_pop(mc_trials))
        pop.produce(population, interactions)
        if method == 'chain':
            pop = population.Population(size, 'random')
            pop.learn(data, interactions)
        if method == 'replacement':
            population.update() 
            pop.learn(data, interactions)
        if method == 'closed':
            pop.learn(data, interactions)

    # Plot the results
            
    return data_accumulator




if __main__ == 'simulation':
    set_matplotlib_formats('svg', 'pdf')
    simulation()
