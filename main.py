# -*- coding: utf-8 -*-
"""
GreenChinchilla
Name: Harsh Nagarkar
date last edit:- 5/8/2017
Cite: https://stackoverflow.com/questions/14931769/how-to-get-all-combination-of-n-binary-value this site to generate possiblities
Working:- Driver.py contains generating possiblities and solving them
combination.py has my dfs algorithm to scan through maze and return true or false based on outcome
"""

from __future__ import division
import neuro
import random
inputs = []
targets = []

#opening File
file1 = open("data.csv","r")
file2 = open("results.csv","r")

file1 = file1.read()
file2 = file2.read()

file1= file1.split("\n")
file2 = file2.split("\n")

#Getting random 30,00 data mazes from data.csv and corresponding solutions from results.csv and appending
print type(file1[0])
print float(list(file1[0].split(",")[0])[1])
for i in  range(0,30000):
    index = random.randint(0,2**25)
    temp1 = file1[index].split(",")
    matrix = [float(list(temp1[0])[1]),float(list(temp1[1])[1]),float(list(temp1[2])[1]),float(list(temp1[3])[1]),float(list(temp1[4])[1]),
              float(list(temp1[5])[1]),float(list(temp1[6])[1]),float(list(temp1[7])[1]),float(list(temp1[8])[1]),float(list(temp1[9])[1]),
              float(list(temp1[10])[1]),float(list(temp1[11])[1]),float(list(temp1[12])[1]),float(list(temp1[13])[1]),float(list(temp1[14])[1]),
              float(list(temp1[15])[1]),float(list(temp1[16])[1]),float(list(temp1[17])[1]),float(list(temp1[18])[1]),float(list(temp1[19])[1]),
              float(list(temp1[20])[1]),float(list(temp1[21])[1]),float(list(temp1[22])[1]),float(list(temp1[23])[1]),float(list(temp1[24])[1])]
    inputs.append(matrix)  
    targets.append([float(list(file2[index])[1])])
    
reps=1000
network=[] #makes an empty list to contain the neural net
#sets up the network to accommodate the size of your inputs
network=neuro.setup_network(inputs)
#trains the network for some number of repetitions on your
#training input and targets
neuro.train(network, inputs, targets, reps)
neuro.writeNetworkToFile("myNetwork.net", network)

