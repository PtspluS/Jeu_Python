import pygame
import Menu
import Game
from pygame.locals import *


pygame.init()
width = 1500
height = 700
fenetre = pygame.display.set_mode((width, height))
fond = pygame.image.load('sprite/Fond.png')
newGameButton = pygame.image.load('sprite/New_game.png')
continueButton = pygame.image.load('sprite/Continue.png')
exitButton = pygame.image.load('sprite/Exit.png')
fond = pygame.transform.scale(fond, (width, height))
fenetre.blit(fond, (0, 0))
fenetre.blit(newGameButton, (width / 2 - 327, 100))
fenetre.blit(continueButton, (width / 2 - 327, 300))
fenetre.blit(exitButton, (width / 2 - 327, 500))
pygame.display.flip()
cursor=Menu.menu()
if cursor == 0:
    Game.game()
if cursor == 1:
    print("charge une partie")
if cursor == 2:
    pygame.display.quit()
