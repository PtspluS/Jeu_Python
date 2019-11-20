import pygame
from src import UI

pygame.init()
width = 1500
height = 704
window = pygame.display.set_mode((width, height))

grass1 = pygame.image.load('src/sprite/Grass1.png')
grass2 = pygame.image.load('src/sprite/Grass2.png')
ble = pygame.image.load('src/sprite/ble.png')
wall = pygame.image.load('src/sprite/Wall.png')
inventory_fond = pygame.image.load('src/sprite/fond_inventaire.png')
inventory_tile = pygame.image.load('src/sprite/inventory_tiles.png')
inventory_press_tile = pygame.image.load('src/sprite/inventory_press_tiles.png')
inventory_helmet = pygame.image.load('src/sprite/inventory_helmet.png')
inventory_sword = pygame.image.load('src/sprite/inventory_sword.png')
inventory_chest = pygame.image.load('src/sprite/inventory_chest.png')
inventory_pants = pygame.image.load('src/sprite/inventory_pants.png')
inventory_shoes = pygame.image.load('src/sprite/inventory_shoes.png')
inventory_ring = pygame.image.load('src/sprite/inventory_ring.png')
red_cursor = pygame.image.load('src/sprite/cursor.png')
red_cursor.set_alpha(100)
yellow_cursor = pygame.image.load('src/sprite/yellow_cursor.png')  # curseur d'examination
yellow_cursor.set_alpha(100)
# ca merde la
fond_ui = pygame.image.load('src/sprite/Fond_ui.png')
attack_button = pygame.image.load('src/sprite/Attack_button.png')
examine_button = pygame.image.load('src/sprite/Examine_button.png')
interact_button = pygame.image.load('src/sprite/Interact_button.png')
inventory_button = pygame.image.load('src/sprite/Inventory_button.png')
spell_button = pygame.image.load('src/sprite/spell_button.png')
equipe_button = pygame.image.load('src/sprite/Equipe_button.png')
switch_button = pygame.image.load('src/sprite/Switch_button.png')
use_button = pygame.image.load('src/sprite/Use_button.png')
throw_button = pygame.image.load('src/sprite/Throw_button.png')
life_bar = pygame.image.load('src/sprite/Life_bar.png')
life_bar_full = pygame.image.load('src/sprite/Life_bar_full.png')
xp_bar_full = pygame.image.load('src/sprite/XP_bar_full.png')
coin = pygame.image.load('src/sprite/coin.png')
PA= pygame.image.load('src/sprite/PA.png')
stat_tile = pygame.image.load('src/sprite/stat_tile.png')
print_text = pygame.image.load('src/sprite/print_board.png')
police = pygame.font.Font("src/8bit.ttf",20)

ui=UI.UI()