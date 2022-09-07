import pygame

class Visualize:

    def __init__(self, width, height, maze, steps):

        pygame.init()

        self.margin = 20
        self.cell_size = 0

        self.maze = maze
        self.steps = steps

        print(self.steps)

        if width>height:
            self.cell_size = (600-self.margin*2)//width
        else:
            self.cell_size = (600-self.margin*2)//height

        screen_width = self.cell_size*width+self.margin*2
        screen_height = self.cell_size*height+self.margin*2

        self.window = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption("maze solver")

        self.main_loop()

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.window.fill((0,0,0))
            self.draw_grid()
            #self.draw_tremaux()
            self.draw_wall_follower()

            pygame.display.flip()

    def draw_grid(self):
        indx_y = 0

        for i in self.maze:
            indx_x = 0
            y = self.margin+indx_y*self.cell_size

            for j in i:
                x = self.margin+indx_x*self.cell_size
                coord = (x, y, self.cell_size, self.cell_size)
                indx_x += 1

                if j == "#":
                    pygame.draw.rect(self.window, (255, 255, 255), coord)

            indx_y += 1

    def draw_tremaux(self):
        indx_y = 0

        for i in self.maze:
            indx_x = 0
            y = self.margin+indx_y*self.cell_size

            for j in i:
                x = self.margin+indx_x*self.cell_size
                coord = (x+1, y+1, self.cell_size-2, self.cell_size-2)
                indx_x += 1

                if j != "#" and j != "x" and j != 0:
                    pygame.draw.rect(self.window, (255, 0, 0), coord)
                    
            indx_y += 1

    def draw_wall_follower(self):

            for i in range(len(self.steps)):
                row = self.steps[i][0]
                col = self.steps[i][1]
                dir = self.steps[i][2]
                intersection = True
                #intersection = self.steps[i][3]
                size = (self.cell_size-10)/2

                #y -> row position
                #x -> col position

                if dir == "S":
                    #x = self.margin + self.cell_size*(col+0.5)
                    #y = self.margin + self.cell_size*row
                    #coord = (x+1, y+1, size, size)
                    #pygame.draw.rect(self.window, (255, 0, 0), coord)
                    self.top_right(row, col, size)

                if dir == "N":
                    #x = self.margin + self.cell_size*col
                    #y = self.margin + self.cell_size*(row+0.5)
                    #coord = (x+1, y+1, size, size)
                    #pygame.draw.rect(self.window, (255, 0, 0), coord)
                    self.bottom_left(row,col,size)

                if dir == "E":
                    self.top_left(row,col,size)
                    #x = self.margin + self.cell_size*col
                    #y = self.margin + self.cell_size*row
                    #coord = (x+1, y+1, size, size)
                    #pygame.draw.rect(self.window, (255, 0, 0), coord)


                if dir == "W":
                    self.bottom_right(row,col,size)
                    #x = self.margin + self.cell_size*(col+0.5)
                    #y = self.margin + self.cell_size*(row+0.5)
                    #coord = (x+1, y+1, size, size)
                    #pygame.draw.rect(self.window, (255, 0, 0), coord)

                if i == len(self.steps)-1:
                    intersection = False

                if i<len(self.steps)-1: 
                    next_dir = self.steps[i+1][2]
                    if dir == next_dir:
                        intersection = False

                    if (dir == "N" and next_dir == "S"
                    or dir == "S" and next_dir == "N"
                    or dir == "E" and next_dir == "W"
                    or dir == "W" and next_dir == "E"):
                        self.top_left(row,col,size)
                        self.top_right(row,col,size)
                        self.bottom_left(row,col,size)
                        self.bottom_right(row,col,size)

                if dir == "N" and next_dir == "E":
                    self.top_left(row,col,size)
                    self.top_right(row,col,size)
                if dir == "S" and next_dir == "W":
                    self.bottom_right(row,col,size)
                    self.bottom_left(row,col,size)
                if dir == "E" and next_dir == "S":
                    self.top_right(row,col,size)
                    self.bottom_right(row,col,size)
                if dir == "W" and next_dir == "N":
                    self.bottom_left(row,col,size)
                    self.top_left(row,col,size)
                
                #pygame.draw.rect(self.window, (255, 0, 0), coord)

                if intersection == False:
                #y -> row position
                #x -> col position

                    if dir == "S":
                        self.bottom_right(row,col,size)
                        #x = self.margin + self.cell_size*(col+0.5)
                        #y = self.margin + self.cell_size*(row+0.5)
                        #coord = (x+1, y+1, size, size)
                        #pygame.draw.rect(self.window, (155, 0, 0), coord)

                    if dir == "N":
                        self.top_left(row,col,size)
                        #x = self.margin + self.cell_size*(col)
                        #y = self.margin + self.cell_size*(row)
                        #coord = (x+1, y+1, size, size)
                        #pygame.draw.rect(self.window, (155, 0, 0), coord)


                    if dir == "E":
                        self.top_right(row,col,size)
                        #x = self.margin + self.cell_size*(col+0.5)
                        #y = self.margin + self.cell_size*row
                        #coord = (x+1, y+1, size, size)
                        #pygame.draw.rect(self.window, (155, 0, 0), coord)


                    if dir == "W":
                        self.bottom_left(row,col,size)
                        #x = self.margin + self.cell_size*(col)
                        #y = self.margin + self.cell_size*(row+0.5)
                        #coord = (x+1, y+1, size, size)
                        #pygame.draw.rect(self.window, (155, 0, 0), coord)


                    #pygame.draw.rect(self.window, (155, 0, 0), coord)

    def top_left(self,row, col, size):
        x = self.margin + self.cell_size*(col)
        y = self.margin + self.cell_size*(row)
        coord = (x+1, y+1, size, size)
        pygame.draw.rect(self.window, (255, 0, 0), coord)

    def top_right(self,row, col, size):
        x = self.margin + self.cell_size*(col+0.5)
        y = self.margin + self.cell_size*row
        coord = (x+1, y+1, size, size)
        pygame.draw.rect(self.window, (255, 0, 0), coord)

    def bottom_left(self,row, col, size):
        x = self.margin + self.cell_size*(col)
        y = self.margin + self.cell_size*(row+0.5)
        coord = (x+1, y+1, size, size)
        pygame.draw.rect(self.window, (255, 0, 0), coord)

    def bottom_right(self,row, col, size):
        x = self.margin + self.cell_size*(col+0.5)
        y = self.margin + self.cell_size*(row+0.5)
        coord = (x+1, y+1, size, size)
        pygame.draw.rect(self.window, (255, 0, 0), coord)