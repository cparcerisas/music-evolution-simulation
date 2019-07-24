import math 
import numpy as np 

import agent 

class self.agents:
    def __init__(self, size, initial_rythm_type):
        """ Create a self.agents with N agents """
        self.agents = []
        self.N = size
        self.initial_rythm = initial_rythm_type

        for i in range(N):
            self.agents.append(agent.Agent())
        
    
    def replace(self):
        """ Get and old man replaced by a baby """
        n = random.uniform(N)
        self.agents[n] = agent.Agent()


    def update(self.agents):
        """ Update the self.agents """
        # Random speaker and hearer
        speaker_index = random.randrange(self.N)
        hearer_index = random.randrange(self.N - 1)
        if hearer_index >= speaker_index: 
            hearer_index += 1
        speaker = self.agents[speaker_index]
        hearer = self.agents[hearer_index]

        # Initialize a random rythm 
        rythm = rythm.Rythm()
        rythm.random_rythm()

        # Make a random speaker teach the rythm to a random hearer
        success = self.communicate(speaker, hearer, meaning)
        speaker[2][0] += success
        speaker[2][1] += 1
        hearer[2][2] += success
        hearer[2][3] += 1
        return success


    def communicate(self, speaker, hearer, rythm=None, dev=0.1):
        """ Make speaker teach hearer. If rythm is None then create it (Composer!) """
        if rythm == None: 
            speaker_rythm = speaker.create_rythm(dev)
        else:
            speaker_rythm = speaker.repeat_rythm(rythm, dev)

        hearer_rythm = hearer.repeat_rythm(speaker_rythm, dev)

        if hearer_rythm.is_equal_to(speaker_rythm):
            return 1
        else:
            return 0
    

    def next_generation(self):
        """ Get to the next generation """
        new_p = []
        sum_f = self.sum_fitness()
        for i in range(self.N):
            parent = pick_parent(self.agents, sum_f)
            child_production_system = deepcopy(parent[0])
            child_reception_system = deepcopy(parent[1])
            mutate(child_production_system)
            mutate(child_reception_system)
            child=[child_production_system,
                child_reception_system,
                [0., 0., 0., 0.]]
            new_p.append(child)


    def learn(self, data, no_learning_episodes):
        # TO DEFINE
        for n in range(no_learning_episodes):
            ms_pair = random.choice(data)
            learn(random.choice(self.agents), ms_pair[0], ms_pair[1])


    def produce(self, no_productions):
        # TO DEFINE
        ms_pairs = []
        for n in range(no_productions):
            speaker = random.choice(self.agents)
            meaning = random.randrange(len(speaker))
            signal = wta(speaker[meaning])
            ms_pairs.append([meaning, signal])  
        return ms_pairs


    def sum_fitness(self):
        """ Return the fitness of the self.agents (sum) """
        total = 0
        for agent in self.agents:
            total += self.agents.fitness()
        return total


    def ca_monte_pop(self, trials):
        total = 0.
        for n in range(trials):
            speaker = random.choice(self.agents)
            hearer = random.choice(self.agents)
            total += communicate(speaker, hearer, random.randrange(len(speaker)))
        return total / trials


    # def random_self.agents(size):
    #     self.agents = []
    #     for i in range(size):
    #         self.agents.append([random_system(meanings, signals),
    #                         random_system(signals, meanings),
    #                         [0., 0., 0., 0.]])
    #     return self.agents