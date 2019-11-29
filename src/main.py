import pygame

from src import Global, Game_level
from src import inventory
from src.Game_Object.Personnages.Zombi import Zombi
from src.Game_Object.Objets import Sword
from src.Game_Object.Objets import Bow
from src.Game_Object.Objets import Tete
from src.Game_Object.Map.Generator.game_generator import generate_level

# Fonction pour tester


width = 1500
height = 704

window = Global.window

# chargement des images
grass1 = Global.grass1
grass2 = Global.grass2
ble = Global.ble
wall = Global.wall

# creation de la map
map_x = 17
map_y = 11



# creation de personnages
my_inventory = inventory.inventory()


imgcasque = pygame.image.load('sprite/wall.png')
helmet=Tete.Tete("casque",imgcasque, 1, 10)
imgepee = pygame.image.load('sprite/ble.png')
sword=Sword.Sword("epee",imgepee, 100, 10)
bow=Bow.Bow("bow",imgepee, 100, 10)
#my_inventory.pick(sword)
#my_inventory.pick(bow)
# character_tab est le tableau contenant tput les personnages de la salle
# creation de la salle



# lancement de la salle
Game_level.game_level()
