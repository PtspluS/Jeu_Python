import pygame
from room import Room
from terrain.ground import Ground
from Game import game
from Gameobject import Personnage
import copy
from pygame.locals import *


pygame.init()
width = 1500
height = 700
window = pygame.display.set_mode((width, height))
grass1 = pygame.image.load('sprite/Grass1.png')
grass2 = pygame.image.load('sprite/Grass2.png')
ble = pygame.image.load('sprite/ble.png')
wall = pygame.image.load('sprite/Wall.png')
map_x=10
map_y=10

tab_map = []
for i in range(0, map_x):
    malist=[]
    for j in range(0, map_y):
        malist.append(Ground(i, j, grass1))
    tab_map.append(malist)


first_room = Room(tab_map)
first_room.generate(window)
map_pos=10*[0]
for i in range(0,10):
    map_pos[i] = (10*[0])
bob_sprite = pygame.image.load('sprite/Zombie_villager.png')
bob=Personnage.Personnage(bob_sprite, "bob", "he is bob")
billy_sprite = pygame.image.load('sprite/miner.png')
billy=Personnage.Personnage(billy_sprite, "billy", "he is bob",100,0,9,9)

character_tab=[]
character_tab.append(bob)
character_tab.append(billy)
map_pos[0][0]=bob
map_pos[9][9]=billy
game(window, tab_map, map_pos, character_tab)
