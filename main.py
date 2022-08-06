import random
import pygame
import copy

class GenerateMaze():
#this class creates random maze using randomized Prim's algorithm 

    def __init__(self):
        # user input
        width = 30
        #width = int(input("Width: "))
        while width < 3:
            print("The minimum width of the maze must be 3")
            width = int(input("Width: "))

        height = 20
        #height = int(input("Height: "))
        while height <3:
            print("The minimum height of the maze must be 3")
            height = int(input("Height: "))

        self.width = width
        self.height = height
        self.maze = []

        self.init_empty_maze()
    
    def print_maze(self):
        #prints the maze in the terminal
        for i in range(len(self.maze)):
            maze_row = ""
            for j in range(len(self.maze[i])):
                maze_row = maze_row + str(self.maze[i][j]) + " "
            print(maze_row)
        print(f"entrance index: {self.entrance}")
        print(f"exit index: {self.exit}")

    def init_start_point(self):
        # randomly chooses a starting point from where the maze is further created
        self.x = int(random.randint(0,self.width-2)) # height (ie. which row)
        self.y = int(random.randint(0, self.height-2)) # width (ie. which column)

        self.current_cell()

    def init_empty_maze(self):
        # creates a grid of an empty maze
        for i in range(0, self.height):
            row = []
            for j in range(0, self.width):
                row.append("x")
            self.maze.append(row)

        self.init_start_point()

    def current_cell(self):
        #randomly chosen starting point/cell
        self.maze[self.y][self.x] = "."

        #creates walls around chosen cell
        self.walls = []
        self.walls.append([self.y+1, self.x])
        self.walls.append([self.y-1, self.x])
        self.walls.append([self.y, self.x+1])
        self.walls.append([self.y, self.x-1])

        for i in range(len(self.walls)):
            y = self.walls[i][0]
            x = self.walls[i][-1]
            self.maze[y][x] = "#"

        while len(self.walls)>0:
            self.pick_random_wall()

        self.left_unvisited()      

    def pick_random_wall(self):
        random_wall = self.walls[int(random.randint(0,len(self.walls)-1))]
        #checks if it's an upper wall
        if random_wall[0] != 0:
            self.if_not_upper(random_wall)
        #checks if it's a bottom wall
        if random_wall[0] != self.height-1:
            self.if_not_bottom(random_wall)
        #checks if it's a left wall
        if random_wall[1] != 0:
            self.if_not_left(random_wall)
        #checks if it's a right wall
        if random_wall[1] != self.width-1:
            self.if_not_right(random_wall)

        self.remove_wall(random_wall)

    def if_not_upper(self, random_wall):
        a = random_wall[0]
        b = random_wall[1]

        if self.maze[a-1][b] == "x" and self.maze[a+1][b] == ".":
            cells_counter = self.count_cells_around(random_wall)

            if cells_counter <= 1:
                self.maze[a][b] = "."

                #upper
                if a != 0:
                    self.upper_wall(a,b)

                #left
                if b != 0:
                    self.left_wall(a, b)

                #right
                if b != self.width-1:
                    self.right_wall(a, b)
        
        self.remove_wall(random_wall)

    def if_not_bottom(self, random_wall):
        a = random_wall[0]
        b = random_wall[1]

        if self.maze[a+1][b] == "x" and self.maze[a-1][b] == ".":
            cells_counter = self.count_cells_around(random_wall)

            if cells_counter <= 1:
                self.maze[a][b] = "."

                #bottom
                if a != self.height-1:
                    self.bottom_wall(a,b)

                #left
                if b != 0:
                    self.left_wall(a,b)

                #right
                if b != self.width-1:
                    self.right_wall(a,b)
            
            self.remove_wall(random_wall)


    def if_not_left(self, random_wall):
        a = random_wall[0]
        b = random_wall[1]

        if self.maze[a][b-1] == "x" and self.maze[a][b+1] == ".":
            cells_counter = self.count_cells_around(random_wall)

            if cells_counter <= 1:
                self.maze[a][b] = "."
                
                #upper
                if a != 0:
                    self.upper_wall(a, b)
                
                #bottom
                if a != self.height-1:
                    self.bottom_wall(a, b)

                #left
                if b != 0:
                    self.left_wall(a, b)

            self.remove_wall(random_wall)

    def if_not_right(self, random_wall):
        a = random_wall[0]
        b = random_wall[1]

        if self.maze[a][b+1] == "x" and self.maze[a][b-1] == ".":
            cells_counter = self.count_cells_around(random_wall)

            if cells_counter <= 1:
                self.maze[a][b] = "."

                #right
                if b != self.width-1:
                    self.right_wall(a,b)

                #upper
                if a != 0:
                    self.upper_wall(a,b)
                    
                #bottom
                if a != self.height-1:
                    self.bottom_wall(a,b)

            self.remove_wall(random_wall)

    def upper_wall(self, a, b):
        #marks the cell as visited, puts a wall there (above the path ".")
        if self.maze[a-1][b] != ".":
            self.maze[a-1][b] = "#"
        if [a-1, b] not in self.walls:
            self.walls.append([a-1, b])

    def bottom_wall(self, a, b):
        #marks the cell as visited, puts a wall there (below the path ".")
        if self.maze[a+1][b] != ".":
            self.maze[a+1][b] = "#"
        if [a+1, b] not in self.walls:
            self.walls.append([a+1, b])

    def left_wall(self, a, b):
        #marks the cell as visited, puts a wall there (on the left from the path ".")
        if self.maze[a][b-1] != ".":
            self.maze[a][b-1] = "#"
        if [a, b-1] not in self.walls:
            self.walls.append([a, b-1])

    def right_wall(self, a, b):
        #marks the cell as visited, puts a wall there (on the right from the path ".")
        if self.maze[a][b+1] != ".":
            self.maze[a][b+1] = "#"
        if [a, b+1] not in self.walls:
            self.walls.append([a, b+1])

    def count_cells_around(self, random_wall):
        #counting the surrounding cells
        counter = 0
        a = random_wall[0]
        b = random_wall[1]

        if self.maze[a+1][b] == ".":
            counter += 1
        if self.maze[a-1][b] == ".":
            counter += 1
        if self.maze[a][b+1] == ".":
            counter += 1
        if self.maze[a][b-1] == ".":
            counter += 1

        return counter
    
    def left_unvisited(self):
        # marks the unvisited cells as walls
        for i in range(self.height):
            for j in range(self.width):
                if self.maze[i][j] == "x":
                    self.maze[i][j] = "#"
        
        self.entrance_exit()

    def remove_wall(self, random_wall):
        # remove visited wall from the street
        for i in self.walls:
            if random_wall[0] == i[0] and random_wall[-1] == i[-1]:
                self.walls.remove(i)
    
    def entrance_exit(self):
        # creates a random entrance to the maze (1st row)
        used_indexes = []
        while True:
            i = random.randint(0, self.width-1)
            if i not in used_indexes:
                if self.maze[1][i] == ".":
                    self.maze[0][i] = "."
                    self.entrance = i
                    break
            used_indexes.append(i)
        
        #created a ranom exit from the maze (last row)
        used_indexes = []
        while True:
            i = random.randint(0, self.width-1)
            if i not in used_indexes:
                if self.maze[self.height-2][i] == ".":
                    self.maze[self.height-1][i] = "."
                    self.exit = i
                    break
            used_indexes.append(i)

        self.print_maze()

