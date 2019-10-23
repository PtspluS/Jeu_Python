import pygame
import Menu
from pygame.locals import *


pygame.init()
width = 1500
height = 700
cursor = 1
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
Menu.menu(pygame)