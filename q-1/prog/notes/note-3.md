
# Prise de note - prog - N03

### Algorithmie

Algorithme: Moyen de resoudre un probleme de maniere systematique. Transformation d'une solution en language parler en code comprehensible par la machine.

En Algorithmie, l'ordinateur ne prend pas d'initiative, on evite donc les embiguites

#### Trois regles d'un algorithme

- Terminaison: A une fin.
- Correction: Repond au probleme
- Completude: Donne toujours la bonne reponse, meme en changeant les valeurs initales

### Structure en algorithmie

#### De controle

- Sequences
- Conditionnels
- Iteratives

#### De donnees

- Constantes
- Variables
- Tableaux
- Recursives

### Tableaux

Variable qui contient plusieurs emplacement pouvant stocker des donnees, les donnes on un index precis pour les retrouver, on ne peut pas ajouter ou supprimer des donnes, on peut remplacer les donnees actuelles, il peut etre a plusieurs dimmensions, le tableau ne peut contenir plus d'un type de variable a l'interieur.

Index de la premiere valeur = 0

ex:
```py
tableau[dimension, taille]

tableau[2, 3]

2 | x | x | x |
1 | x | x | x |
0 | x | x | x |
    0   1   2
```

#### Tableau dynamiques

Permet d'ajouter et de supprimer des valeurs.

#### Tableau associatifs

L'index des elements du tableau est modifiable

ex:
```
tableau = {nom: "Jack", prenom: "Paul"}

tableau[nom] == "Jack"
tableau[prenom] == "Paul"
```

### Liste chainees

Ensemble d'element les un a la suite des autres, n'a pas de taille limite, il est possible d'ajouter et supprimer des elements

PARCONTRE, il faut passer par chaque element precedant pour atteindre un element x.

element = noeud
chaque noeud possede une donne + un pointeur vers l'element suivant.

```
1 => 2 => 3
```

#### Doublement chainees

Chaque noeuf possede aussi un pointeur vers l'element precedant. 

```
1 <=> 2 <=> 3
```

#### Circulaire

Le derrnier element pointe vers le premier.
```
1 => 2 => 3 => | 
| -----<<<---- | 
```

### Principes de files et piles.

les files (LIFO): Last In First Out
les Piles (FIFO): First In First Out

## Exercices


Fait le pseudo code, l'arbre algorithmique et optionnelement le code python des problemes suivant.

```txt
J’ai x € et j’en dépense y. Calculer combien il me reste d’€
```
```txt
Comment déterminer que kayak est un palindrome ?
```
```txt
Étant donné cinq entiers positifs [1,2,3,4,5] , trouvez les valeurs 
minimale et maximale qui peuvent être calculées en additionnant exactement 
quatre de ces cinq entiers. Ensuite, imprimez ces valeurs.
```

```txt
Marie a inventé une machine à voyager dans le temps et veut la tester en 
voyageant dans le temps pour visiter la Russie le jour du programmeur (le 
256e jour de l'année) pendant une année comprise entre 1700 et 2700.​

De 1700 à 1917, le calendrier officiel de la Russie était le calendrier 
julien ; depuis 1919, ils utilisent le système de calendrier grégorien. La 
transition du système de calendrier julien au calendrier grégorien s'est 
produite en 1918, lorsque le lendemain du 31 janvier était le 14 février. 
Cela signifie qu'en 1918, le 14 février était le 32e jour de l'année en 
Russie.​


Dans les deux systèmes de calendrier, février est le seul mois avec un 
nombre variable de jours ; il a 29 jours pendant une année bissextile et 
28 jours pendant toutes les autres années. Dans le calendrier julien, les 
années bissextiles sont divisibles par 4 ; dans le calendrier grégorien, 
les années bissextiles sont l'une des suivantes :​

Divisible par 400.​

Divisible par 4 et non divisible par 100.
```

```txt
Étant donné une année, y, trouvez la date du 256e jour de cette année 
selon le calendrier officiel russe au cours de cette année. Ensuite, 
imprimez-le au format jj.mm.aaaa, où jj est le jour à deux chiffres, mm 
est le mois à deux chiffres et aaaa est y.​

Par exemple, l'année donnée = 1984. 1984 est divisible par 4, c'est donc 
une année bissextile. Le 256ème jour d'une année bissextile après 1918 est 
le 12 septembre, donc la réponse est 12.09.1984.
```