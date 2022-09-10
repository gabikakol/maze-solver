# Testing

<br/>

## General

There are three test files: 
- ```test_tremaux.py``` with ```TestTremaux()``` class for testing ```Tremaux()``` class 
- ```test_wall_follower.py``` with ```TestWallFollower()``` class for testing ```WallFollower()``` class 
- ```test_generate.py``` with ```TestGenerate()``` class for testing ```Generate()``` class. <br/>

Program runs tests using ```unittest``` library. Functions of the classes are tested using exemplary input. ```.assertEqual()``` and ```.assertNotEqual()``` are used for comparing expected and returned values, and ```.assertTrue()``` and ```.assertFalse()``` for checking the Boolean values. <br/>

<br/>

## Input

Maze dimensions: width and height (integer values between 3 and 30). <br/>
For each testing class, a random exemplary maze is used. Such maze is written in the function ```.setUp()``` in required by each class formats, and used througout the whole test class. 

<br/>

## Test coverage
![img](/documentation/test_coverage/coverage_report_marked.png)

<br/>

## Performance testing
*Graphs shown below are also included in the implementation document.* <br/>


<br/>

<p align="center">
<br/> <img src="graph_analysis/prims_graph.png" width="500">
<br/> <img src="graph_analysis/tremaux_graph.png" width="500">
<br/> <img src="graph_analysis/wall_follower_graph.png" width="500">
</p>

<br/>
