# Project specification

Programme: **Bachelor in Science** <br/>
Language of the project: **English** <br/>
Coding language: **Python** <br/>

<br/>

## Problem to be solved

I create a random maze generator: generate a maze and solve it. I use pygame to illustrate the maze grid and solution path. I consider maze to be an undirected, fully connected graph, where cells are vertices and the paths in the maze are the edges. Maze will always have one entrance point and one exit point, and it will consists of various dead ends. <br/>

<br/>

## Data structures and algorithms

Maze generating:
- randomized Prim's algorithm

Maze solving:
- Tremaux algorithm
- Wall Follower algorithm <br/>

To generate the grid of the maze, I use randomized Prim's algorithm, which goes through all the cells and adds them to the minimum spanning tree (MST) to keep track of the visited vertices (nodes). The distance from the node is always the same (1), hence the edge is chosen randomly. <br/>

To solve the maze, either Tremaux or Wall Follower algorithm can be used. <br/>

Tremaux algorithm: <br/>
The edges are marked as unvisited with 0 and with every visit +1 is added. The algorithm tries to first go right, then straight, then left. If it's at the dead end, it turns and goes back the same way until it finds the first possible turn with unvisited cells. The operation ends when the maze is solved (correct path to the end point is found). The solution path is cells visited once - marked '1'. <br/>

Wall Follower algorithm: <br/>
The algorithm finds a path from the starting point to the exit of the maze by following its walls. It always sticks to the wall to the left - wall to the west if facing north, wall to the east if facing south, wall to the south if facing west, and wall to the north is facing east. If the algorithm encounters a dead end, it does a 180 degrees turn. It is not the shortest solution path but the maze is solved. <br/>

<br/>

## Input

Input: width and height of the maze. Hence, user decides on the complexity of the maze - its size is defined by the number of its cells, which is calculated by *(width * height)*. User also chooses the algorithm used to solve the maze (Tremaux or Wall Follower). <br/>

<br/>

## Time complexity

Prim's algorithm will have time complexity O(v^2) and space complexity O(v), where 'v' is number of vertices - ie. cells in the maze. Hence, both the time complexity and the space complexity of the program dependent on the program input, ie. the size of the grid (number of cells) of the maze. <br/>
Tremaux and Wall Follower algorithms run in polynomial time. <br/>

<br/>

## Sources:

Data Structures and Algorithms course materials <br/>
https://en.wikipedia.org/wiki/Maze_generation_algorithm <br/>
https://en.wikipedia.org/wiki/Maze-solving_algorithm <br/>
https://en.wikipedia.org/wiki/Prim%27s_algorithm <br/>
*Sadik, Adil MJ, et al. "A comprehensive and comparative study of maze-solving techniques by implementing graph theory." 2010 International Conference on Artificial Intelligence and Computational Intelligence. Vol. 1. IEEE, 2010.*