class FindSolution(GenerateMaze):
#Tremaux's algorithm
    def __init__(self):
        self.entrance = copy.deepcopy(maze.entrance)
        self.marked = copy.deepcopy(maze.maze)
        for i in range(len(self.marked)):
            for j in range(len(self.marked[i])):
                if self.marked[i][j] == ".":
                    self.marked[i][j] = 0
                    # 0 = not marked; +1 with every visit, 'x' if it's a dead end
        self.walkable = copy.deepcopy(maze.maze)
        self.exit = copy.deepcopy(maze.exit)
        self.moves = {}

        self.current_cell("from_top", 0, self.entrance)

    def junction_from_top(self, row, column):
        #checks for junction one down, and one to the right and left
        junction = False

        #check if it's not the last row and if one cell down is a path
        if row != len(self.walkable)-1:
            if self.walkable[row+1][column] == "." and self.marked[row+1][column] != "x":
                junction = True
                self.marked[row][column] += 1
                return ("from_top", row+1, column)

        #check if it's not the last column and if one cell to the right is a path
        if column != len(self.walkable[-1])-1 and junction == False:
            if self.walkable[row][column+1] == "." and self.marked[row][column+1] != "x":
                junction = True
                self.marked[row][column] += 1
                return ("from_left", row, column+1)

        #check if it's not the first column and if one cell to the left is a path
        if column != 0 and junction == False:
            if self.walkable[row][column-1] == "." and self.marked[row][column-1] != "x":
                junction = True
                self.marked[row][column] += 1
                return ("from_right", row, column-1)
        
        if junction == False:
            if (row, column) != (0, self.entrance):
                self.marked[row][column] = "x"
            move_back = self.return_to_junction("from_top", row, column)
            return (move_back[0], move_back[1], move_back[2])
    
    def junction_from_left(self, row, column):
        #checks for junction one down, one up, and one to the right
        junction = False
        
        #check if it's not the last row and if one cell down is a path
        if row != len(self.walkable)-1:
            if self.walkable[row+1][column] == "." and self.marked[row+1][column] != "x":
                junction = True
                self.marked[row][column] += 1
                return ("from_top", row+1, column)

        #check if it's not the last column and if one cell to the right is a path
        if column != len(self.walkable[-1])-1 and junction == False:
            if self.walkable[row][column+1] == "." and self.marked[row][column+1] != "x":
                junction = True
                self.marked[row][column] += 1
                return ("from_left", row, column+1)
        
        #check if it's not the first row and if one cell up is a path
        if row != 0 and junction == False:
            if self.walkable[row-1][column] == "." and self.marked[row-1][column] != "x":
                junction = True
                self.marked[row][column] += 1
                return ("from_bottom", row-1, column)

        if junction == False:
            if (row, column) != (0, self.entrance):
                self.marked[row][column] = "x"
            move_back = self.return_to_junction("from_left", row, column)
            return (move_back[0], move_back[1], move_back[2])

    def junction_from_right(self, row, column):
        #checks for junction one down, one up, and one to the left
        junction = False
        
        #check if it's not the last row and if one cell down is a path
        if row != len(self.walkable)-1:
            if self.walkable[row+1][column] == "." and self.marked[row+1][column] != "x":
                junction = True
                self.marked[row][column] += 1
                return ("from_top", row+1, column)

        #check if it's not the first column and if one cell to the left is a path
        if column != 0 and junction == False:
            if self.walkable[row][column-1] == "." and self.marked[row][column-1] != "x":
                self.junction = True
                self.marked[row][column] += 1
                return ("from_right", row, column-1)
        
        #check if it's not the first row and if one cell up is a path
        if row != 0 and junction == False:
            if self.walkable[row-1][column] == "." and self.marked[row-1][column] != "x":
                junction = True
                self.marked[row][column] += 1
                return ("from_bottom", row-1, column)

        if junction == False:
            if (row, column) != (0, self.entrance):
                self.marked[row][column] = "x"
            move_back = self.return_to_junction("from_right", row, column)
            return (move_back[0], move_back[1], move_back[2])

    def junction_from_bottom(self, row, column):
        #checks for junction one up, and one to the right and left
        junction = False

        #check if it's not the last column and if one cell to the right is a path
        if column != len(self.walkable[-1])-1:
            if self.walkable[row][column+1] == "." and self.marked[row][column+1] != "x":
                junction = True
                self.marked[row][column] += 1
                return ("from_left", row, column+1)
                
        #check if it's not the first column and if one cell to the left is a path
        if column != 0 and junction == False:
            if self.walkable[row][column-1] == "." and self.marked[row][column-1] != "x":
                self.junction = True
                self.marked[row][column] += 1
                return ("from_right", row, column-1)

        #check if it's not the first row and if one cell up is a path
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

    def scan_for_exit(self, row, column):
        exit = False
        if (row, column) == (len(self.walkable)-1, self.exit):
            exit = True
            self.marked[row][column] = +1
            print("exit found")
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

