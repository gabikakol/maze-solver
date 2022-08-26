import pygame
import pygame_menu
#from generate_maze import GenerateMaze

pygame.init()
window = pygame.display.set_mode((700, 400))
pygame.display.set_caption('maze solver')

menu = pygame_menu.Menu('Maze dimensions', 600, 300, theme=pygame_menu.themes.THEME_DARK)

def maze_dimensions():
    width = int(w.get_value())
    height = int(h.get_value())
    pass

w = menu.add.text_input('Width: ')
h = menu.add.text_input('Height: ')
menu.add.button('Go!', maze_dimensions)
menu.add.button('Exit', pygame_menu.events.EXIT)

menu.mainloop(window)



