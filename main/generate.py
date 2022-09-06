import random

class Generate():

    '''creates a ranom maze using randomized Prim's algorithm'''

    def __init__(self, width, height):
        
        '''
        width = int(input("Width: "))
        while width < 3:
            print("The minimum width of the maze must be 3")
            width = int(input("Width: "))

        height = int(input("Height: "))
        while height <3:
            print("The minimum height of the maze must be 3")
            height = int(input("Height: "))
        '''

        self.width = width
        self.height = height
        self.maze = []

        self.init_empty_maze()


    def init_start_point(self):

        '''        
        randomly chooses a starting point from where the maze is further created
            x -> height, ie. row
            y -> width, ie. column
        '''

        x = int(random.randint(1,self.width-2))
        y = int(random.randint(1,self.height-2))

        return [x, y]


    def init_empty_maze(self):
        
        '''creates a grid of an empty maze'''

        for i in range(0, self.height):
            row = []
            for j in range(0, self.width):
                row.append("x")
            self.maze.append(row)

        coord = self.init_start_point()
        self.current_cell(coord[0], coord[-1])


    def current_cell(self, x, y):
        
        '''creates walls around chosen cell'''

        self.maze[y][x] = "."   
        self.walls = []

        self.walls.append([y+1, x])
        self.walls.append([y-1, x])
        self.walls.append([y, x+1])
        self.walls.append([y, x-1])

        self.maze[y+1][x] = "#"
        self.maze[y-1][x] = "#"
        self.maze[y][x+1] = "#"
        self.maze[y][x-1] = "#"

        while len(self.walls)>0:
            self.pick_random_wall()

        self.left_unvisited()      


    def pick_random_wall(self):
        random_wall = self.walls[random.randint(0,len(self.walls)-1)]

        #checks if it's an upper wall
        if random_wall[0] != 0:
            self.not_upper(random_wall)

        #checks if it's a bottom wall
        if random_wall[0] != self.height-1:
            self.not_bottom(random_wall)

        #checks if it's a left wall
        if random_wall[1] != 0:
            self.not_left(random_wall)

        #checks if it's a right wall
        if random_wall[1] != self.width-1:
            self.not_right(random_wall)

        self.remove_wall(random_wall)


    def not_upper(self, random_wall):
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


    def not_bottom(self, random_wall):
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


    def not_left(self, random_wall):
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


    def not_right(self, random_wall):
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

        '''marks the cell as visited, puts a wall there (above the path ".")'''

        self.maze[a-1][b] = "#"
        if [a-1, b] not in self.walls:
            self.walls.append([a-1, b])


    def bottom_wall(self, a, b):

        '''marks the cell as visited, puts a wall there (below the path ".")'''

        self.maze[a+1][b] = "#"
        if [a+1, b] not in self.walls:
            self.walls.append([a+1, b])


    def left_wall(self, a, b):
        
        '''marks the cell as visited, puts a wall there (on the left from the path ".")'''

        self.maze[a][b-1] = "#"
        if [a, b-1] not in self.walls:
            self.walls.append([a, b-1])


    def right_wall(self, a, b):

        '''marks the cell as visited, puts a wall there (on the right from the path ".")'''

        self.maze[a][b+1] = "#"
        if [a, b+1] not in self.walls:
            self.walls.append([a, b+1])

    def count_cells_around(self, random_wall):

        '''counting the surrounding cells'''

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

        '''marks the unvisited cells as walls'''

        for i in range(self.height):
            for j in range(self.width):
                if self.maze[i][j] == "x":
                    self.maze[i][j] = "#"
        
        self.entrance_exit()


    def remove_wall(self, random_wall):

        '''marks the unvisited cells as walls'''

        for i in self.walls:
            if random_wall[0] == i[0] and random_wall[-1] == i[-1]:
                self.walls.remove(i)
    

    def entrance_exit(self):

        '''
        ENTRANCE:
        creates a random entrance to the maze (1st row)
        '''

        while True:
            i = random.randint(0,self.width-1)
            if self.maze[1][i] == ".":
                self.maze[0][i] = "."
                self.entrance = i
                break
        
        
        '''
        EXIT:
        creates a random exit from the maze (last row)
        '''

        while True:
            i = random.randint(0,self.width-1)
            if self.maze[self.height-2][i] == ".":
                self.maze[self.height-1][i] = "."
                self.exit = i
                break

        