from src.Game_Object.Map.Generator.game_generator import generate_level
from src.Game_Object.Objets.Generators.arme_generator import generate_sword,generate_bow

e1 = generate_sword(1)
e2 = generate_sword(2)
e3 = generate_sword(3)
e4 = generate_sword(4)

a1 = generate_bow(1)
a2 = generate_bow(2)
a3 = generate_bow(3)
a4 = generate_bow(4)

l = generate_level(nb_room=10)


print(l.map)

e1.describe()
e2.describe()
e3.describe()
e4.describe()

a1.describe()
a2.describe()
a3.describe()
a4.describe()