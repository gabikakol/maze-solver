import copy

from generate import Generate
from visualize import Visualize

class WallFollower:

    '''finds the solution path for the maze from Generate() class using Wall Follower algorithm with left hand rule'''

    def __init__(self, width, height):

        maze = Generate(width, height)
        self.maze = copy.deepcopy(maze.maze)

        '''
        0 = not marked
        +1 with every visit
        '''

        self.marked = copy.deepcopy(maze.maze)
        for i in range(len(self.marked)):
            for j in range(len(self.marked[i])):
                if self.marked[i][j] == ".":
                    self.marked[i][j] = 0

        self.steps = []
 
        self.entrance = copy.deepcopy(maze.entrance)
        self.exit = copy.deepcopy(maze.exit)

        self.current_cell(0,self.entrance, "S")


    def current_cell(self, row, column, direction):

        '''
        directions: north (N), south (S), east (E), west (W):
            if current cell is facing south, it goes one step down from the user's perspective
            if current cell is facint east, it goes one step to the right from the user's perspective
            etc...
        '''

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

        '''
        first searches for a wall to the left (E), then in front (S), and then to the right (W)
        if all above mentioned walls exists, it turns 180 degrees around since it's a dead end
        '''

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

        '''
        first searches for a wall to the left (W), then in front (N), and then to the right (E)
        if all above mentioned walls exists, it turns 180 degrees around since it's a dead end
        '''

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

        '''
        first searches for a wall to the left (N), then in front (E), and then to the right (S)
        if all above mentioned walls exists, it turns 180 degrees around since it's a dead end
        '''

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

        '''
        first searches for a wall to the left (S), then in front (W), and then to the right (N)
        if all above mentioned walls exists, it turns 180 degrees around since it's a dead end
        '''

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