# initialize pygame window
pygame.init()

maze = GenerateMaze()
solve = FindSolution()

margin = 20

if maze.width>maze.height:
    cell_size = (600-margin*2)//maze.width
else:
    cell_size = (600-margin*2)//maze.height

screen_width = cell_size*maze.width+margin*2
screen_height = cell_size*maze.height+margin*2

window = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
    
for i in range(len(solve.marked)):
            maze_row = ""
            for j in range(len(solve.marked[i])):
                maze_row = maze_row + str(solve.marked[i][j]) + " "
            print(maze_row)

def draw_empty_paths():
    indx_y = 0
    for i in maze.maze:
        indx_x = 0
        y = margin+indx_y*cell_size
        for j in i:
            x = margin+indx_x*cell_size
            coord = (x, y, cell_size, cell_size)
            indx_x += 1
            if j == "#":
                #mark walls as white (correct path is black)
                pygame.draw.rect(window, (255, 255, 255), coord)
        indx_y += 1

def draw_solved():
    indx_y = 0
    for i in solve.marked:
        indx_x = 0
        y = margin+indx_y*cell_size
        for j in i:
            x = margin+indx_x*cell_size
            coord = (x+1, y+1, cell_size-2, cell_size-2)
            indx_x += 1
            if j != "#" and j != "x" and j != 0:
                pygame.draw.rect(window, (255, 0, 0), coord)
        indx_y += 1

while True:
    window.fill(pygame.Color(0,0,0))

    draw_empty_paths()
    draw_solved()

    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            exit()

    pygame.display.flip()
