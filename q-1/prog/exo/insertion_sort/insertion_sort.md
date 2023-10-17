# Insertion sort

## Exo

Algorithme de tri par insertion

Faire:
- Deroulement en francais.
- Arbre algorithmique ou Pseudo code
- Code Python. (Iteratif)

### Francais

1. parcourt la liste a partir du deuxieme element a gauche autant de fois qu'il y a d'elements dans la liste.
2. On stocke l'element dans un tempon.
3. On compare tous les elements precedents avec notre element, tant que la condition est vraie on les deplaces de un vers la droite.
4. Une fois que la condition est fausse, on place notre tempon juste a droite de l'element declencheur.

### Pseudo Code.

```txt
tempon;
transmutation;

pour int i = 1, i > taille list, i++
    tempon = l'element i dans list
    transmutation = i - 1
    tant que transmutation >= 0 et que la condition avec l'element i et l'element transmutation est vraie
        l'element transmutation + 1 de list = l'element transmutation de list
        transmutation--
    l'element transmutation de list + 1 = tempon
```

### Code python

Base:
```py
def insertion_sort(list, condtion):
    # insertion sort code


def condition(element_1, element_2):
    return element_1 <= element_2


my_list = [9, 4, 3, 2, 6, 5]
insertion_sort(my_list, condition)
print(my_list)
```

Answer:
```py
def insertion_sort(list, condtion):
    tempon = 0
    transmutation = 0
    for key in range(1, len(list)):
        tempon = list[key]
        transmutation = key - 1
        while transmutation > 0 and condtion(tempon, list[transmutation]):
            list[transmutation + 1] = list[transmutation]
            transmutation -= 1
        list[transmutation + 1] = tempon


def condition(element_1, element_2):
    return element_1 <= element_2


my_list = [9, 4, 3, 2, 6, 5]
insertion_sort(my_list, condition)
print(my_list)
```