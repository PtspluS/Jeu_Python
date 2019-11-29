import pygame
from src import UI

pygame.init()
width = 1500
height = 704

window = pygame.display.set_mode((width, height))
fond_death = pygame.image.load('sprite/dead.png')
fond = pygame.image.load('sprite/Fond.png')
new_game_button_picture = pygame.image.load('sprite/New_game.png')
continue_button_picture = pygame.image.load('sprite/Continue.png')
exit_button_picture = pygame.image.load('sprite/Exit.png')
fleche_picture = pygame.image.load('sprite/Fleche.png').convert_alpha()


grass1 = pygame.image.load('sprite/Grass1.png')
grass2 = pygame.image.load('sprite/Grass2.png')
door = pygame.image.load('sprite/Door.png')
ble = pygame.image.load('sprite/ble.png')
wall = pygame.image.load('sprite/Wall.png')

inventory_fond = pygame.image.load('sprite/fond_inventaire.png')
black = pygame.image.load('sprite/black.png')
inventory_tile = pygame.image.load('sprite/inventory_tiles.png')
inventory_press_tile = pygame.image.load('sprite/inventory_press_tiles.png')
inventory_helmet = pygame.image.load('sprite/inventory_helmet.png')
inventory_sword = pygame.image.load('sprite/inventory_sword.png')
inventory_chest = pygame.image.load('sprite/inventory_chest.png')
inventory_pants = pygame.image.load('sprite/inventory_pants.png')
inventory_shoes = pygame.image.load('sprite/inventory_shoes.png')
inventory_ring = pygame.image.load('sprite/inventory_ring.png')

red_cursor = pygame.image.load('sprite/cursor.png')
red_cursor.set_alpha(100)
yellow_cursor = pygame.image.load('sprite/yellow_cursor.png')  # curseur d'examination
yellow_cursor.set_alpha(100)
cyan_cursor = pygame.image.load('sprite/cyan_cursor.png')  # curseur d'examination
cyan_cursor.set_alpha(100)

fond_ui = pygame.image.load('sprite/Fond_ui.png')
attack_button = pygame.image.load('sprite/Attack_button.png')
examine_button = pygame.image.load('sprite/Examine_button.png')
interact_button = pygame.image.load('sprite/Interact_button.png')
inventory_button = pygame.image.load('sprite/Inventory_button.png')
spell_button = pygame.image.load('sprite/spell_button.png')
cast_button = pygame.image.load('sprite/cast_button.png')
sell_button = pygame.image.load('sprite/sell_button.png')
equipe_button = pygame.image.load('sprite/Equipe_button.png')
switch_button = pygame.image.load('sprite/Switch_button.png')
use_button = pygame.image.load('sprite/Use_button.png')
throw_button = pygame.image.load('sprite/Throw_button.png')
pass_button = pygame.image.load('sprite/Pass_button.png')
pick_button = pygame.image.load('sprite/Pick_button.png')
return_button = pygame.image.load('sprite/return_button.png')
life_bar = pygame.image.load('sprite/Life_bar.png')
life_bar_full = pygame.image.load('sprite/Life_bar_full.png')
xp_bar_full = pygame.image.load('sprite/XP_bar_full.png')
coin = pygame.image.load('sprite/coin.png')
PA = pygame.image.load('sprite/PA.png')
stat_tile = pygame.image.load('sprite/stat_tile.png')
print_text = pygame.image.load('sprite/print_board.png')

# spell
spell = pygame.image.load('sprite/spell.png')
bite = pygame.image.load('sprite/bite.png')

# zombie charac
zombie = pygame.image.load('sprite/Zombie.png')
zombie_bowman = pygame.image.load('sprite/Zombie_Bowman.png')
zombie_villager = pygame.image.load('sprite/Zombie_Villager.png')
zombie_richman = pygame.image.load('sprite/Zombie_Richman.png')
zombie_mineur = pygame.image.load('sprite/Zombie_miner.png')
zombie_farmer = pygame.image.load('sprite/Zombie_farmer.png')

# pnj charac
guarde_de_la_porte= pygame.image.load('sprite/Soldier.png')
villager = pygame.image.load('sprite/Villager.png')
farmer = pygame.image.load('sprite/Farmer.png')
miner = pygame.image.load('sprite/Miner.png')
richman = pygame.image.load('sprite/Richman.png')
grave = pygame.image.load('sprite/Grave.png')
bowman = pygame.image.load('sprite/Bowman.png')
lepreux = pygame.image.load('sprite/Lepreux.png')

# music
pygame.mixer.music.load('sprite/music.mp3')


# arme
# epe
epe1 = pygame.image.load('sprite/sword.png')
epe2 = pygame.image.load('sprite/iron_sword.png')
epe3 = pygame.image.load('sprite/steel_sword.png')
epe4 = pygame.image.load('sprite/master_sword.png')
# arc
arc1 = pygame.image.load('sprite/Arc.png')
arc4 = pygame.image.load('sprite/arc_elfique.png')



pygame.display.set_icon(zombie)

police = pygame.font.Font('8bit.ttf', 20)
ui = UI.UI()


def isinrange(x, y, max_x, max_y):
    """
    :param x: position x visée
    :param y: position y visée
    :param max_x: taille du tableau x
    :param max_y: taille du tableau y
    :return: si on est dans le tableau ou pas
    """
    if x >= max_x or x < 0 or y >= max_y or y < 0:
        return False
    else:
        return True



