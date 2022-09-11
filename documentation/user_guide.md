# User guide

install ```pygame``` to run PyGame menu and PyGame window for maze visualization, and ```coverage``` for testing report: 
- ```pip install pygame```
- ```pip install coverage```

<br/>

Run ```index.py``` to execute the program. The menu asks for user input: type an integer between 3 and 30 to specify the width and height of the maze and choose the solving algorithm - Tremaux or Wall Follower. Use arrows or mouse left click to move between input boxes. <br/>
To quit the program when menu is displayed, choose ```exit``` or X button in the top right corner. Once the solving algorithm is chosen, PyGame window with maze grid and solution path is displayed. To close the program, use X button in the top right corner. <br/>

<br/>

File ```index.py``` is located in the directory ```/main```. Other files required to execute the program are: ```tremaux.py```, ```wall_follower.py```, ```generate.py```, ```visualize.py```, and can be found in the same directory. <br/>

<br/>

Testing files are located in the directory ```/main/tests``` and coverage report files in ```.html``` format in ```/main/tests/htmlcov```. To generate tests report, use command ```coverage report```.
