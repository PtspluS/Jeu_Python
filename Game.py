import pygame
from Gameobject import Personnage
from pygame.locals import *
turn=0



def game():


    continuer=1
    while continuer:
        for event in pygame.event.get():
            pygame.display.flip()
            if event.type == QUIT:
                continuer = 0
            if event.type == KEYDOWN:
                if event.key == K_s or event.key == K_DOWN:
                    bob.move(window, )
                if event.key == K_w or event.key == K_UP:
                if event.key == K_a or event.key == K_LEFT:
                if event.key == K_d or event.key == K_RIGHT:
                if event.key == K_q:
                if event.key == K_e:
                if event.key == K_i:
                if event.key == K_r:
