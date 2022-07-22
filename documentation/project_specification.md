# project specification
**Programme: Bachelor in Science <br/>
Language of the project: english (Python) <br/>**
<br/>
<br/>
What data structures and algorithms will you be using? <br/>
<br/>
I will use Depth First Search (DFS) and stack for maze generating and Breadth First Search (BFS) for maze solving. <br/>
The project will be written in Python. <br/>
<br/>
<br/>
What problem are you solving and why did you chose these specific data structures and algorithms?<br/>
<br/>
I create a random maze generator: generate a maze and solve it (+ I use pygame to illustrate the whole process). I consider maze to be an undirected graph, where cells are vertices and walls are edges.<br/>
I use Depth First Seach algorithm since it allows me to visit all reachable vertices, ie. all the cells in the maze grid, and stack to keep track of the visited cells. Maze will always have one entrance point and one exit, and it will consists of various dead ends. <br/>
<br/>
General method (steps): <br/>
I pop a cell from a non-empty stack. It is my current cell now. I check its neighbours. If it has any unvisited ones, I push it back to the stack and choose one of those neighbours. I remove the wall between the cell and its chosen neighbour. I mark the neighbour cell as visited and push it to the stack. <br/>
<br/>
<br/>
What is the program input and how will it be used?<br/>
<br/>
Input: width and height of the maze, size of the cell (ie. width of the path). Number of edges (walls) and vertices (cells) depends on that: columns = width/cell size; rows = height/cell size.<br/>
<br/>
<br/>
Expected time and space complexities of the program (big-O notations): <br/>
<br/>
Time complexity of stack operations I’ll be using (push and pop) is O(1). Time complexity of DFS algorithm is O(e+v), where ‘e’ is number of edges (walls) and ‘v’ is number of vertices (cells). Hence, the time complexity of the program depends on the program input, ie. the size of the grid and cells of the maze. <br/>
<br/>
<br/>
Sources:<br/>
<br/>
Data Structures and Algorithms course materials <br/>
https://www.algosome.com/articles/maze-generation-depth-first.html <br/>
https://en.wikipedia.org/wiki/Maze_generation_algorithm <br/>
*Sadik, Adil MJ, et al. "A comprehensive and comparative study of maze-solving techniques by implementing graph theory." 2010 International Conference on Artificial Intelligence and Computational Intelligence. Vol. 1. IEEE, 2010.*
