
# Prise de note - cours - Nxx

### PEP

Zen in python:
```py
import this
print(this)
```

#### Ne pas faire

- Ne pas reinventer la roue.

- des code iteratif en imperatif.
```py
my_list = [1, 2]

if (my_list[0] == 1):
    ...
if (my_list[1] == 1):
    ...
```

- des if imbriques (mieux if else ou if return)
```py
if (c1):
    if (c2):
        if (c3):
        else:
    else:
else:
```

- plus de trois niveau d'indentation.
```py
if (c1):
    if (c2):
        if(c3):
            if(c4):
```

- nom de variable sans signification (a, b, c)
```py
a = 1
b = "Hello"
c = 3.4
```

- importer des sous methodes
```py
from x.y import z
```

- pass les except en python.
```py
```

- importer tout un module en python
```py
from x import * # import all du module x
```

- indentation des crochets de listes / tableaux au mauvais niveau.
```py
my_list = [
    1, 2, 3,
    4, 5, 6,
    ] # mauvais niveau.
```

- faire des ligne trop longue (72+ char)
```py
print("Lorem Lorem Ispum dolor sit amet Lorem Ispum dolor sit amet Lorem Ispum dolor sit amet Ispum dolor sit amet")
```

#### Choses a Faire

- Utiliser des modules pour faire des choses au lien de reinventer la roue.

- faire des code iteratif si ca fait gagner de l'espace.
```py
my_list = [1, 2, 3]

for e in my_list:
    if(e == 1):
        ...
```

- des nom de variable explicites (firstname, age, price).
```py
firstname = "Jack"
age = 15
price = 32.99
```

- Espace apres certain statement.

    - faire un cas pour chaques erreurs dans les excepts.

    - un espace apres: importation, declaration de variable, while, for, if, match

```py
from x import y
from z import a

firstname = "Jack"
lastname = "Paul"

def test():
    return 0


while True:
    if True:
        break
```

- Documenter son code (docstrings)



- deux espace apres: fonctions, classes

#### important

indentation en python: 4 spaces.

72 characters in one line max.

Docstring, c'est une documentation d'un code en inline.
```py
"""
Un docstring en python.
"""
```

Commentaire, c'est du texte visible dans le code, mais pas dans le programme final ou dans la doc.
```py
# Un commentaire en python.
```

### Big data

#### data generation

- Stocker une grande quantiter de donnees et traiter / ranger / categoriser ces donnees.

#### Grosse base de donnees

- Security by design: mise en place de sercurite par la difficulter.

- regle des cinq neuf: 99.99% des cas ca doit fonctionner.