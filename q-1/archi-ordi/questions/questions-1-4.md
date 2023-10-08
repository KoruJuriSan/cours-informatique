Niveau d'un transistor comment on a un 1 ou un 0 logique ?
    - Tension: 0-3 = 0 logique
    - Tension: 3-6 = 1 logique

Qu'est-ce qu'une valeur logique ? Que peut-il contenir ?
    - un bit
    - un 0 ou un 1 (binaire)

Quel est la base du binaire ?
    - base 2

Quel est la base de l'octale ?
    - base 8

Quel est la base du decimal ?
    - base 10

Quel est la base de l'hexadecimal ?
    - base 16

Combiens de bits faut-il pour faire une valeur en octal ?
    - trois bits
    - xxx binaire => x octal

Combiens de bits faut-il pour faire une valeur en hexa ?
    - quatres bits
    - xxxx binaire => x hexa

Comment convertir le binaire en decimal et viseversa ?
    - | ... | 256 | 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
    - | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    - | 1/0 | 1/0 | 1/0 | 1/0 | 1/0 | 1/0 | 1/0 | 1/0 | 1/0 | 1/0 |
    -
    - On fait l'addition de tout les decimal (ligne du haut)
    - SI le binaire du dessous est == a 1 sinon on passe au suivant.
    - !! Tableau commence par la droite !!

Comment appelle-on le premier bit d'un nombre binaire ?
    - bits de poid fort

comment fait-on une soustraction en binaire ?
    - xxxx - yyyy
    - A1 yyyy = NOT yyyy
    - A2 yyyy = A1 + 1
    - xxxx - yyyy = xxxx + A2 yyyy = a/zzzz 
    - on supprime ce qui depasse (a)

Fait la soustraction binaire suivante: 1010-0111
    - 11 = 3

Comment passer du binaire a l'hexa et visevera ?
    - binaire => hexa
    - on divise la chaine de binaire en morceaux de quatre (commence a droite)
    - xyyyyzzzz => 000x yyyy zzzz
    -
    - on calcul la valeur de chaque morceau en decimal (0-15)
    - 000x => x
    - yyyy => y
    - zzzz => z
    -
    - si la valeur > 9 alors on transforme en lettre dans l'ordre alphabetique (A-F). et on met les valeurs les une a cote des autres.
    - xyz
    -
    - Pour faire de l'hexa au binaire faites le meme mais inverse.

Comment passer du binaire a l'octal et viseversa ?
- binaire => hexa
    - on divise la chaine de binaire en morceaux de quatre (commence a droite)
    - xyyyzzz => 00x yyy zzz
    -
    - on calcul la valeur de chaque morceau en decimal (0-7)
    - 00x => x
    - yyy => y
    - zzz => z
    -
    - On met les valeurs les une a cote des autres.
    - xyz
    -
    - Pour faire de l'octal au binaire faites le meme mais inverse.

Que fait l'operation mathematique modulo ?
    - donne le reste d'une division entiere.

Qu'est-ce que l'ASCII ? sur combiens de bits est-il encode ? que fait le derrnier bits ?
    - premier caractere d'ordinateur cree par les americains
    - 8bits = 7 + 1 parite

Que fait l'operateur logique NOT ?
    - il inverse l'entree
    - 1 => 0
    - 0 => 1

Que fait l'operateur logique AND ?
    - il retourne VRAI si l'entre A et B sont vrais
    - 0, 0 => 0
    - 0, 1 => 0
    - 1, 0 => 0
    - 1, 1 => 1

Que fait l'operateur logique OR ?
    - il retourne VRAI si l'entre A et/ou B sont vrais
    - 0, 0 => 0
    - 0, 1 => 1
    - 1, 0 => 1
    - 1, 1 => 1

Que fait l'operateur logique XOR ?
    - il retourne VRAI si l'entre A ou B sont vrais
    - 0, 0 => 0
    - 0, 1 => 1
    - 1, 0 => 1
    - 1, 1 => 0

Que fait l'operateur logique NOR ?
    - il retourne VRAI si l'entre A et B sont faux
    - 0, 0 => 1
    - 0, 1 => 0
    - 1, 0 => 0
    - 1, 1 => 0

Que fait l'operateur logique HAND ?
    - il retourne VRAI tant que A et B sont pas vrais
    - 0, 0 => 1
    - 0, 1 => 1
    - 1, 0 => 1
    - 1, 1 => 0

Que fait l'operateur logique XNOR ?
    - Il retourne VRAI si A et B sont vrais ou faux
    - 0, 0 => 1
    - 0, 1 => 0
    - 1, 0 => 0
    - 1, 1 => 1

Quels sont les deux taches principales qu'effectue le CPU ?
    - fait des calculs
    - deplace des donnees

Quels sont les composants d'un cpu ?
    - Bus de donnees
    - Unite d'entre sortie
    - Coeur(s)
    - Cache L3
    - Unite de controle du CPU

Quels sont les composants d'un coeur de CPU ?
    - Bus de donnees
    - Unite d'entre sortie
    - Unite de controle du coeur
    - ALU (Arithmetic Logic Unit)
    - FPU (FLoating Point Unit)
    - VPU (Vector Processing Unit)
    - Cache L2
    - Cache L1
    - Registres

Qu'est-ce qu'un thread de CPU techniquement ? (definition)
    - Une memoire dans un coeur de CPU qui conserve des information d'une action precedente pour en traiter une autre et alterner entre les deux au fur et a mesure du temps. Divise un coeur en plusieurs taches. C'est des coeurs virtuels

Qu'est-ce que le parallelisme ? (niveau des cpu) quels sont les trois types ?
    - le fait de pouvoir effectuer plusieurs taches en meme temps.
    -   1. Multiprocesseurs
    -   2. Multicoeurs
    -   3. Multithreading

