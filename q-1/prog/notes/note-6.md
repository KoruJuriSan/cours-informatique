# Prise de note - prog - N06

### Les fichiers

Permet de stocker les donnees meme si le programme n'est pas lance.

Fichier: Une unite de stockage logique avec un nom et une extension (format). 

Systeme de fichier: partie du systeme d'exploitation responsable de la gestion des fichiers et droits.

Chemin relatif: Chemin qui ne depend pas du root (./Documents SI JE SUIS DANS user.)
Chemin Absolu: Chemin qui depend du root (/home/user/Documents/...) !! PAS FOU !!

Flux de donnees: Methode tranparente et unifiee d'envoi et reception de donnees

#### Comment ouvrir un fichier en prog ?

methodes d'ouvertures: r=read, w=write, a=append, x=create

- read: lire
- write: ecrire au debut (ecrase les donnees)
- append: ecrire a la fin
- create: cree un fichier

> !! QUAND ON OUVRE UN FICHIER ON LE FERME LE PLUS VITE POSSIBLE !!

#### L'ecriture de fichier.

1. Stocker toutes les donnes au fur et a mesure du programme, puis save tout d'un coups dans un fichier, plus opti.
2. Ecrire au fur et a mesure de l'utilisation du programme, save auto.

#### Erreurs

Produit une erreur:

- On ne peut pas lire un fichier qui est en cours d'utilisation en meme temps ailleurs.

- On ne peut pas lire un fichier qui n'existe pas.

Structure defensive:

- prevois les erreurs et on donne un resultat different en consequence. ex: try catch

#### Try catch

est execute si:

- try: toujours
- except: si il y a une erreur dans le try
- else: si il n'y a pas d'execpt
- finally: toujours

### Module

```__init__.py``` : indique que le repo est un pk, python

### Testing

les tests sont dans leurs propres fichiers a part

test-first = ecrire les tests avant d'intergrer

type de tests:
Tests unitaires.
Tests d'intergration
Tests de regression

#### Tests unitaires

Test le bon fonctionnement d'un module / d'une fonction

1. Initialise l'environnement de test
2. Execution du module de test
3. Verification des resultats obtenus et dit si il est reussi ou non. !! on peut metre en place une marge d'erreur ex: 1 >= result >= 0 !!
4. Desactivation: desinstallation des fixtures pour retrouver l'etat initial du systeme, pour ne pas polluer les tests suivants. TESTS independants

#### Tests d'intergration

Test le bon fonctionnement de fonctionnalites d'un programme ensemble.

Differentes approches:
- Top-Down
- Bottom-up
- Big-Bang
- ...

suite Quad-2

#### Tests de regression.

Verification, que de nouvelles fonctionnalite ne cree pas de bugs avec des anciennes.

longs et dur. PRESQUE JAMAIS UTILISE

### Documentation

Il est important de documenter le code.
