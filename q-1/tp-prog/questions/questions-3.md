Comment cree une liste en python ? Valeur de depart ?
```
my_list = [] # liste vide
my_list = [valeur1, valeur2, ...] # valeurs serparer par une ','
```

Comment ajouter un element a la fin d'une liste deja existante en python ?
```
my_list.append(valeur)
```

Comment ajouter un element a un index percis dans une liste deja existante en python ?
```
my_list.append(index, valeur)
```

Comment supprimer un element a un diex percis dans une liste en python ? Deux reponses.
```
my_list.pop(index)
del my_list[index] # Moderne
```

Comment supprimer le premier element qui a une valeur x dans une liste en python ?
```
my_list.remove(valeur)
```

Comment obtenir la taille d'une liste en python ?
```
len(my_list)
```

si je veux declarer plusieurs variables sur une seule ligne en python comment faire ? Si c'est possible.
```
var1, var2, ... = valeur1, valeur2, ...
```

comment faire une boucle foreach en python ?
```
for e in my_list: # itere autant de fois qu'il y a d'element dans la liste et le stocke dans 'e' a chaque iteration
        print(e) # print l'element e de la liste
```

C'est quoi la coprehension de liste en python ? Que remplace-elle
```
my_list = [variable for ...variable if condition sur variable]

equivalent to:

my_list = []
for variable in ...:
    if (condtion):
        my_list.append(variable)
```

fait un tri a bulle en python. Test avec [1, 4, 3, 2, 6, 5]
```
Si fonctionnel: Facile
Sinon: Reset

Correction:

for i in range(len(list)):
    for j in range(0, len(list)-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
```

