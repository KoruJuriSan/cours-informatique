
# Prise de note - prog - N04

### Priorite des operations en programmation

1. Exposant
2. Multiplication / Division / Modulo
3. Addition / Soustraction
4. Relationnel / Conditionnel
5. NOT
6. AND
7. OR

### Fonctions

Un bout de code que l'on peut appeller n'importe ou autant de fois que l'on veut. Elle peut prendre des valeurs en arguements et retourner une valeur.

!! LA FONCTION N'A PAS ACCES AU VARIABLE DEFINIES DANS LE RESTE DU PROGRAMME !!

ex js:
```
function addition(num1, num2) {
    return num1 + num2
}
```

#### Procedure

Procedure: Une fonction qui ne retourne aucune valeur.

#### Recursivite

Rescurivite: la possiblite qu'une fonction puisse s'appeler elle meme.

Permet de resoudre des probleme plus simplement, est moins optimise que la methode iterative dans 99% des cas, peut etre remplacer par des structures iterative.

## Exercices

Fait le pseudo code, l'arbre algorithmique et optionnelement le code python des problemes suivant. L'algorithme doit etre recursif !

```txt
On a 7 disques de diamètres différents qui forment une tour. On souhaite 
déplacer ces disques vers une nouvelle tour en suivant les règles 
suivantes :​

On ne peut pas déplacer plus d’un disque à la fois​

On ne peut placer un disque que sur un disque plus grand (ou sur un 
emplacement vide)​

Trouver comment résoudre ce problème avec le moins de déplacement 
possible, et en utilisant une tour intermédiaire.
```

```txt
Quelqu’un a déposé un couple de lapins dans un certain​
lieu, clos de toutes parts, pour savoir combien de couples​
seraient issus de cette paire en une année, car il est dans​
leur nature de générer un autre couple en un seul mois, et​
qu’ils enfantent dans le second mois après leur naissance.

En sachant qu’un couple de lapins génère un nouveau couple de lapin chaque 
mois à partir de leur 2ème mois d’existence, après x mois combien 
aurais-je de couple de lapins ?
```

```txt
Calculer la factorielle d'un nombre reel positif p
```