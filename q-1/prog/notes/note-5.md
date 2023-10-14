
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

parcour la liste, a chaque element le compare avec le suivant, si il est plus grand que le suivant il les interchanges.

utilite: facile a comprendre, l'un des pires tri possible.

Complexite:
```txt
meilleur cas temporelle  = n
moyen cas temporelle     = n^2
pire cas temporelle      = n^2
complexite spatiale      = 1
stabilite                = oui
```

#### Tri par insertion

1. parcourt la liste, a chaque element
2. le retire du tableau, la met dans une variable tempon
3. deplace tout les elements a gauche de l'element vers la droite jusqu'a en trouver un plus petit.
4. depose le tempon a cet endroit.

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

1. Separer la liste en deux, si impaire choisir arbitrairement, le faire aussi sur chaque morceau de la liste jusqu'a avoir des listes de un element au max.
2. comparer les liste entre elle et remonter en les tirant entre elle.

utilite: facile a mettre en place et tres efficace en general.

Complexite:
```txt
meilleur cas temporelle  = log n
moyen cas temporelle     = log n
pire cas temporelle      = log n
complexite spatiale      = n
stabilite                = oui
```

#### Tri rapide

1. Choisir un element "pivot" dans la liste, le choix est libre.
2. parcourir tous les elements avant le pivot a partir de l'extreme gauche pour trouver un element qui est plus grand que lui. Ne va pas plus loin que le pivot
3. parcourir toues les elements apres le pivot a partir de l'extreme droite pour trouver un element qui est plus petit que lui. Ne va pas plus loin que le pivot
4. Inverser l'element plus petit que le pivot avec celui qui est plus grand. Si un des pointeur est sur le pivot on inverse l'autre pointeur avec le pivot. Si les deux pointeur son sur le pivot, alors le pivot est a la bonne position
5. On serpare la liste en deux a partir du pivot sans le prendre en compte.
6. On applique la technique du dessus jusqu'a avoir tous les elements trie. (listes de un elements.)

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