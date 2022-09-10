import copy

from generate import Generate
from visualize import Visualize

class WallFollower:

    def __init__(self, width, height):

        maze = Generate(width, height)
        self.maze = copy.deepcopy(maze.maze)

        self.marked = copy.deepcopy(maze.maze)
        for i in range(len(self.marked)):
            for j in range(len(self.marked[i])):
                if self.marked[i][j] == ".":
                    self.marked[i][j] = 0

        self.steps = []
 
        self.entrance = copy.deepcopy(maze.entrance)
        self.exit = copy.deepcopy(maze.exit)

        self.current_cell(0,self.entrance, "S")

        #facing direction: N, S, E, W

        #left from to:
        #   S -> E (col+1)
        #   N -> W (col-1)
        #   E -> N (row-1)
        #   W -> S (row+1)


    def current_cell(self, row, column, direction):

        #check if there is a wall to the left
        #check if there is a wall to the front
        #check if there is a wall to the right

        self.marked[row][column] += 1
        self.steps.append([row, column, direction])
        x = []

        if row == len(self.maze)-1 and column == self.exit:
            Visualize(len(self.maze[0]), len(self.maze), self.marked, self.steps, "wf")

        else:

            if direction == "S":
                x = self.check_south(row, column)

            if direction == "N":            
                x = self.check_north(row, column)

            if direction == "E":
                x = self.check_east(row, column)

            if direction == "W":
                x = self.check_west(row, column)

            self.current_cell(x[0], x[1], x[2])


    def check_south(self, row, column):

        path = []

        if column+1<len(self.maze[0]) and self.maze[row][column+1] != "#":
            path = [row, column+1, "E"]

        elif row+1<len(self.maze) and self.maze[row+1][column] != "#":
            path = [row+1, column, "S"]

        elif column-1>=0 and self.maze[row][column-1] != "#":
            path = [row, column-1, "W"]

        else:
            path = [row, column, "N"]
            self.marked[row][column] += 1
            self.steps.append(path)

        return path


    def check_north(self, row, column):

        path = []

        if column-1>=0 and self.maze[row][column-1] != "#":
            path = [row, column-1, "W"]

        elif row-1>=0 and self.maze[row-1][column] != "#":
            path = [row-1, column, "N"]
    
        elif column+1<(len(self.maze[0])) and self.maze[row][column+1] != "#":
            path = [row, column+1, "E"]
        
        else:
            path = [row, column, "S"]
            self.marked[row][column] += 1
            self.steps.append(path)

        return path


    def check_east(self, row, column):

        path = []

        if row-1>=0 and self.maze[row-1][column] != "#":
            path = [row-1, column, "N"]

        elif column+1<len(self.maze[0]) and self.maze[row][column+1] != "#":
            path = [row, column+1, "E"]

        elif row+1<len(self.maze) and self.maze[row+1][column] != "#":
            path = [row+1, column, "S"]

        else:
            path = [row, column, "W"]
            self.marked[row][column] += 1
            self.steps.append(path)

        return path


    def check_west(self, row, column):

        path = []

        if row+1<len(self.maze) and self.maze[row+1][column] != "#":
            path = [row+1, column, "S"]

        elif column-1>=0 and self.maze[row][column-1] != "#":
            path = [row, column-1, "W"]

        elif row-1>=0 and self.maze[row+1][column] != "#":
            path = [row-1, column, "N"]
        
        else:
            path = [row, column, "E"]
            self.marked[row][column] += 1
            self.steps.append(path)

        return path
