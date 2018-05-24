from __future__ import division
import neuro
import mazey
import pandas as pd
import numpy as np
import time
##training inputs and their respective target
#t1 = time.time()
inputs=[]
targets=[]
df1 = pd.read_csv("data.csv",header=None,nrows=10000)
df2 = pd.read_csv("results.csv",header=None,nrows=10000)

for i in range(0,len(df1.index)):
    ins = df1.iloc[[i]].values
    ins = np.asfarray(ins,float)
    ins = ins.tolist()
    ins = ins[0]
    inputs.append(ins)
    ins = df2.iloc[[i]].values
    ins = np.asfarray(ins,float)
    ins = ins.tolist()
    ins = ins[0]
#    print type(ins)
    targets.append(ins)
#print targets
#for i in range(0,5000):
#    inputs.append(mazey.geneticmatrix())
#    targets.append([1])
#    inputs.append(mazey.openmaze(5,5))
#    targets.append([1])
#    inputs.append(mazey.kindaopenmaze(5,5))
#    targets.append([1])
#    inputs.append(mazey.notmaze())
#    targets.append([0])
#    inputs.append(mazey.maze(5,5))
#    targets.append([0])
##print inputs
#    targets= [[1],[1],[1],[0],[0]]
#number of repetitions to train the network
reps=30
network=[] #makes an empty list to contain the neural net
#sets up the network to accommodate the size of your inputs
network=neuro.setup_network(inputs)
#trains the network for some number of repetitions on your
#training input and targets
neuro.train(network, inputs, targets, reps)
neuro.writeNetworkToFile("myNetwork.net", network)

#t2=time.time()
#total = t2-t1
#
#print "total time required was ",total," secs"