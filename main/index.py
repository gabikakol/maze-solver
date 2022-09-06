import pygame
import pygame_menu

from tremaux import Tremaux

'''
PyGame Menu asks for user input: width and height of the maze, ie. number of cells
both inputs must be integers between 3 and 40'''

pygame.init()
window = pygame.display.set_mode((700, 600))
pygame.display.set_caption('maze solver')

menu = pygame_menu.Menu('Maze dimensions', 600, 300, theme=pygame_menu.themes.THEME_DARK)

def maze_dimensions():
    width = int(w.get_value())
    height = int(h.get_value())
    if width<3 or width>40 or height<3 or width>40:
        pass        #to be done
    go = Tremaux(width, height)

w = menu.add.text_input('Width: ')
h = menu.add.text_input('Height: ')
menu.add.button('Go!', maze_dimensions)
menu.add.button('Exit', pygame_menu.events.EXIT)

menu.mainloop(window)

