# week3
hours spent: about 20h <br/>
<br/>
This week I worked on the class FindSolution(). I implemented the Tremaux's algorithm for finding the path from the beggining to the end of the maze. The program looks for possible steps forward from the current cell. If there is no junction for the cell, it goes back and finds the closes cell on the path with junction using the function return_to_junction(). Sometimes the maze is not solved because the maximum recursion depth is exceeded, so that's something to work on and get fixed next week. <br/>
Unvisited cells are marked with 0, +1 is added to the cell with every visit, and the cells with no junction are marked with 'x'. <br/>
The correct path is illustrated in the pygame window as a red path. <br/>
Next week the class FIndSolution() should be fully working, the way the algorithm works will be illustrated in the pygame window (not just the solution), and I have to figure out testing. <br/>

