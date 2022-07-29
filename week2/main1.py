import random
import pygame

class GenerateMaze():
#this class creates random maze using randomized Prim's algorithm 

    def __init__(self):
        # user input
        width = int(input("Width: "))
        while width < 3:
            print("The minimum width of the maze must be 3")
            width = int(input("Width: "))

        height = int(input("Height: "))
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

class FindSolution():
#Tremaux's algorithm
    def __init__(self):
        pass

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
    
def draw_path():
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

while True:
    window.fill(pygame.Color(0,0,0))

    draw_path()

    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            exit()

    pygame.display.flip()
