# project specification
**Programme: Bachelor in Science <br/>
Language of the project: english (Python) <br/>**
<br/>
<br/>
What data structures and algorithms will you be using? <br/>
<br/>
I will use randomized Prim's algorithm for maze generating and Breadth First Search (BFS) for maze solving. <br/>
The project will be written in Python. <br/>
<br/>
<br/>
What problem are you solving and why did you chose these specific data structures and algorithms?<br/>
<br/>
I create a random maze generator: generate a maze and solve it (+ I use pygame to illustrate the whole process). I consider maze to be an undirected, fully connected graph, where cells are vertices and walls are edges.<br/>
I use randomized Prim's algorithm, which goes through all the cells and adds them to the minimum spanning tree (MST) to keep track of the visited vertices (nodes). The distance from the node is always the same (1), hence the edge is chosen randomly. 
Maze will always have one entrance point and one exit point, and it will consists of various dead ends. <br/>
I use Breadth First Search (BFS) algorithm to find the path from the starting point to the exit. It markes the current node as visited and pushes it into the queue. Then pops a node from the queue and checks for its unvisited neighbours. Unvisited neighbouring node is chosen as a current cell and the process is repeated. The operation ends when the maze is solved.  <br/>
<br/>
<br/>
What is the program input and how will it be used?<br/>
<br/>
Input: width and height of the maze. Hence, user decides on the complexity of the maze - its size is defined by the number of its cells, which is calculated by *width * height*.  <br/>
<br/>
<br/>
Expected time and space complexities of the program (big-O notations): <br/>
<br/>
Prim's algorithm will have time complexity O(v^2), where 'v' is number of vertices/nodes - ie. cells in the maze. Time complexity of BFS is O(e+v), where ‘e’ is number of edges (walls) and ‘v’ is number of vertices (cells). Hence, the time complexity of the program will be O(v^2) - will be dependent on the program input, ie. the size of the grid and cells of the maze. <br/>
<br/>
<br/>
Sources:<br/>
<br/>
Data Structures and Algorithms course materials <br/>
https://en.wikipedia.org/wiki/Maze_generation_algorithm <br/>
https://en.wikipedia.org/wiki/Maze-solving_algorithm <br/>
https://en.wikipedia.org/wiki/Breadth-first_search <br/>
*Sadik, Adil MJ, et al. "A comprehensive and comparative study of maze-solving techniques by implementing graph theory." 2010 International Conference on Artificial Intelligence and Computational Intelligence. Vol. 1. IEEE, 2010.*
