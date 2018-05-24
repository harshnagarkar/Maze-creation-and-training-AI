import numpy
import numpy as np
from numpy.random import random_integers as rand
import matplotlib.pyplot as pyplot
import random

def notmaze():
    matrix = []
    for i in range(0,5):
        matrix.append([])
        for j in range(0,5):
            matrix[i].append(float(random.randint(0,1)))
    chk = random.choice([0,1,2])
    if chk == 0:
        matrix[0][0]= float(1)    
        matrix[4][4] = float(0)
    elif chk == 1:
        matrix[0][0]= float(0)    
        matrix[4][4] = float(1)
    else:
        matrix[0][0]= float(1)    
        matrix[4][4] = float(1)     
        
    choice=[[0,1],[0,2],[0,3],[0,4],[1,0],[2,0],[3,0],[4,0],[4,1],[4,2],[4,3],[1,4],[2,4],[3,4]]
    for n in choice:
        matrix[n[0]][n[1]] = random.randint(0,1)
#    print matrix
#    print matrix
    maze = []
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            maze.append(matrix[i][j])
    
    return maze


#com = random.random()
#den = random.random()
def maze(width=5, height=5, complexity=random.random(), density=random.random()):
    # Only odd shapes
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1])))
    density    = int(density * ((shape[0] // 2) * (shape[1] // 2)))
    # Build actual maze
    Z = numpy.zeros(shape, dtype=int)
    # Fill borders
    Z[0, :] = Z[-1, :] = 1
    Z[:, 0] = Z[:, -1] = 1
    # Make aisles
    for i in range(density):
        x, y = random.randint(0, shape[1] // 2) * 2, random.randint(0, shape[0] // 2) * 2
        Z[y, x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_,x_ = neighbours[random.randint(0, len(neighbours) - 1)]
                if Z[y_, x_] == 0:
                    Z[y_, x_] = 1
                    Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                    x, y = x_, y_               
#    mazerandom = maze(5, 5)
#    print Z
    mazes = []
    for i in range(0,len(Z)):
        for j in range(0,len(Z)):
            mazes.append(float(Z[i][j]))
    return mazes

def  trickymazey(width=5, height=5, complexity=random.random(), density=random.random()):
    matrix = []
    for i in range(0,5):
        matrix.append([])
        for j in range(0,5):
            matrix[i].append(1)
    list1=[0,1,2,3,4]
    list2=[0,1,2,3,4]
    
    choice=[[0,1],[0,2],[0,3],[0,4],[1,0],[2,0],[3,0],[4,0],[4,1],[4,2],[4,3],[1,4],[2,4],[3,4],[4,4],[0,0]]
    
    for cho in choice:
        matrix[cho[0]][cho[1]]=random.randint(0,1)
#    print matrix
    mazes = []
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            mazes.append(float(matrix[i][j]))
    return mazes
    
trickymazey(5,5)
def openmaze(width=5, height=5, complexity=round(random.uniform(0.2, 0.9)), density=random.uniform(0.5, 0.9)):
    # Only odd shapes
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1])))
    density    = int(density * ((shape[0] // 2) * (shape[1] // 2)))
    # Build actual maze
    Z = numpy.zeros(shape, dtype=int)
    # Fill borders
    Z[0, :] = Z[-1, :] = 1
    Z[:, 0] = Z[:, -1] = 1
    # Make aisles
    for i in range(density):
        x, y = random.randint(0, shape[1] // 2) * 2, random.randint(0, shape[0] // 2) * 2
        Z[y, x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_,x_ = neighbours[random.randint(0, len(neighbours) - 1)]
                if Z[y_, x_] == 0:
                    Z[y_, x_] = 1
                    Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                    x, y = x_, y_    
    choice=[[0,0],[0,1],[0,2],[0,3],[0,4],[1,0],[2,0],[3,0],[4,0],[4,1],[4,2],[4,3],[4,4],[1,4],[2,4],[3,4]]
    for n in choice:
        Z[n[0]][n[1]] = 0
    mazes = []
    for i in range(0,len(Z)):
        for j in range(0,len(Z)):
            mazes.append(float(Z[i][j]))
    return mazes
#print openmaze(5,5)

#def trickymaze():
#    mazes = notmaze()
#    print mazes

#trickymaze()
def kindaopenmaze(width=5, height=5, complexity=round(random.uniform(0.2, 0.9)), density=random.uniform(0.5, 0.9)):
    # Only odd shapes
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1])))
    density    = int(density * ((shape[0] // 2) * (shape[1] // 2)))
    # Build actual maze
    Z = numpy.zeros(shape, dtype=int)
    # Fill borders
    Z[0, :] = Z[-1, :] = 1
    Z[:, 0] = Z[:, -1] = 1
    # Make aisles
    
    for i in range(density):
        x, y = random.randint(0, shape[1] // 2) * 2, random.randint(0, shape[0] // 2) * 2
        Z[y, x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_,x_ = neighbours[random.randint(0, len(neighbours) - 1)]
                if Z[y_, x_] == 0:
                    Z[y_, x_] = 1
                    Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                    x, y = x_, y_               
    Z[0][0] = 0
    Z[4][4] = 0
    ch1 = random.randint(0,1)
    if(ch1 == 1):
        Z[0][1]=0
    else:
        Z[1][0]=0
    ch2 = random.randint(0,1)
    if(ch2 == 1):
        Z[3][4]=0
    else:
        Z[4][3]=0
        
#    print Z
    mazes = []
    for i in range(0,len(Z)):
        for j in range(0,len(Z)):
            mazes.append(float(Z[i][j]))
    return mazes
#kindaopenmaze(5,5)  

def  geneticmatrix():
    matrix = []
    for i in range(0,5):
        matrix.append([])
        for j in range(0,5):
            matrix[i].append(0)
#    print matrix
    choice = [1,0,1,0,1,0,1,0]
    
    list1=[0,1,2,3,4]
    list2=[0,1,2,3,4]
    
    points = [[x,y] for x in list1 for y in list2]
    #print points
    points.remove([0,0])
    #del points
    #print points
    ycount = 0
    xcount = 0
    checklist = []
    checklist.append([ycount,xcount])
    for i in range(0,len(choice)):
        choose = random.choice(choice)
        choice.remove(choose)
        if(choose == 1):
            ycount = ycount+1
        else:
            xcount = xcount+1
        m = [ycount,xcount]
        points.remove(m)
        
    
    for sp in points:
        matrix[sp[0]][sp[1]] = random.randint(0,1)
        
    maze = []
    matrix = [[int(float(j)) for j in i] for i in matrix]
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            maze.append(float(matrix[i][j]))
#    nomaze = notmaze(matrix)
    print matrix        
    return maze

def  genetictrickymatrix():
    matrix = []
    for i in range(0,5):
        matrix.append([])
        for j in range(0,5):
            matrix[i].append(0)
#    print matrix
    
    list1=[0,1,2,3,4]
    list2=[0,1,2,3,4]
    
    points = [[x,y] for x in list1 for y in list2]
    #print points
    points.remove([0,0])
    #del points
    #print points
    ycount = 0
    xcount = 0
#    cal = [-1,1]
    checklist = []
    checklist.append([ycount,xcount])
    neighbor=[]
    while(xcount != 4 and ycount!=4):
        
        neighbors = [[ycount+1,xcount],[ycount-1,xcount],[ycount,xcount+1],[ycount,xcount-1]]
        for n in neighbors:
            if(n in points and n[0]>=0 and n[0]<5 and n[1]>=0 and n[1]<5):
                neighbor.append(n)
#                print n
#        print neighbors
#            print neighbor
        if(len(neighbor)!=0):
            choose = random.choice(neighbor)
            ycount = choose[0]
            xcount = choose[1]
            m = [ycount,xcount]
    #        print points
            points.remove(m)
            neighbor = []
        else:
            break
            
            
    for sp in points:
        matrix[sp[0]][sp[1]] = random.randint(0,1)
#    print matrix
    mazes = []
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            mazes.append(float(matrix[i][j]))
    return mazes
    



