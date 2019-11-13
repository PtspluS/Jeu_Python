from Game.Personnages.Generators.pnj_generator import generate_civil

a = generate_civil(type = "fermier")
b = generate_civil(type='mineur')
c = generate_civil(type='villageois')
d = generate_civil(type='bourgeois')


print(a.name)
print(b.name)
print(c.name)
print(d.name)