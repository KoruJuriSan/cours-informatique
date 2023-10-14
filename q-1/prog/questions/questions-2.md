Quelles sont les deux notations les plus commune de l’operateur logique ET?
```
- and
- &&
``` 

Quelles sont les deux notations les plus communes de l’operateur logique OU ? 
```
- or
- //
``` 

Quelles sont les deux notations les plus communes de l’operateur logique NOT ? 
```
- not
- !
```

Comment fonctionne un if statement en general ? Dans quel cas l’utilise-on 
```
Le If statement permet d'effectuer des actions si une condition est vraie.

if (condition) {
    // code si condition est vraie
} else if (condition_2) {
    // code si condition est fausse et condition_2 est vraie
} else {
    // code si condition 1 et 2 sont fausses
}
```

Comment fonctionne un switch/match statement en general ? Dans quel cas l’utilise-on 
```
Le Switch/Match ne s’utilise pour remplacer le If dans le cas ou l’on verifie plusieurs egualitees uniquement.

switch(value) { 
    case 1: 
        // code si value == 1 
    case 2: 
        // code si value == 2
    case _:
        // code si aucun case n'est vrai
}  
```

Comment fonctionne une boucle for en general ? Dans quel cas l’utilise-on ? 
```
Permet de faire des itermations a traver une variable 'int' qui augmente ou diminue au cours des iterations.

for (int value = x; condition sur value; modif a chaques iterations) { 
    // code qui sera execute a chaque iterations 
}
```

Comment fonctionne une boucle while en general ? Dans quel cas l’utilise-on ? 
```
Permet de faire des iterations tant que ca condition est vraie 

While (condition) { 
    // code execute a chaques boucles 
} 
```

Comment fonctionne une boucle DO while en general ? Dans quel cas l’utilise-on ? 
```
Permet de faire des iterations  tant que ca condition est vraie en plus d’etre executer au moins une fois si elle est fausse. 

Do { 
    // code execute a chaques boucles 
} while (condition)
```

Comment fonctionne une boucle foreach ? Dans quel cas l’utilise-on ? 
```
Permet de faire une iteration sur chaques element d’un array

Foreach (element in array) { 
    // code de la boucle avec l’element sous forme de variable 
}
``` 

Qu’est-ce qu’une variable ? 
```
Un nom qui permet d’acceder a un emplacement dans la memoire centrale.
```

Quelles sont les trois interdictions communes a chaques languages dans le nommage des variables ? 
```
- Pas d’espaces 
- Ne demarre pas par un chiffre 
- N'utilise pas un nom reserve par le language
``` 

Qu’est-ce qu’un language au typage dynamique ? 
```
Le typage des variables est implicite au language (automatique)

Ex: Python
variable = 2
```

Qu’est-ce qu’un language au typage statique ? 
```
Le typage des variables est explicite au language (le dev doit le preciser)

Ex: Typescript 
variable: int = 3
```

Qu’est-ce qu’un language au typage faible 
```
Les variables PEUVENT chager de TYPE au cours de l'execution du programme

Ex: Python 
variable = 3 
print(variable) 
variable = “hello” 
print(variable)
```

Qu’est-ce qu’un language au typage fort ? 
```
les variables ne PEUVENT PAS changer de TYPE au cours de l'execution du programme.

Ex: Typescript 
variable: int = 34 
variable = “Hello” 
CE CODE PRODUIT UNE ERREUR.
```

Quel est la difference entre la declaration, l'affectation et l'initialisation d'une variable ?
```
- Declaration: Signifier au programme que la variable existe
- Affectation: Placement d'une valeur dans une variable
- Initialisation: Donner une valeur a une variable au moment de la declaration
```