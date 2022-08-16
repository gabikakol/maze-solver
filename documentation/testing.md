# testing
There are two separate testing files for classes ```GenerateMaze()``` and ```FindSolution()```: tes_generate_maze.py and test_find_solution.py. Program runs tests using ```unittest```. <br/>Functions of the classes are tested using exemplary input. ```.assertEqual()``` and ```.assertNotEqual()``` are used for comparing expected and returned values, and ```.assertTrue()``` and ```.assertFalse()``` for checking the Boolean values. <br/>
Each testing file runs tests for the whole class. To test the whole program, both files must be ran *(that could actually be combined to run tests for both classes with one command, might change it later)*. <br/>
## test coverage
![img](/documentation/test_coverage/coverage_report.png)
