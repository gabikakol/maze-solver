import copy
from generate import Generate
from visualize import Visualize

class WallFollower:
    #left-hand rule (facing the walking direction - if going down the its kinda mirrored?)

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

        #self.print_maze()
        #self.steps.append([0,self.entrance, "S"])
        self.current_cell(0,self.entrance, "S")
        #facing direction: N, S, E, W

        #left from to:
        #   S -> E (col+1)
        #   N -> W (col-1)
        #   E -> N (row-1)
        #   W -> S (row+1)

        #right from to:
        #   S -> W (col-1)
        #   N -> E (col+1)
        #   E -> S (row+1)
        #   W -> N (row-1)


    def current_cell(self, row, column, direction):
        #check if there is a wall to the left
        #check if there is a wall to the front
        #check if there is a wall to the right

        self.marked[row][column] += 1
        self.steps.append([row, column, direction])
        x = []


        if row == len(self.maze)-1 and column == self.exit:
            Visualize(len(self.maze[0]), len(self.maze), self.marked, self.steps)

        else:

            if direction == "S":

                x = self.check_south(row, column)

                #self.next_move(x)
                #self.current_cell(x[0], x[1], x[2])


            if direction == "N":            

                x = self.check_north(row, column)

                #self.next_move(x)
                #self.current_cell(x[0], x[1], x[2])


            if direction == "E":

                x = self.check_east(row, column)

                #self.next_move(x)
                #self.current_cell(x[0], x[1], x[2])


            if direction == "W":

                x = self.check_west(row, column)

                #self.next_move(x)
                #self.current_cell(x[0], x[1], x[2])

            self.current_cell(x[0], x[1], x[2])

    def check_south(self, row, column):

        path = []

        if column+1<len(self.maze[0]) and self.maze[row][column+1] != "#":
            path = [row, column+1, "E"]
            #self.steps.append([row, column+1, "E", True])
            #return [row, column+1, "E", True]

        elif row+1<len(self.maze) and self.maze[row+1][column] != "#":
            path = [row+1, column, "S"]
            #self.steps.append([row+1, column, "S", False])
            #return [row+1, column, "S", False]

        elif column-1>=0 and self.maze[row][column-1] != "#":
            path = [row, column-1, "W"]
            #self.steps.append([row, column-1, "W", True])
            #return [row, column-1, "W", True]

        else:
            path = [row, column, "N"]
            self.marked[row][column] += 1
            self.steps.append(path)
            #return [row, column, "N", False]

        #self.steps.append(path)
        return path

    def check_north(self, row, column):

        path = []

        if column-1>=0 and self.maze[row][column-1] != "#":
            path = [row, column-1, "W"]
            #self.steps.append([row, column-1, "W", True])
            #return [row, column-1, "W", True]

        elif row-1>=0 and self.maze[row-1][column] != "#":
            path = [row-1, column, "N"]
            #self.steps.append([row-1, column, "N", False])
            #return [row-1, column, "N", False]
    
        elif column+1<(len(self.maze[0])) and self.maze[row][column+1] != "#":
            path = [row, column+1, "E"]
            #self.steps.append([row, column+1, "E", True])
            #return [row, column+1, "E", True]
        
        else:
            path = [row, column, "S"]
            self.marked[row][column] += 1
            self.steps.append(path)
            #return [row, column, "S", False]

        #self.steps.append(path)
        return path

    def check_east(self, row, column):

        path = []

        if row-1>=0 and self.maze[row-1][column] != "#":
            path = [row-1, column, "N"]
            #self.steps.append([row-1, column, "N", True])
            #return [row-1, column, "N", True]

        elif column+1<len(self.maze[0]) and self.maze[row][column+1] != "#":
            path = [row, column+1, "E"]
            #self.steps.append([row, column+1, "E", False])
            #return [row, column+1, "E", False]
    
        elif row+1<len(self.maze) and self.maze[row+1][column] != "#":
            path = [row+1, column, "S"]
            #self.steps.append([row+1, column, "S", True])
            #return [row+1, column, "S", True]

        else:
            path = [row, column, "W"]
            self.marked[row][column] += 1
            self.steps.append(path)
            #return [row, column, "W", False]

        #self.steps.append(path)
        return path

    def check_west(self, row, column):

        path = []

        if row+1<len(self.maze) and self.maze[row+1][column] != "#":
            path = [row+1, column, "S"]
            #self.steps.append([row+1, column, "S", True])
            #return [row+1, column, "S", True]

        elif column-1>=0 and self.maze[row][column-1] != "#":
            path = [row, column-1, "W"]
            #self.steps.append([row, column-1, "W", False])
            #return [row, column-1, "W", False]

        elif row-1>=0 and self.maze[row+1][column] != "#":
            path = [row-1, column, "N"]
            #self.steps.append([row-1, column, "N", True])
            #return [row-1, column, "N", True]
        
        else:
            path = [row, column, "E"]
            self.marked[row][column] += 1
            self.steps.append(path)
            #return [row, column, "E", False]

        #self.steps.append(path)
        return path

    '''
    def next_move(self, x):
        if x[0] == "left":
            self.turn_left(x[1], x[2], x[3])
        elif x[0] == "straight":
            self.keep_straight(x[1], x[2], x[3])
        elif x[0] == "right":
            self.turn_right(x[1], x[2], x[3])

    def turn_left(self, row, column, direction):
        self.current_cell(row, column, direction)
        
    def keep_straight(self, row, column, direction):
        self.current_cell(row, column, direction)

    def turn_right(self, row, column, direction):
        self.current_cell(row, column, direction)
    '''

if __name__ == "__main__":
    go = WallFollower(25,25)