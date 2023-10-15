C'est quoi la Derecursivation en programmation ?
```
Principe de transformer un algorithme recursif en iteratif.
```

C'est quoi la difference entre un algorithme en place ou non ?
```
- en place: tri dans le tableau d'origine.

- non en place: elements copier dans une nouvelle structure.
```

C'est quoi la difference entre un algorithme de tri stable ou non ?
```
- stable: garanti que si dans le tri il y a plusieurs fois la meme valeur, elles seront toujours dans le meme ordre entre elles.

- non-stable: si il y a plusieurs fois la meme valeur, il n'est pas garanti que le tri les gardes dans leurs ordre d'origine.
```

Quels sont les deux types de complexites des algorithmes de tri ? Quel est la notations de complexite d'un algorithme ?
```
- temporelle: temps d'execution.

- spaciale: espace en memoire.

Complexite temporelle:
- meilleur cas: O()
- moyen cas: O()
- pire cas: O()

Complexite spaciale: O()
```

Donne chacune des trois etapes du tri a bulles. (francais)
```
1. On parcour la liste a partir de la droite autant de fois qu'il y a d'elements dans la liste.
2. a chaque fois on compare l'element avec celui a ca gauche, si la condition du tri est fausse on les inverses.
3. a chaque etape on sais qu'un element a l'extreme gauche en plus est a la bonne position. On ne prendra plus en compte dans les prochaines iterations.
```

Donne les quatres etapes du tri par insertion. (francais)
```
1. parcourt la liste a partir du deuxieme element a gauche autant de fois qu'il y a d'elements dans la liste.
2. On stocke l'element dans un tempon.
3. On compare tous les elements precedents avec notre element, tant que la condition est vraie on les deplaces de un vers la droite.
4. Une fois que la condition est fausse, on place notre tempon juste a droite de l'element declencheur.
```

Donne les quatres etapes du tri par fusion. (francais)
```
1. Separer la liste en deux tant que chaque sous-liste ne sont pas composees d'un seul element.
2. Comparer les elements des sous-listes entre eux en partant du debut de chaque liste. Si la condition est vraie, on place l'element de cette liste au debut et on continue de comparer les elements des listes entre eux.
3. Quand une liste est vide d'element, on place tous ceux de l'autre a la fin et on remonte.
4. On continue de remonter jusqu'a finir le tri.
```

Donne les six etapes du tri rapide. (francais)
```
1. Choisir un element "pivot" dans la liste, le choix est libre.
2. Parcourir tous les elements avant le pivot à partir de l'extreme gauche pour trouver un element qui est plus grand que lui. Ne va pas plus loin que le pivot.
3. Parcourir tous les elements après le pivot à partir de l'extreme droite pour trouver un element qui est plus petit que lui. Ne va pas plus loin que le pivot.
4. Inverser l'element plus petit que le pivot avec celui qui est plus grand. Si un des pointeur est sur le pivot, inversez l'autre pointeur avec le pivot. Si les deux pointeurs sont sur le pivot, alors le pivot est a la bonne position.
5. On separe la liste en deux a partir du pivot sans le prendre en compte.
6. On applique la technique du dessus jusqu'a avoir tous les elements tries (listes de un elements).
```

Quel est la complexite du tri a bulles ? est-il stable ou non ?
```
meilleur cas temporelle  = n
moyen cas temporelle     = n^2
pire cas temporelle      = n^2
complexite spatiale      = 1
stabilite                = oui
```

Quel est la complexite du tri par insertion ? est-il stable ou non ?
```
meilleur cas temporelle  = n
moyen cas temporelle     = n^2
pire cas temporelle      = n^2
complexite spatiale      = 1
stabilite                = oui
```

Quel est la complexite du tri par fusion ? est-il stable ou non ?
```
meilleur cas temporelle  = n log n
moyen cas temporelle     = n log n
pire cas temporelle      = n log n
complexite spatiale      = n
stabilite                = oui
```

Quel est la complexite du tri rapide ? est-il stable ou non ?
```
meilleur cas temporelle  = n log n
moyen cas temporelle     = n log n
pire cas temporelle      = n^2
complexite spatiale      = log n
stabilite                = non
```