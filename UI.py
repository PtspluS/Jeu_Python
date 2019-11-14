import pygame
from pygame.locals import *
class UI():

    def __init__(self,window):
        self.full_bar=285
        fond_ui = pygame.image.load('sprite/fond_ui.png')
        attack_button = pygame.image.load('sprite/Attack_button.png')
        examine_button= pygame.image.load('sprite/Examine_button.png')
        interact_button = pygame.image.load('sprite/Interact_button.png')
        inventory_button = pygame.image.load('sprite/Inventory_button.png')
        spell_button = pygame.image.load('sprite/spell_button.png')
        life_bar = pygame.image.load('sprite/Life_bar.png')
        life_bar_full = pygame.image.load('sprite/Life_bar_full.png')
        xp_bar_full = pygame.image.load('sprite/XP_bar_full.png')


        window.blit(fond_ui, (1088, 0))
        window.blit(attack_button, (1170, 100))
        window.blit(examine_button, (1270,100))
        window.blit(interact_button, (1370, 100))
        window.blit(inventory_button, (1170, 200))
        window.blit(spell_button, (1270, 200))
        window.blit(life_bar, (1150, 300))
        window.blit(life_bar, (1150, 350))
        window.blit(pygame.transform.scale(life_bar_full,( self.full_bar,16)), (1160, 310))
        window.blit(pygame.transform.scale(xp_bar_full, (self.full_bar, 16)), (1160, 360))

