# week3
hours spent:  <br/>
<br/>
This week I worked on the class FindSolution(). I started implementing Tremaux's algorithm for finding the path from the beggining to the end of the maze. The program looks for possible steps forward from the current cell. If there is no junction for the cell, it goes back and finds the closes cell on the path with junction. Unvisited cells are marked with 0, +1 is added with every visit, and the cells with no junction are marked with 'x'. <br/>
The program workes correctly until the first cell with no junction is found. To return to the closes cell with the junction, function return_to_junction() is used. It doesn't do it's job correctly yet so that's something to work on. <br/>
Next week the class FIndSolution() should be fully working, the solution path will be illustrated in the pygame window, and I have to figure out testing. <br/>

