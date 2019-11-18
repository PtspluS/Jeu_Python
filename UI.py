from math import floor
import Global
import pygame
from pygame.locals import *


class UI:

    def __init__(self):
        self.window=Global.window
        self.full_bar = 285
        self.fond_ui = pygame.image.load('sprite/fond_ui.png')
        self.attack_button = pygame.image.load('sprite/Attack_button.png')
        self.examine_button = pygame.image.load('sprite/Examine_button.png')
        self.interact_button = pygame.image.load('sprite/Interact_button.png')
        self.inventory_button = pygame.image.load('sprite/Inventory_button.png')
        self.spell_button = pygame.image.load('sprite/spell_button.png')
        self.life_bar = pygame.image.load('sprite/Life_bar.png')
        self.life_bar_full = pygame.image.load('sprite/Life_bar_full.png')
        self.xp_bar_full = pygame.image.load('sprite/XP_bar_full.png')
        self.coin = pygame.image.load('sprite/coin.png')
        self.PA= pygame.image.load('sprite/PA.png')
        self.stat_tile = pygame.image.load('sprite/stat_tile.png')
        self.print_text = pygame.image.load('sprite/print_board.png')
        self.police = pygame.font.Font("8bit.ttf",20)

    def init_ui_game(self):
        self.window.blit(self.fond_ui, (1088, 0))
        self.window.blit(self.attack_button, (1170, 100))
        self.window.blit(self.examine_button, (1270, 100))
        self.window.blit(self.interact_button, (1370, 100))
        self.window.blit(self.inventory_button, (1170, 200))
        self.window.blit(self.spell_button, (1270, 200))




    def print_coin(self,player):
        self.window.blit(self.stat_tile, (1170, 400))
        self.window.blit(self.coin, (1225, 412))
        texte = self.police.render(str(player.money), True, pygame.Color("#a7a389"))
        self.window.blit(texte, (1178, 425))

    def print_life(self, player):
        self.window.blit(self.life_bar, (1150, 300))
        self.window.blit(self.life_bar, (1150, 350))
        self.window.blit(pygame.transform.scale(self.life_bar_full, (round(player.hp/player.max_hp*self.full_bar), 16)), (1160, 310))
        self.window.blit(pygame.transform.scale(self.xp_bar_full, (player.lvl, 16)), (1160, 360))

    def print_PA(self,player):
        self.window.blit(self.stat_tile, (1335, 400))
        self.window.blit(self.PA, (1390, 412))
        texte = self.police.render(str(player.PA), True, pygame.Color("#a7a389"))
        self.window.blit(texte, (1360, 425))


    def write(self,object):
        self.window.blit(self.print_text, (1152, 500))
        my_text=object
        for i in range(0,len(my_text)):
            texte = self.police.render(my_text[i], True, pygame.Color("#a7a389"))
            self.window.blit(texte, (1162+i%28*10, 505+ floor(i/28)*15))






