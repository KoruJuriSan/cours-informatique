# Prise de note - prog - N02

### Variables

Variable: Nom qui permet d'acceder a une valeur dans la memoire centrale

Type: le type de valeur que contient la variable.

#### Declaration vs Affectation vs Initialisation

- Declaration: Signifier au programme que la variable existe

- Affectation: Placement d'une valeur dans une variable

- Initialisation: Donner une valeur a une variable au moment de la declaration

#### Nommage des variables

Interdiction:

- commencer par un caractere special
- avoir des espaces
- d'etre un nom protege par le language

#### Typage statique ou dynamique

- Typage statique: typage explicite au language, le developpeur doit preciser le type lors de la creation.

- Typage dynamique: typage implicite au langage, le developpeur ne doit pas precicer le type lors de la creation.

#### Typage faible vs fort

- Typage fort: la variable ne peut pas changer de type lors de l'execution du programme.

- Typage faible: la variable peut changer de type lors de l'execution du programme.

### Exemples de types de variables

Les plus communs
- entiers
- nombres a virgules
- chaines de caracteres
- booleens (vrai ou faux)

Depend du language.

### Conditions

#### If

Permet d'executer du code que si une condition est vraie ou un autre code si elle est fausse mais qu'une condition deux est vraie ou encore d'executer encore une autre code si aucune conditions n'est vraie.

```js
if (condition) {
    // Code execute si la condition est VRAIE
} else if (condition_2) {
    // Code execute si la condition une est FAUSSE et la deuxieme VRAIE
} else {
    // Execute si la condition une et deux sont FAUSSES
}
```

#### Switch / Match

Permet de faire des tests de comparaisons entre une variable et plusieurs cas, si un cas est vrai, le code a l'interieur est execute.

```js
switch fruit {
    case "pomme":
        // code si fruit == "pomme"
    case "poire":
        // code si fruit == "poire"
    default:
        // code si aucun cas n'est correct
}
```

!! PLUS OPTIMISE Q'UN IF DANS LES COMPARAISONS !!

### Boucles

boucle: Structure iterative, qui se repete.

#### While

*Tant que* la *Condition* est *Vraie*, continue/**commence** les repetitions.

ex:
```ts
while (condition) {
    // code qui sera repete. tant que la condition est vraie
}
```

!! COMMENCE QUE SI LA CONDITION EST VRAIE AU DEPART !!

#### Do While

Tant que la condition est Vraie, continue les repetitions.

ex:
```ts
do {
    // code qui sera execute une fois et repete si la condition est vraie
} while (condition)
```

!! S'EXECUTE AU MOINS UNE FOIS, MEME SI LA CONDITION EST FAUSSE !!

#### For

Une boucle qui a chaque fin de tour applique une modification a une certaine variable (le **pas** de la variable, ex: elle meme + 1), elle continue tant que la condition centrale est correcte.

ex:
```ts
for (var; condition_sur_var; pas_var) {
    // code qui sera repete tant que condition_sur_variable est vrai
    // la variable "var" est utilisable (faire des variations)
}
```

#### For Each

Elle parcour chaque elements d'un tableau et le stoque a chaque tour dans une variable.

ex:
```ts
foreach (element of array) {
    // code qui sera repete autant de fois qu'il y a d'element dans array
    // la variable "element" est egal a l'element du tableau correspondant
}
```

### Operateurs

Permet de faire une nouvelle valeur a partir d'une ou deux autres

ex:
```
1 + 1 = 2
VRAI et FAUX = FAUX
"Bonjour " + "Michel" = "Bonjour Michel"
```

#### Operateurs mathematique en programmation

```
Addition: +
Soustraction: -
Multiplication: *
Division: /
Division entiere: //
Modulo: %
Puissance: **
```

#### Operateurs booleen en programmation

Permet de retourner vrai ou faux en comparants des valeurs entre eux

```
egalite: ==
egalite stricte: ===
inferieur: <
superieur: >
inferieur ou egal: <= 
superieur ou egal: >=
```

Operateurs ternaires. Permet de retourner vrai ou faux en comparants des valeurs booleen entre elles
```
ET: and / &&
OU: or / ||
NON: not / !

```

### Resolution de probleme

Decomposition d'un probleme:

- Parametres d'entrees (variables de l'enonce)
- Pre-condition (condition a respecter pour que le probleme est du sens)
- Post-condition (condition a respecter par les parametres d'entree et de sortie)
- Parametres de sortie (que retourne l'algorithme, quel format ?)