Que sont les CPU superscalaires ? (definition)
    - Execute plusieurs instructions en meme temps si elles ne dependent pas les une des autres. C'est l'unite de controle qui verifie si il a dependance ou non.
    -
    - exemple:
    - ligne 1: a besoin de l'ALU
    - ligne 2: a besoin du FPU
    - !! Ligne 2 ne depend pas de ligne 1
    -
    - Alors ils peuvent etre execute en meme temps.

Quels est l'unite qui calcul l'efficacite d'un coeur de CPU ?
    - IPC = Instruction Per Cycles

Il y deux type de coeurs quand on parle perfomrance, il servent a quoi ? quels sont leurs differences ?
    - Petits coeurs = --Energie = --Performants
    - Grands coeurs = ++Energie = ++Performants
    -
    - les petits permettent de consommer moins de batteries dans les portables.

Quels est la latence moyenne des registres du CPU ?
    - 0,02ns

Quels est la latence moyenne du cache L1 du CPU ?
    - 2ns

Quels est la latence moyenne du cache L2 du CPU ?
    - 5ns

Quels est la latence moyenne du cache L3 du CPU ?
    - 20ns

Quels est la latence moyenne de la RAM ?
    - 60ns

Quel est le debit moyen du cache L1 ?
    - 210Go/s

Quel est le debit moyen du cache L2 ?
    - 80Go/s

Quel est le debit moyen du cache L3 ?
    - 60Go/s

Quel est le debit moyen de la RAM ?
    - 40Go/s

Pourquoi on n'utilise pas des Registres partout a la place de la RAM ? Qu'en est-il des caches L1,2,3 ?
    - car les registres coutents beacoup plus chers.
    - Les cahces L1,2,3 sont moins chers mais toujours trop chers pour en avoir en meme quantite que la RAM

Comment reconnaitre un scoket AMD et Intel ?
    - les sockets AMD ~= AAx
    - les sockets Intel ~= xxxx
    - x = chiffre
    - A = Lettre

Ces sockets sont des sockets de chez ? 1090, 1356, 2066, 1151
    - Intel
    - format: xxxx

Ces sockets sont des sockets de chez ? FP5, FP6, SP3, TRx4
    - AMD
    - format: AAx
    - SAUF POUR TRx4 qui vient bien d'AMD.

Que fait le CPU si la temperature de celui-ci depasse une certaine limite ?
    - Le CPU ce bride automatiquement pour produire moins de chaleur

Que signifie l'Overclocking d'un CPU ? (definition)
    - Augmentation de frequence d'horloge du CPU pour augmenter la cadence de celui-ci !! PLUS DE CHALEUR !!

Que signifie l'Undervolting d'un CPU ? (definition)
    - Reduction du voltage du CPU pour diminuer la temperature de celui-ci, Reduit la puissance du CPU au passage.

Que fait le Turboboost d'un CPU ? (definition)
    - Overclocking automatique si on n'utilise moins de coeurs. Moins on utilise de coeurs plus l'overclocking est eleve, plus on utilise de coeurs, moins l'overcloking est eleve.

Qu'est ce que le Throttling d'un CPU ? (definition)
    - Processeur qui se met en econnomie pour diminuer la temperature de celui-ci, puis qui une fois descendu reactive son mode normal et rechauffe donc retombe en mode econnomie....

Qu'est-ce que le TDP d'un CPU ? Que signifie T-D-P ?(definition)
    - Termal Design Power
    - Puissance d'un CPU en watts / Production de chaleur

Donne la formule du TDP. Que signifie chaques elements ?
    - K . V^2 . f
    - K = constate qui depend du CPU
    - V = tension
    - f = frequence

Que fait le pipeline du CPU ? (definition)
    - Decoupe un processus en differents types d'instructinos et fait des predictions sur des futures valeurs possibles.

Quelle sont les cinq types d'instructions du principe de pipeline du CPU ?
    - IF (Instruction Fetch)
    - ID (Instruction Decode)
    - EX (Execute)
    - MEM (Memory)
    - WB (Write back)

Dans le principe de pipeline du CPU, le flush, c'est quoi ?
    - Le principe de faire des predictions sur des futures valeurs

Dans le principe de pipeline du CPU, l'instruction IF, elle fait quoi ?
    - Elle charge une instruction depuis la memoire

Dans le principe de pipeline du CPU, l'instruction ID, elle fait quoi ?
    -elle decode l'instruction pour savoir quell operation devra etre execute

Dans le principe de pipeline du CPU, l'instruction EX, elle fait quoi ?
    - Execute l'instruction, effectue les calculs

Dans le principe de pipeline du CPU, l'instruction MEM, elle fait quoi ?
    - Ecrit ou lit dans la memoire si necessaire

Dans le principe de pipeline du CPU, l'instruction WB, elle fait quoi ?
    - Ecrit le resultat dans les registres du CPU

Qu'est-ce que le developpeur peut faire avec le principe de pipeline du CPU ?
    - Rien.

Qu'est-ce qu'un logiciel de Benchmark ?
    - Un logiciel qui effectue des test de performances sur un ordinateur.

Qu'elles sont les deux types benchmark ? Quels sont leurs differences ?
    - synthetique: evalue les performances de maniere simplifiee, tests brut non representatifs.
    - applicatifs: evalue les performances en pratique avec des tests sur des logiciels et jeux.

Si je prend un cpu pour jouer a des jeux video, je prefere donner la priorite au nombres de coeurs ou la frequence de mon CPU ?
    - Frequence+++

Si je prend un cpu pour faire du rendu, je prefere donner la priorite au nombres de coeurs ou la frequence de mon CPU ?
    - Coeurs+++