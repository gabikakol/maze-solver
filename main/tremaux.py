import copy
from generate import Generate
from visualize import Visualize

class Tremaux():

    '''finds the solution path for the maze from GenerateMaze() class'''
    
    def __init__(self, width, height):

        maze = Generate(width, height)

        self.entrance = copy.deepcopy(maze.entrance)
        self.marked = copy.deepcopy(maze.maze)

        '''
        0 = not marked
        +1 with every visit
        'x' if it's a dead end
        '''

        for i in range(len(self.marked)):
            for j in range(len(self.marked[i])):
                if self.marked[i][j] == ".":
                    self.marked[i][j] = 0

        self.walkable = copy.deepcopy(maze.maze)
        self.exit = copy.deepcopy(maze.exit)
        self.moves = {}

        self.width = width
        self.height = height

        self.current_cell("from_top", 0, self.entrance)


    def junction_from_top(self, row, column):

        '''check for junction one down, and one to the right and left'''

        junction = False

        '''check if it's not the last row and if one cell down is a path'''

        if row != len(self.walkable)-1:
            if self.walkable[row+1][column] == "." and self.marked[row+1][column] != "x":
                junction = True
                self.marked[row][column] += 1

                return ("from_top", row+1, column)

        '''check if it's not the last column and if one cell to the right is a path'''

        if column != len(self.walkable[0]) and junction == False:
            if self.walkable[row][column+1] == "." and self.marked[row][column+1] != "x":
                junction = True
                self.marked[row][column] += 1

                return ("from_left", row, column+1)

        '''check if it's not the first column and if one cell to the left is a path'''

        if column != 0 and junction == False:
            if self.walkable[row][column-1] == "." and self.marked[row][column-1] != "x":
                junction = True
                self.marked[row][column] += 1

                return ("from_right", row, column-1)
        
        if junction == False:   #no junction
            if (row, column) != (0, self.entrance):
                self.marked[row][column] = "x"
            move_back = self.return_to_junction("from_top", row, column)

            return (move_back[0], move_back[1], move_back[2])
    
    def junction_from_left(self, row, column):

        '''checks for junction one down, one up, and one to the right'''

        junction = False
        
        '''check if it's not the last row and if one cell down is a path'''

        if row != len(self.walkable)-1:
            if self.walkable[row+1][column] == "." and self.marked[row+1][column] != "x":
                junction = True
                self.marked[row][column] += 1

                return ("from_top", row+1, column)

        '''check if it's not the last column and if one cell to the right is a path'''
        
        if column != len(self.walkable[0])-1 and junction == False:
            if self.walkable[row][column+1] == "." and self.marked[row][column+1] != "x":
                junction = True
                self.marked[row][column] += 1

                return ("from_left", row, column+1)
        
        '''check if it's not the first row and if one cell up is a path'''

        if row != 0 and junction == False:
            if self.walkable[row-1][column] == "." and self.marked[row-1][column] != "x":
                junction = True
                self.marked[row][column] += 1

                return ("from_bottom", row-1, column)

        if junction == False:   #no junction
            if (row, column) != (0, self.entrance):
                self.marked[row][column] = "x"
            move_back = self.return_to_junction("from_left", row, column)

            return (move_back[0], move_back[1], move_back[2])

    def junction_from_right(self, row, column):

        '''checks for junction one down, one up, and one to the left'''

        junction = False
        
        '''check if it's not the last row and if one cell down is a path'''

        if row != len(self.walkable)-1:
            if self.walkable[row+1][column] == "." and self.marked[row+1][column] != "x":
                junction = True
                self.marked[row][column] += 1

                return ("from_top", row+1, column)

        '''check if it's not the first column and if one cell to the left is a path'''

        if column != 0 and junction == False:
            if self.walkable[row][column-1] == "." and self.marked[row][column-1] != "x":
                self.junction = True
                self.marked[row][column] += 1

                return ("from_right", row, column-1)
        
        '''check if it's not the first row and if one cell up is a path'''

        if row != 0 and junction == False:
            if self.walkable[row-1][column] == "." and self.marked[row-1][column] != "x":
                junction = True
                self.marked[row][column] += 1

                return ("from_bottom", row-1, column)

        if junction == False:   #no junction
            if (row, column) != (0, self.entrance):
                self.marked[row][column] = "x"
            move_back = self.return_to_junction("from_right", row, column)
            
            return (move_back[0], move_back[1], move_back[2])

    def junction_from_bottom(self, row, column):
        
        '''checks for junction one up, and one to the right and left'''

        junction = False

        '''check if it's not the last column and if one cell to the right is a path'''

        if column != len(self.walkable)-1:
            if self.walkable[row][column+1] == "." and self.marked[row][column+1] != "x":
                junction = True
                self.marked[row][column] += 1

                return ("from_left", row, column+1)
                
        '''check if it's not the first column and if one cell to the left is a path'''

        if column != 0 and junction == False:
            if self.walkable[row][column-1] == "." and self.marked[row][column-1] != "x":
                self.junction = True
                self.marked[row][column] += 1

                return ("from_right", row, column-1)

        '''check if it's not the first row and if one cell up is a path'''

        if row != 0 and junction == False:
            if self.walkable[row-1][column] == "." and self.marked[row-1][column] != "x":
                junction = True
                self.marked[row][column] += 1

                return ("from_bottom", row-1, column)
        
        if junction == False:
            if (row, column) != (0, self.entrance):
                self.marked[row][column] = "x"
            move_back = self.return_to_junction("from_bottom", row, column)

            return (move_back[0], move_back[1], move_back[2])


    def current_cell(self, from_where, row, column):
        self.moves[(row, column)] = from_where
        exit = False

        if row == len(self.walkable)-1:
            exit = self.scan_for_exit(row, column)

        if not exit:
            a = ()

            if from_where == "from_top":
                a = self.junction_from_top(row, column)

            elif from_where == "from_left":
                a = self.junction_from_left(row, column)
            
            elif from_where == "from_right": 
                a = self.junction_from_right(row, column)
            
            elif from_where == "from_bottom":
                a = self.junction_from_bottom(row, column)
            
            self.current_cell(a[0], a[1], a[2])

        if exit:
            Visualize(self.width, self.height, self.marked, [], "t")


    def scan_for_exit(self, row, column):
        exit = False

        if column == self.exit:
            exit = True
            self.marked[row][column] += 1

        return exit


    def return_to_junction(self, from_where, row, column):

        if from_where == "from_top" and row != 0:
            row -= 1

        elif from_where == "from_left":
            column -= 1
        
        elif from_where == "from_right":
            column += 1
        
        elif from_where == "from_bottom":
            row += 1
        
        direction = self.moves[(row, column)]
        return (direction, row, column)
