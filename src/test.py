from src.Game_Object.Personnages.Zombi import Zombi
from src.Game_Object.Personnages.Generators.pnj_generator import generate_civil


z = Zombi("", nom = 'billy')
v = generate_civil(type='fermier')
c = generate_civil(type='villageois')

z.kill(v)
z.kill(c)

print(z.lvl)

z.respawn()

print(z.lvl)