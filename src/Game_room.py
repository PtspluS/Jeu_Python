from src import Global
import pygame
from src import Game
from src.Game_Object.Map.terrain import Porte
from src.Game_Object.Personnages import Player

def game_room(lvl,player): # boucle qui gere un level
    room=lvl.rooms[0]
    continuer=1
    while continuer:
        return_value=Game.game(room, player)# lance une room
        if isinstance(return_value, Player.Player):# si un player est return cela veut dire que le player est mort
            return return_value
        elif isinstance(return_value, Porte.Porte):# si une porte est return, le player change de room
            for d in lvl.doors: # on cherche la room suivantes
                if d.id_in == return_value.id_out and d.id_out == return_value.id_in:
                    player.x = d.x
                    player.y = d.y

                    # une fois qu'on a trouve la porte qui correspond, on cherche la salle en rapport
                    for r in lvl.rooms:
                        if r.id == d.id_in:
                            room = r
        else :
            return False





