
# Prise de note - cours - N01-N04

### Binaire, Hexa, Octale, Decimal

niveau des transistors
0-3 = 0 logique
3-6 = 1 logique

une valeur logique = bit a 1 ou 0

binaire = base 2
octale = base 8
decimal = base 10
hexa = base 16 (1-F)

combiens de bits pour :
octale = 8 = xxx
hexa = 16 = xxxx

#### Language et CPU

Le seul language que comprend le CPU: Binaire.

#### Convertir binaire et decimal :
| ... | 256 | 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1/0 | 1/0 | 1/0 | 1/0 | 1/0 | 1/0 | 1/0 | 1/0 | 1/0 | 1/0 |

On fait l'addition de tout les decimal (ligne du haut)
SI le binaire du dessous est == a 1 sinon on passe au suivant.
!! Tableau commence par la droite !!

premier bit d'un nombre binaire == bit de poid fort

#### Soustractions en binaire

```
xxxx - yyyy
A1 yyyy = NOT yyyy
A2 yyyy = A1 + 1
xxxx - yyyy = xxxx + A2 yyyy !! LIMIT BY NUMBERS OF BITS !!
```
Exemple:
```
  1010
- 0111

A1 0111 = 1000

     1000
   + 0001
A2 = 1001

    1010
+   1001
= 1/0011

on retire le bit en trop a gauche
reponse = 11
```

#### Transformation binaire / hexa / octale

xxxxxxxxx<sub>2</sub> = xxx<sub>2</sub>/xxx<sub>2</sub>/xxx<sub>2</sub> = xxx<sub>8</sub>

xxxxxxxxx<sub>2</sub> = 00x<sub>2</sub>/xxxx<sub>2</sub>/xxxx<sub>2</sub> = xxx<sub>16</sub>


### Modulo

Modulo = reste d'une division entiere

### ASCII

premier caractere d'ordinateur cree par les americains
code sur 8bits = 7bits + 1bits de controle de parite(pair ou impair)

### Operateurs logiques de base

NOT / INVERSEUR logique
```
1 => 0
0 => 1
```

AND / ET logique
```
0, 0 => 0
0, 1 => 0
1, 0 => 0
1, 1 => 1
```

OR / OU INCLUSIF logique
```
0, 0 => 0
0, 1 => 1
1, 0 => 1
1, 1 => 1
```

XOR / OU EXCLUSIF logique
```
0, 0 => 0
0, 1 => 1
1, 0 => 1
1, 1 => 0
```

NOR / NOT OR logique
```
0, 0 => 1
0, 1 => 0
1, 0 => 0
1, 1 => 0
```

NAND / NOT AND logique
```
0, 0 => 1
0, 1 => 1
1, 0 => 1
1, 1 => 0
```

XNOR / NOT XOR logique
```
0, 0 => 1
0, 1 => 0
1, 0 => 0
1, 1 => 1
```

### CPU / Central Porcessing Unit

#### effectue deux taches principales:
- faire des calculs
- deplacer des donnees

#### Dans le CPU :
- Bus de donnees
- Unite d'entre sortie
- Coeur(s)
- Cache L3
- Unite de controle du CPU

#### Dans le coeur d'un CPU :
- Bus de donnees
- Unite d'entre sortie
- Unite de controle du coeur
- ALU (Arithmetic Logic Unit)
- FPU (FLoating Point Unit)
- VPU (Vector Processing Unit)
- Cache L2
- Cache L1
- Registres

### Threading

> coeurs virtuels

Une memoire dans un coeur de CPU qui conserve des information d'une action precedente pour en traiter une autre et alterner entre les deux au fur et a mesure du temps. Divise un coeur en plusieurs taches.

#### Le Parallelisme du CPU
fait de faire plusieurs taches en meme temps / cpu / coeurs / threads

  - Vrai parallelisme: coeurs / une tache par coeur

  - Faux parallelisme: threads / alternance entre plusieurs taches sur un meme coeur.

  Trois moyens de faire du parallelisme, combinables.

  1. Multiprocesseurs
  2. Multicoeurs
  3. Multithreading

### CPU superscalaire
Execute plusieurs instructions en meme temps si elles ne dependent pas les une des autres. C'est l'unite de controle qui verifie si il a dependance ou non.

