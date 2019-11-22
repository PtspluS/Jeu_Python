import pygame
from src import UI

pygame.init()
width = 1500
height = 704
window = pygame.display.set_mode((width, height))


grass1 = pygame.image.load('../sprite/Grass1.png')
grass2 = pygame.image.load('../sprite/Grass2.png')
ble = pygame.image.load('../sprite/ble.png')
wall = pygame.image.load('../sprite/Wall.png')
inventory_fond = pygame.image.load('../sprite/fond_inventaire.png')
inventory_tile = pygame.image.load('../sprite/inventory_tiles.png')
inventory_press_tile = pygame.image.load('../sprite/inventory_press_tiles.png')
inventory_helmet = pygame.image.load('../sprite/inventory_helmet.png')
inventory_sword = pygame.image.load('../sprite/inventory_sword.png')
inventory_chest = pygame.image.load('../sprite/inventory_chest.png')
inventory_pants = pygame.image.load('../sprite/inventory_pants.png')
inventory_shoes = pygame.image.load('../sprite/inventory_shoes.png')
inventory_ring = pygame.image.load('../sprite/inventory_ring.png')
red_cursor = pygame.image.load('../sprite/cursor.png')
red_cursor.set_alpha(100)
yellow_cursor = pygame.image.load('../sprite/yellow_cursor.png')  # curseur d'examination
yellow_cursor.set_alpha(100)
cyan_cursor = pygame.image.load('sprite/cyan_cursor.png')  # curseur d'examination
cyan_cursor.set_alpha(100)