# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 11:36:15 2022

@author: Dell
"""
import random
import matplotlib.animation
carry_on = True

class Agent():
        def __init__(self,environment,agents):
            self.y = random.randint(0,99)
            self.x = random.randint(0,99)
            self.environment = environment
            self.agents = agents
            self.store = 0 # We'll come to this in a second.
        def eat(self): # can you make it eat what is left?
            if self.environment[self.y][self.x] > 10:
                self.environment[self.y][self.x] -= 10
                self.store += 10 
        def move(self):
            if random.random() < 0.5:
                self.y = (self.y + 1) % 100
            else:
                self.y = (self.y - 1) % 100
            if random.random() < 0.5:
                self.x = (self.x + 1) % 100
            else:
                self.x = (self.x - 1) % 100
                
        def share_with_neighbours(self, neighbourhood):
            for agent in self.agents:
                 dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                # print("sharing " + str(dist) + " " + str(ave)
        
        def distance_between(self, agent):
            return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
        
        
        
