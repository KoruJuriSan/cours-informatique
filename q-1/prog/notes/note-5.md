
# Prise de note - prog - N05

### Recursivite

#### Validite de la recursivite

Preuves d'arret
- Bien fonde
- Appel avec des valeurs inferieurs

Preuves de validite
- Correction partielle
- Demontrer que si l'algorithme fonctionne pou n-1, alors il fonctionne pour n.

#### Derecursivation

Principe de transformer un algorithme recursif en iteratif.
Il est toujours possible de le faire, mais pas l'inverse (~~iteratif => recursif~~).

### Algorithme de tri

!! Une liste avec un seul element est trie !!

#### Tri en place ou non

en place: le tri ce deroule dans le tableau d'origine, consome pas plus de memoire.

non en place: elements du tri copier dans une nouvelle structure, plus gourmand en memoire.

#### Tri stable ou non

stable: garanti que si dans le tri il y a plusieurs fois la meme valeur, elles seront toujours dans le meme ordre entre elles.

```
3, 1, 3, 0   =>   0, 1, 3, 3
a  a  b  a        a  a  a  b
```

non-stable: si il y a plusieurs fois la meme valeur, il n'est pas garanti que le tri les gardes dans leurs ordre d'origine
```
3, 1, 3, 0   =>   0, 1, 3, 3   ou   0, 1, 3, 3
a  a  b  a        a  a  a  b        a  a  b  a
```

#### Complexite

temporelle: temps d'execution

spaciale: espace en memoire

!! Quand on regarde l'efficacite temporelle d'un alogo on regarde son meilleur moyen et pire cas !!

#### Tri a bulles

1. On parcour la liste a partir de la droite autant de fois qu'il y a d'elements dans la liste.
2. a chaque fois on compare l'element avec celui a ca gauche, si la condition du tri est fausse on les inverses.
3. a chaque etape on sais qu'un element a l'extreme gauche en plus est a la bonne position. On ne prendra plus en compte dans les prochaines iterations.

utilite: facile a comprendre, l'un des pires tri possible.

ex python:
```py
def bubble_sort(list, condition):
    tempon = 0
    for key in range(len(list)):
        for transmutation in range(len(list)-1, key, -1):
            tempon = list[transmutation]
            if (condition(tempon, list[transmutation - 1])):
                list[transmutation] = list[transmutation - 1]
                list[transmutation - 1] = tempon
```

Complexite:
```txt
meilleur cas temporelle  = n
moyen cas temporelle     = n^2
pire cas temporelle      = n^2
complexite spatiale      = 1
stabilite                = oui
```

#### Tri par insertion

1. parcourt la liste a partir du deuxieme element a gauche autant de fois qu'il y a d'elements dans la liste.
2. On stocke l'element dans un tempon.
3. On compare tous les elements precedents avec notre element, tant que la condition est vraie on les deplaces de un vers la droite.
4. Une fois que la condition est fausse, on place notre tempon juste a droite de l'element declencheur.

ex python:
```py
def insertion_sort(list, condition):
    tempon = 0
    transmutation = 0
    for key in range(1, len(list)):
        tempon = list[key]
        transmutation = key - 1
        while transmutation > 0 and condition(tempon, list[transmutation]):
            list[transmutation + 1] = list[transmutation]
            transmutation -= 1
        list[transmutation + 1] = tempon
```

utilite: le tri de petite liste ou liste presque deja trie.

Complexite:
```txt
meilleur cas temporelle  = n
moyen cas temporelle     = n^2
pire cas temporelle      = n^2
complexite spatiale      = 1
stabilite                = oui
```

#### Tri par fusion

1. Separer la liste en deux tant que chaque sous-liste ne sont pas composees d'un seul element.
2. Comparer les elements des sous-listes entre eux en partant du debut de chaque liste. Si la condition est vraie, on place l'element de cette liste au debut et on continue de comparer les elements des listes entre eux.
3. Quand une liste est vide d'element, on place tous ceux de l'autre a la fin et on remonte.
4. On continue de remonter jusqu'a finir le tri.

utilite: facile a mettre en place et tres efficace en general.

Complexite:
```txt
meilleur cas temporelle  = n log n
moyen cas temporelle     = n log n
pire cas temporelle      = n log n
complexite spatiale      = n
stabilite                = oui
```

#### Tri rapide

1. Choisir un element "pivot" dans la liste, le choix est libre.
2. Parcourir tous les elements avant le pivot à partir de l'extreme gauche pour trouver un element qui est plus grand que lui. Ne va pas plus loin que le pivot.
3. Parcourir tous les elements après le pivot à partir de l'extreme droite pour trouver un element qui est plus petit que lui. Ne va pas plus loin que le pivot.
4. Inverser l'element plus petit que le pivot avec celui qui est plus grand. Si un des pointeur est sur le pivot, inversez l'autre pointeur avec le pivot. Si les deux pointeurs sont sur le pivot, alors le pivot est a la bonne position.
5. On separe la liste en deux a partir du pivot sans le prendre en compte.
6. On applique la technique du dessus jusqu'a avoir tous les elements tries (listes de un elements).

utilite: dans le tri de longue listes, en pratique il est tres efficace car le pire cas est tres rare, mais pas facile a mettre en place.

Complexite:
```txt
meilleur cas temporelle  = n log n
moyen cas temporelle     = n log n
pire cas temporelle      = n^2
complexite spatiale      = log n
stabilite                = non
```

## Exercices

Fait le pseudo code, l'arbre algorithmique et optionnelement le code python des problemes suivant. Fait un algorithme recursif ou un autre iteratif en fonction du type de tri.

```txt
Faire un tri a bulle pour une liste de nombres
```

```txt
Faire un tri par insertion pour une liste de nombres
```

```txt
Faire un tri de fusion pour une liste de nombres
```

```txt
Faire un tri rapide pour une liste de nombres
```