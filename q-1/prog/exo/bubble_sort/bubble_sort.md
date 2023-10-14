# Insertion sort

## Exo

Algorithme de tri a bulles

Faire:
- Deroulement en francais.
- Arbre algorithmique ou Pseudo code
- Code Python. (Iteratif)

### Francais

1. On parcour la liste a partir de la droite autant de fois qu'il y a d'elements dans la liste.
2. a chaque fois on compare l'element avec celui a ca gauche, si la condition du tri est fausse on les inverses.
3. a chaque etape on sais qu'un element a l'extreme gauche en plus est a la bonne position. On ne prendra plus en compte dans les prochaines iterations.

### Pseudo Code.

```txt
tempon;

pour int i = 1, i > taille list, i++
    pour int transmutation = taille de list - 1, transmutation > i, i--
        tempon = element transmutation de list
        si la condtion entre l'element et son voisin de gauche est vraie
            l'element transmutation de list = l'element transmutation - 1 de list
            l'element transmutation - 1 de list = tempon

```

### Code python

Base:
```py
def bubble_sort(list, condition):
    # bubble sort code


def condition(element_1, element_2):
    return element_1 <= element_2


my_list = [1, 4, 3, 2, 6, 5]
bubble_sort(my_list, condition)
print(my_list)
```

Answer:
```py
def bubble_sort(list, condition):
    tempon = 0
    for key in range(len(list)):
        for transmutation in range(len(list)-1, key, -1):
            tempon = list[transmutation]
            if (condition(tempon, list[transmutation - 1])):
                list[transmutation] = list[transmutation - 1]
                list[transmutation - 1] = tempon


def condition(element_1, element_2):
    return element_1 <= element_2


my_list = [1, 4, 3, 2, 6, 5]
bubble_sort(my_list, condition)
print(my_list)
```