# Implementation

## Structure

Code is divided into files: ```index.py```, ```tremaux.py```, ```wall_follower.py```, ```generate.py```, ```visualize.py```. <br/>
<br/>

1. **index** <br/>
Uses PyGame menu library to display the menu for the user. It asks for inputs: width and height of the maze, and selection of the algorithm to solve the maze: Tremaux or Wall Follower. Using the input data, it calls either class ```Tremaux()``` from ```tremaux.py``` file or class ```WallFollower()``` from ```wall_follower.py``` file and passes the width and height arguments. 

2. **tremaux** <br/>
??

3. **wall_follower** <br/>
??

4. **generate** <br/>
??

5. **visualize** <br/>
??


1. **generate_maze** <br/>
First an empty grid of a maze is generated (dimensions specified by user input. Next, coordinates of a starting point are choosen randomly (it cannot be on the border, ie. not the first or last column on row). That point is where generating the path starts and it becomes the current cell - function ```self.current_cell()```. That cell is marked as a walkable path and walls are drawn around it. From the existing walls one is chosen randomly and it becomes a new current cell. It is marked as a path and walls are drawn aroudn it (only empty cells become walls, paths remain walkable). Current cell is chosen again and again, and the maze is created by this recursion. Remaining empty (invisited, marked ```'x'``` cells become wallls, and function ```self.entrance_exit()``` randomly chooses ```self.entrance``` and ```self.exit``` - points where solution path of the maze should start and finish (entrance is always in the first row and exit in the last row). <br/>

2. **find_solution** <br/>
Function ```self.current_cell()``` uses entrance point to initiate the recursion. Program checks for possible junction and follows the walkable path. The next ```'.'``` cell, ie. path, becomes the current cell and its junction is searched. If there is junction, the recursion continues. If there is no junction (ie. there are no unvisited cells that are not walls), function ```self.return_to_junction()``` is called. Program goes back to the previous current cell (one step back on the path) and checks for it's other junctions (with unvisited walkable cells). The recursion occurs until junction is found and program continues as before. Every time the function ```self.current_cell()``` is called, it checks if the cell is the exit. If it is, recursion is stopped as solution path has been found. <br/>
3. **main** <br/>
Program initiates pygame and uses user input (ie. height and width of the maze) to set dimenstions of the pygame window. In the class ```Draw()``` there are functions which draw empty maze and solution path (in red) in the pygame window. <br/>

## Performance

![](graph_analysis/prims_graph.png)
![](graph_analysis/tremaux_graph.png)
![](graph_analysis/wall_follower_graph.png)

