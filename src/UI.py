from math import floor
from src import Global
import pygame
from pygame.locals import *


class UI:

    def __init__(self):
        self.window = Global.window
        self.full_bar = 285
        self.fond_ui = Global.fond_ui
        self.attack_button = Global.attack_button
        self.examine_button = Global.examine_button
        self.interact_button = Global.interact_button
        self.inventory_button = Global.inventory_button
        self.spell_button = Global.spell_button
        self.equipe_button = Global.equipe_button
        self.switch_button = Global.switch_button
        self.use_button = Global.use_button
        self.throw_button = Global.throw_button
        self.pass_button = Global.pass_button
        self.pick_button = Global.pick_button
        self.return_button = Global.return_button
        self.life_bar = Global.life_bar
        self.life_bar_full = Global.life_bar_full
        self.cast_button = Global.cast_button
        self.sell_button = Global.sell_button
        self.xp_bar_full = Global.xp_bar_full
        self.coin = Global.coin
        self.PA = Global.PA
        self.stat_tile = Global.stat_tile
        self.print_text = Global.print_text
        self.police = Global.police


    def init_ui_game(self):
        self.window.blit(self.fond_ui, (1088, 0))
        self.window.blit(self.attack_button, (1170, 100))
        self.window.blit(self.examine_button, (1270, 100))
        self.window.blit(self.interact_button, (1370, 100))
        self.window.blit(self.inventory_button, (1170, 200))
        self.window.blit(self.spell_button, (1270, 200))
        self.window.blit(self.pass_button, (1370, 200))

    def init_ui_inventory(self):
        self.window.blit(self.equipe_button, (1170, 100))
        self.window.blit(self.throw_button, (1270, 100))
        self.window.blit(self.switch_button, (1370, 100))
        self.window.blit(self.pick_button, (1170, 200))
        self.window.blit(self.return_button, (1270, 200))
        self.window.blit(Global.inventory_tile, (1370, 200))

    def init_ui_marchant(self):
        self.window.blit(self.sell_button, (1170, 100))
        self.window.blit(self.switch_button, (1270, 100))
        self.window.blit(self.return_button, (1370, 100))
        self.window.blit(Global.inventory_tile, (1170, 200))
        self.window.blit(Global.inventory_tile, (1270, 200))
        self.window.blit(Global.inventory_tile, (1370, 200))

    def init_ui_spell(self):
        self.window.blit(self.cast_button, (1170, 100))
        self.window.blit(self.return_button, (1270, 100))
        self.window.blit(Global.inventory_tile, (1370, 100))
        self.window.blit(Global.inventory_tile, (1170, 200))
        self.window.blit(Global.inventory_tile, (1270, 200))
        self.window.blit(Global.inventory_tile, (1370, 200))




    def print_coin(self, player):
        self.window.blit(self.stat_tile, (1170, 400))
        self.window.blit(self.coin, (1225, 412))
        texte = self.police.render(str(player.money), True, pygame.Color("#a7a389"))
        self.window.blit(texte, (1178, 425))

    def print_life(self, player):
        self.window.blit(self.life_bar, (1150, 300))
        self.window.blit(self.life_bar, (1150, 350))
        self.window.blit(
            pygame.transform.scale(self.life_bar_full, (round(player.hp / player.max_hp * self.full_bar), 16)),
            (1160, 310))
        self.window.blit(pygame.transform.scale(self.xp_bar_full,(round(player.xp/player.next_level*self.full_bar), 16)),(1160, 360))

    def print_PA(self, player):
        self.window.blit(self.stat_tile, (1335, 400))
        self.window.blit(self.PA, (1390, 412))
        texte = self.police.render(str(player.PA), True, pygame.Color("#a7a389"))
        self.window.blit(texte, (1360, 425))

    def write(self, my_text):
        self.window.blit(self.print_text, (1152, 500))

        for i in range(0, len(my_text)):
            texte = self.police.render(my_text[i], True, pygame.Color("#a7a389"))
            self.window.blit(texte, (1162 + i % 28 * 10, 505 + floor(i / 28) * 15))
