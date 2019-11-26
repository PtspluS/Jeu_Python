# Monster legacie (Français)

## Principe du jeu 

### Présentation générale

Le jeu est séparé en 3 niveaux.
Le joueur apparait dans le premier niveau dans une salle. 
Dans chaque salle, le joueur rencontrera au choix, soit un marchand, soit des adversaires, soit s'il est dans la dernière salle du niveau, un boss. 
Une fois le boss vaincu, le joueur peut passer au niveau suivant.
Lorsque le joueur tue un pnj, ce dernier est rajouté à son tableau de victimes. Lorsque le joueur meurt, il se réincarne dans un des pnj qu'il a tué.

### Génération

Tous les niveaux sont générés de façon aléatoire et remplis de salles aux contenus qui le sont toute autant.
Le niveau étant fixé dans le marbre après la génération, lorsque l'on navigue de porte en porte, la configuration des salles reste la même.

### Réapparition

Lorsque le joueur meurt, il se réincarne dans l'une de ses victimes. Le choix de la victime est fait par un algorithme qui vous associe à chaque pnj un "victim score", plus le pnj était dur à tuer, plus son "victim score" est haut.
Lorsque le joueur réapparait, ses stats sont calqués sur celles de sa victime, il a donc le même nombre de PA, la même somme d'argent, la même santé, etc ...
Si le joueur n'a tué personne, il se réincarne en lui même.

### Points d'Actions

Le système de combat est régis par les PA (Points d'Actions), chaque action lors d'un tour va coûter des PA. Ce prix en PA va dépendre de nombreux paramètres tel que le type d'arme utilisé, la capacité utilisée, etc ...
Le joueur commence de base avec un nombre de PA maximum (pour un zombi 6) qui peut évoluer selon les réincarnation ou les niveaux.

### Combats

Les combats ont lieu lorsque le joueur rentre dans une salle avec des pnj hostile.
Le combat se déroule au tour par tour, le joueur commençant toujours en premier.
Lors du combat, il n'y a que trois issus possibles :
	- Soit le joueur meurt est réapparait dans sa victime avec le plus "victim score".
	- Soit le joueur change de salle.
	-  Soit le joueur tue son (ou ses adversaires) et gagne ses xp (points d'expérience) pour passer de niveau.

Le gain de niveau en combat est géré selon la règle simple qui est que plus l'adversaire est dur à tuer et plus il rapport d'xp.

### Looting 

Lorsqu'un pnj meurt, il fait apparaitre son cadavre. Ce dernier continent l'or qu'avait le feu pnj ainsi que son inventaire. 
Le joueur peut alors s'en approcher pour récupérer ce qu'il contient.
⚠️ Une fois le cadavre looté, il disparait, que son inventaire soit vide ou non.

## Classes 

### Joueur

Le joueur peut commencé avec une classe de base qui est :

|Nom de la classe|Attaque par défaut|Vie par défaut |PA défaut|
|:------------------:|:---------------------:|:----------------:|:--------:|
|Zombie| moyenne | moyenne | moyen |
|Spectre|haute|basse|moyen|
|Vampire|haute|moyenne|bas|
|Sirène|basse|haute|moyen|
|Loup garou|haute|basse|haut|

### Marchand

Lors de son parcours, le jouer peut tomber sur différents type de marchands :

|Type|Étale|
|:----:|:---:|
|Le lépreux | Armes et armures |
|La rousse | Magie |
|Le croc-mort | Vie |

### Les adversaires

Le joueur rencontrera aussi des adversaires lors de son parcours, qui seront : 

|Type|Attaque moyenne|Vie moyenne|PA moyen|Argent moyen|
|:---:|:---------------------:|:--------------:|:-----------:|:----------:|
|Fermier|basse | moyenne | bas | bas |
|Mineur| moyenne | bas | bas | bas |
|Villageois|moyenne|moyenne|bas|moyen|
|Bourgeois|basse|haute|bas|haut|
|Garde|basse|moyenne|moyen|bas|
|Guerrier|moyenne|haute|moyen|moyen|
|Archer|moyenne|basse|haut|moyen|
|Mage|haute|basse|moyen|haut|
|Chevalier|haute|haute|moyen|haut|
|Alchimiste|haute|moyenne|haut|haut




