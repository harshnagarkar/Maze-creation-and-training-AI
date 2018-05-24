# -*- coding: utf-8 -*-
"""
GreenChinchilla
"""
#importing dfs search as combination.py
import combination
import csv

#creating the combinations
def per(n):
    with open('data.csv', 'w') as myfile,open('results.csv', 'w') as myfileresult:

        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wre = csv.writer(myfileresult, quoting=csv.QUOTE_ALL)

#creates the combinations
        for i in range(1<<n):
            s=bin(i)[2:]
            s='0'*(n-len(s))+s
            m = list(map(int,list(s)))

#checks the start and enpoint 00 and 44
            if(m[0]==1 or m[-1]==1):

                wr.writerow(m)
                wre.writerow('0')
                continue
                
            else:
#creates the matrix for dfs
                count = 0
                matrix = []
                for p in range(0,5):
                     matrix.append([])
                     for q in range(0,5):
                         matrix[p].append(m[count])
                         count= count +1
                     count = 0
#calling dfs
                something = combination.dfsval(matrix)
#                writting the results
                if(something):
                    wr.writerow(m)
                    wre.writerow('1')
                else:
                    wr.writerow(m)
                    wre.writerow('0')
    myfile.close()
    myfileresult.close()        

#intialising above funtion for 25  digitial list combinations
per(25)

