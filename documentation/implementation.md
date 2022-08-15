# implementation
## structure
Whole code is divided into 3 files: generate_maze.py with class ```GenerateMaze()```, find_solution.py with class ```FindSolution()```, and main.py. 
1. generate_maze.py <br/>
First an empty grid of a maze is generated (dimensions specified by user input. Next, coordinates of a starting point are choosen randomly (it cannot be on the border, ie. not the first or last column on row). That point is where generating the path starts and it becomes the current cell - function ```self.current_cell()```. That cell is marked as a walkable path and walls are drawn around it. From the existing walls one is chosen randomly and it becomes a new current cell. It is marked as a path and walls are drawn aroudn it (only empty cells become walls, paths remain walkable). Current cell is chosen again and again, and the maze is created by this recursion. Remaining empty (invisited, marked ```'x'``` cells become wallls, and function ```self.entrance_exit()``` randomly chooses ```self.entrance``` and ```self.exit``` - points where solution path of the maze should start and finish (entrance is always in the first row and exit in the last row). <br/>
2. find_solution.py <br/>
...
3. main.py <br/>
...
