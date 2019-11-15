from Game_Object.Personnages.Generators.pnj_generator import generate_civil

a = generate_civil(type = "fermier")
b = generate_civil(type='mineur')
c = generate_civil(type='villageois')
d = generate_civil(type='bourgeois')


print(a.name, ' ', a.desc)
print(b.name, ' ', b.desc)
print(c.name, " ", c.desc)
print(d.name, ' ', d.desc)