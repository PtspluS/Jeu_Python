import pygame
from room import room
from terrain.ground import Ground
from Game import game
from Gameobject import Personnage
from Gameobject import inventory
import copy
from pygame.locals import *

#Fonction pour tester

pygame.init()
width = 1500
height = 700
window = pygame.display.set_mode((width, height))

#chargement des images
grass1 = pygame.image.load('sprite/Grass1.png')
grass2 = pygame.image.load('sprite/Grass2.png')
ble = pygame.image.load('sprite/ble.png')
wall = pygame.image.load('sprite/Wall.png')

#creation de la map
map_x=10
map_y=10
tab_map = []
for i in range(0, map_x):
    malist=[]
    for j in range(0, map_y):
        malist.append(Ground(i, j, grass1))
    tab_map.append(malist)



#creation de personnages
my_inventory=inventory.inventory()
bob_sprite = pygame.image.load('sprite/Zombie_villager.png')
bob=Personnage.Personnage(bob_sprite, "bob", "he is bob",my_inventory)
billy_sprite = pygame.image.load('sprite/miner.png')
billy=Personnage.Personnage(billy_sprite, "billy", "he is bob",my_inventory,100,0,9,9)
character_tab=[]
character_tab.append(bob)
character_tab.append(billy)
first_room = room(tab_map,character_tab)
first_room.generate(window)


game(window, first_room, character_tab)
