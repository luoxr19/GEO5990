# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 16:23:56 2022

@author: Dell
"""

import random
import operator
import agentframework
import matplotlib.pyplot
import csv
# import matplotlib.animation 
import matplotlib
matplotlib.use('TkAgg')

import tkinter


environment = []
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    row0 = []
    for value in row:
        row0.append(value)
    environment.append(row0)
# matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show() 
f.close() 


# def distance_between(agents_row_a, agents_row_b):
#     return (((agents_row_a.x - agents_row_b.x)**2) +
#     ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

root = tkinter.Tk()
root.wm_title("Model")

carry_on = True

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

# Make the agents.https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part8/examples/animatedmodel.py
for i in range(num_of_agents):
    # agent_1 = agentframework.Agent()
    # agents.append(agent_1)
    agents.append(agentframework.Agent(environment,agents))


def update(frame_number):
    fig.clear()
    global carry_on
    carry_on = True
    # Move the agents.Plot
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood) 
    # plot
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
    # matplotlib.pyplot.show()
    # Stopping condition
    # if random.random() < 0.1:
    #     carry_on = False
    #     print("stopping condition")
		
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
# animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False)
# animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=100)

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()


# Just showing menu elements
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

tkinter.mainloop()

# for agents_row_a in agents:
#     for agents_row_b in agents:
#         distance = distance_between(agents_row_a, agents_row_b) 
#         print(distance)
