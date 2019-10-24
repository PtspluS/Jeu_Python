import pygame
import Menu
import Game
from pygame.locals import *


pygame.init()
width = 1500
height = 700

cursor=Menu.menu(width, height)
if cursor == 0:
    Game.game()
if cursor == 1:
    print("charge une partie")
if cursor == 2:
    pygame.display.quit()
