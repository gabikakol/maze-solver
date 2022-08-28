import pygame

class IllustrateMaze:

    def __init__(self, width, height, marked):

        pygame.init()

        self.margin = 20
        self.cell_size = 0

        self.marked = marked

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
            self.draw_path()

            pygame.display.flip()

    def draw_grid(self):
        indx_y = 0

        for i in self.marked:
            indx_x = 0
            y = self.margin+indx_y*self.cell_size

            for j in i:
                x = self.margin+indx_x*self.cell_size
                coord = (x, y, self.cell_size, self.cell_size)
                indx_x += 1

                if j == "#":
                    pygame.draw.rect(self.window, (255, 255, 255), coord)

            indx_y += 1

    def draw_path(self):
        indx_y = 0

        for i in self.marked:
            indx_x = 0
            y = self.margin+indx_y*self.cell_size

            for j in i:
                x = self.margin+indx_x*self.cell_size
                coord = (x+1, y+1, self.cell_size-2, self.cell_size-2)
                indx_x += 1

                if j != "#" and j != "x" and j != 0:
                    pygame.draw.rect(self.window, (255, 0, 0), coord)
                    
            indx_y += 1