ex:
```
ligne 1: a besoin de l'ALU
ligne 2: a besoin du FPU
!! Ligne 2 ne depend pas de ligne 1

Alors ils peuvent etre execute en meme temps.
```

#### Performance des Coeurs de CPU
Efficacite d'un coeur de CPU: IPC = Instructions per cycles


Il existe des coeurs plus ou moins performant / energivore
> +Perf = + Energie = plus grand
> -Perf = - Energie = plus petit

#### Stockages de donnes en interaction avec le CPU.
| Type      | Latence | Debit   | Cout   |
| --------- | ------- | ------- | ------ |
| Registres | 0,02ns  |         | ++++++ |
| Cache L1  | 2ns     | 210Go/s | +++++  |
| Cache L2  | 5ns     | 80Go/s  | ++++   |
| Cache L3  | 20ns    | 60Go/s  | +++    |
| RAM       | 60ns    | 40Go/s  | +      |

#### Sockets de CPU

| Marque | Laptop           | Desktop          | Server     |
| ------ | ---------------- | ---------------- | ---------- |
| Intel  | 1090, 1356, 1440 | 1151, 1200, 2066 | 2066, 3647 |
| AMD    | FP5, FP6         | TRx4, AM4        | SP3        |

En general:

- Intel: xxxx
- AMD : AAx

#### Overclocking, Undervolting

- Overcloking: Augmentation de la freqence d'horloge du CPU pour augmenter la cadence de celui-ci !! PLUS DE CHALEUR !!

- Undervolting: Reduction du voltage du CPU pour diminuer la production de chaleur de celui-ci !! Reduit la puissance du CPU !!

- Turboboost: Overclocking automatique si on n'utilise moins de coeurs, moins on utilise de coeurs plus l'overcloking et la frequence est eleve, plus on utilise de coeurs moins elle l'est.

- Throttling: Processeur qui se met en econnomie pour diminuer la temperature de celui-ci, puis qui une fois descendu reactive son mode normal et rechauffe donc retombe en mode econnomie....

> !! SI LA TEMPERATURE DU CPU EST TROP ELEVE ALORS IL RALENTI AUTOMATIQUEMENT POUR REFROIDIR !!

#### TDP / Thermal Design Power
Puissance d'un CPU en Watts / Production de chaleur.

> formule: KV<sup>2</sup>f
```
K = constante qui depend du CPU
V = tension
f = frequence
```

### Pipeline du CPU

Decoupe un processus en differents types d'instructions et fait des predictions sur des futures valeurs possibles (ex: if else).

types d'instructions

IF (Instruction Fetch): L'instruction est chargee depuis la memoire
ID (Instruction Decode): L'instruction est decodee pour savoir quelle operation devrra etre execute
EX (Execute): Execute l'instruction, effectue les calculs
MEM (Memory): Ecrit ou read la memoire si necessaire.
WB (Write back): Ecrit le resultat dans les registres du CPU.

Les instructions suivant peuvent etres execute en parallele, une instruction peut etre IF en meme temps qu'une autres soit ID, EX, ... Fait gagne du temps

flush: Principe de faire des predictions sur des futures valeurs.

!! Le developpeur ne peut rien y faire !!

#### Frequence vs Coeurs

- pour les jeux video: frequence+++ coeurs--

- pour les rendus: coeurs+++ frequence--

### Benchmarks

Logiciel qui evalue les performances d'un ordinateur

#### Benchmarks synthetiques

- Benchmarks qui evalue les performances de maniere simplifiee par des test brut qui ne sont pas representatifs.

#### Benchmarks applicatifs

- Benchmarks qui evalue les performances en pratique avec des tests sur des jeux, logiciels, etc...

## Exercices :

### Binaire => Decimal
101111 = 47

1111 = 15

1111101 = 125

100000000 = 256

100000 = 32

### Decimal => Binaire

13 = 001101

91 = 1011011

50 = 110010

30 = 11110

28 = 11100

### Operations en binaire

1001 * 1001 = 1011010 = 90

1111 - 1111 = 0

1010 - 0111 = 11

101 * 111 = 100011