Comment sauvegarder des donnees de son programme meme si il n'est pas lance ?
> card type: entry
```
fichier
```

Donne la definition d'un fichier informatique.
```
Une unite de stockage logique de donnees avec un nom et une extension (format).
```

Explique ce qu'est un systeme de fichier. (description)
```
partie du systeme d'exploitation responsable de la gestion des fichiers logiques et de leurs droits d'acces. C'est une partition sur le disque de stockage
```

la difference entre le chemin absolu ou relatif d'un fichier ?
```
- Absolu: Depend du root (linux: /, windows: C:/)
- Relatif: Depend de l'emplacement actuelle dans le prgoramme. (Plus utile)
```

Donne les quatres methodes les plus utiliser quand a l'ouverture d'un fichier en programmation.
```
- read
- write
- append
- create
```

Quel est l'une des chose a ne surtout pas oublier quand on ouvre un fichier dans un programme ?
```
de le fermer le plus vite possible.
```

Quels sont les deux methodes possible pour la sauvegarde de donnees dans un fichier ?
```
- save manuelle / a la fin d'un programme. (moins gourmand en ressources)
- save auto, quand une donnee est modifie. (sauvegarde automatique, plus gourmand)
```

Que ce passe-il quand j'essaye de lire un fichier qui est en train d'etre lu par un autre programme ?
```
Une erreur
```

Que ce passe-il quand j'essaye de lire un fichier qui n'existe pas ?
```
Une erreur
```

Que ce passe-i quand j'essaye de lire un fichier qui viens d'etre fermer par un autre programme ?
```
Fonctionne correctement.
```

C'est quoi un try catch statement en programmation ?
```
Il permet de tester d'executer un code et de reagir si il y a une erreur dans la partie teste.

ex: python

try:
    # code teste.
except:
    # code si il y a une erreur dans le try.
else:
    # code si il n'y pas eu d'erreur dans le try.
finaly:
    # toujours execute.
```

Qu'est-ce que le 'test first' en programmation ?
```
c'est le fait d'ecrire les testes avant l'integration.
```

En general, c'est quoi un test unitaire ?
```
test d'un module / d'une fonction, on test si le result est celui voulus (range ou preceis) pour une entree precise.
```

En general, c'est quoi un test d'intergration ?
```
On test si les fonctionnalite fonctionnent bien entre elles etapes par etapes.
```

En general, c'est quoi un test de regression ?
```
On verifie si les nouvelles fonctionnalite ne crees pas de bugs avec les anciennes. Il n'est presque jamais utilise car long et dur a mettre en place. 
```

Le code est plus souvant lus que ecrit. Quel est la chose la plus importante a faire pour que le developpeur qui lit le code ne soit par perdu ?
```
Documenter le code.
```