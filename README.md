# Maze-creation-and-training-AI
The aim to train AI for recognising a maze or not. 
A Maze is nothing but a matrix where 0 means hall way and 1 means wall and there has to be a pth from left  upper cocrner to right lower corner

In first try we tried genetic algorith to randomly create mazes and non mazes. This approach did nor prove that effective.

In second try we did a brute force approach to calculate all possible matrix combinations of 5 by 5.
Then ran a Dfs search on each of this and created two csv files one for results and other for matrix array.
Then we trained AI.

Problems in training.
At started we ran successfullfractional training using pandas
But when we tried to do on whole dataset ram limits exceeded for pc and performance slowed down.
In a supercomputer benchmark we found that pandas apprach needs 45GB ram.

In second apprach we just scanned using normal csv file opener and unwined it to float and then ran the same test.
This time it ran successfull on 8GB ram laptop.
