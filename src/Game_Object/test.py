from src.Game_Object.Personnages.Generators.pnj_generator import generate_civil
from src.Game_Object.Map.Generator.game_generator import generate_room, generate_level
from src.Game_Object.Map.Porte import Porte

a = generate_civil(type = "fermier")
b = generate_civil(type='mineur')
c = generate_civil(type='villageois')
d = generate_civil(type='bourgeois')

porte = Porte(1,0,2)

m = generate_room(2, id_next=3, id_previous=1, type='champs', nb_char=2, pos_portes = [0,0,porte,0])
l = generate_level(nb_room=3)

print(a.name, ' ', a.desc)
print(b.name, ' ', b.desc)
print(c.name, " ", c.desc)
print(d.name, ' ', d.desc)