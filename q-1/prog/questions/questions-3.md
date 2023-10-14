Dans un language de programmation, les abiguites sont-elles permisent ? Qu’enttend-on par ambiguite ? 

- Non 
- D'utiliser plusieurs fois le meme nom pour faire des choses differentes. 

Quels sont les trois regles primordiales a l’algorithmie ? 
```
- La terminaison : le proramme est finis, non-infini 
- La correction : L’algorithme repond bien au probleme 
- La compleude : Donne toujours la bonne reponse, malgre le changement des valeurs de depart. 
```

Qu’est-ce qu’une liste chainee en prorammation ? Decompose un element de cette liste. Comment sont les donnees dans la memoire ? Quel sont les limites de ces listes.
```
- C’est un ensemble de noeud avec un ointeur vers l'element suivant.
- element = noeud + pointeur
- Non, contigue
- il faut parcourir TOUS les elements precedents pour atteindre un index precis.

si je veux attendre l'element 3, il faut parcourir l’element 0 => 1 => 2 => => 3 pour atteindre la valeur attendue 
```

Qu’est-ce qu’une liste chainee circulaire ? Comment fonctionne-elle 
```
Comme une liste chainee SAUF que le derrnier element pointe vert le permier, formant une boucle. 

1 => 2 => 3 => | 
| -----<<<---- | 
```

Qu’est-ce qu’une liste doublement chainee ? 
```
C’est une liste chainne SAUF, qu’il est possible de retourner en arriere en dans les noeuds. 
1 <=> 2 <=> 3
```

Comment ajouter un element '2' entre '1' et '3' dans cette liste chainee ? 1 => 3 
```
On garde l’addresse de “3” dans une variable tempon
On change le lien de “1” pour rajouter “2” a la suite 
On met l’addresse de “3” dans le pointeur de “2”
```

Qu'est-ce qu'un Algorithme ? (definition)
```
Moyen de resoudre un probleme de maniere systematique. Transformation d'une solution en language parler en code comprehensible par la machine.
```

Quelles sont les trois regles importantes pour un algorithme ?
```
- Terminaison: A une fin.
- Correction: Repond au probleme
- Completude: Donne toujours la bonne reponse, meme en changeant les valeurs initales
```

En algotithmie quelles sont les trois structures de controle ?
```
- Sequences
- Conditionnels
- Iteratives
```

En algorithmie quelles sont les trois structures de donnees ?
```
- Constantes
- Variables
- Tableaux
- Recursives (listes)
```

Qu’est-ce qu’un tableau en programmation ? Que permet-il ? Qelles sont ces limites
```
- Un type de variable 
- Permet de stocker un nombre PREDFINI de valeur a un INDEX precis dans un TYPE precis et une DIMENSION precise. 
- On ne peut pas supprimer ou ajouter de nouvelle valeurs, seulement les remplacer.

ex: 
Tableau[Dimension, Taille] 
Tableau[x, y] = z 
```

Que permetent les tableaux dynamiques en programmation ?
```
- supprimer des valeurs
- ajouter de nouvelles valeurs
```

Que permetent les tableaux associatifs en programmation ?
```
- choisir la valeur d'un index

ex:
tableau = {nom: "Jack", prenom: "Paul"}
tableau[nom] == "Jack"
tableau[prenom] == "Paul"
```

Que veut dire LIFO et FIFO ? Quels sont les deux principes derrieres ?
```
- files: FIFO (First In First Out)
- piles: LIFO (Last In First Out)
```