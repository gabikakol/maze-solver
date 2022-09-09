import pygame
import pygame_menu

from tremaux import Tremaux
from wall_follower import WallFollower

'''
PyGame Menu asks for user input: width and height of the maze, ie. number of cells
both inputs must be integers between 3 and 40'''

pygame.init()
window = pygame.display.set_mode((700, 600))
pygame.display.set_caption('maze solver')

menu = pygame_menu.Menu('Maze dimensions', 600, 400, theme=pygame_menu.themes.THEME_DARK)

def solve_tremaux():
    width = int(w.get_value())
    height = int(h.get_value())
    if width<3:
        width = 3
    if height<3:
        height = 3
    if width>30:
        width = 30
    if height>30:
        height = 30
    go = Tremaux(width, height)

def solve_wall_follower():
    width = int(w.get_value())
    height = int(h.get_value())
    if width<3:
        width = 3
    if height<3:
        height = 3
    if width>30:
        width = 30
    if height>30:
        height = 30
    go = WallFollower(width, height)

w = menu.add.text_input('Width: ')
h = menu.add.text_input('Height: ')
menu.add.button('Solve with TREMAUX', solve_tremaux)
menu.add.button('Solve with WALL FOLLOWER', solve_wall_follower)
menu.add.button('Exit', pygame_menu.events.EXIT)

menu.mainloop(window)

