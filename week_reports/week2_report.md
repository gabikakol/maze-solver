# week 2
hours spent: about 20h <br/>
<br/>
This week I wrote the main functionality of the project. The program randomly generates a maze and illustrates it using pygame. The dimensions of the maze are specified by the user input. The size of the pygame window also depends on the maze dimensions (width or height of the maze + margins of the size 20). The class GenerateMaze() uses randomized Prim's algorithm to create the maze and the class FindSolution() will solve the maze (it is an empty class now, the code will be written next week). <br/>
<br/>
The idea is that FindSolution() will use Tremaux's algorithm for maze solving. I did not know this algorithm before and I started researching online about it. Surprisingly there is not that much informaion about it so it will be a challenge to work on it. I understood how it works but still have no clue how to code it (the problem to deal with the next week). <br/>
<br/>
I struggled with the infinite loop and couldn't find a mistake for quite some time. It turned out to be a stupid bug - I typed 1 instead of i in the remove_wall function. <br/>
<br/>
Next week I will code the FindSolution() class, learn how to use Tremaux's algorithm, and visualize it in pygame
