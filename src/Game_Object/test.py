from src.Game_Object.Map.Generator.game_generator import generate_level
from src.Game_Object.Objets.Generators.arme_generator import generate_sword,generate_bow
from src.save import save_game, load_save

e1 = generate_sword(1)
e2 = generate_sword(2)
e3 = generate_sword(3)
e4 = generate_sword(4)

a1 = generate_bow(1)
a2 = generate_bow(2)
a3 = generate_bow(3)
a4 = generate_bow(4)

l = generate_level(nb_room=10)

save_game(l,e1)
p = load_save()

print(l.map)

print(p.value)