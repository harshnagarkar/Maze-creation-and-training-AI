"""
GreenChinchilla
"""

#setting return variable
global matrixvalue
matrixvalue=False
global visited
visited = []

#recursive dfs
def dfs(graph,start):
    global matrixvalue
    if(matrixvalue==False):
        ycount = start[0]
        xcount = start[1]
        neighbor = []
        #scanning neighbors
        neighbors = [[ycount+1,xcount],[ycount-1,xcount],[ycount,xcount+1],[ycount,xcount-1]]
        for n in neighbors:
            if(n not in visited and n[0]>=0 and n[0]<5 and n[1]>=0 and n[1]<5 and graph[n[0]][n[1]]!=1):
                neighbor.append(n)
    #    checkinh reached the solution or not
        if(len(neighbor)!=0):
            for p in neighbor:
                    visited.append(p)
#                    print p
                    if(p[0]==4 and p[1]==4):
#                        print p
                        matrixvalue = True
                        break
                        
                    else:
                        dfs(graph,p)
#non recursive base case instanciation
def dfsval(graph):
    #initialising dfs
    if(graph[4][4]!=1 and graph[0][0]!=1):
        dfs(graph,[0,0])
        print graph
        visited.append([0,0])
    else:
        return False
    print matrixvalue
    return matrixvalue;
