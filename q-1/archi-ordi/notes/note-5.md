
# Prise de note - archi-ordi - N05

### RAM / Random Acces Memory

Caches/Registres CPU > RAM > HDD/SSD

stocke des donnees

#### SDRAM () vs DRAM ()

SDRAM: Rapide, souvant dans les CPU, Chers, Moins dense
DRAM: Moins Rapide que SDRAM, souvant dans les barretes RAM classique, besoin d'etre constement alimente. Meilleure densite, Moins chers

#### Points important achat

1. !!! Type de memoire. (DDRx, compatibilite CPU et Carte mere)
2. !!! Format. (UDIMM(Desktop) SO-DIMM)(Laptop)
3. !! Capacite.
4. !! Frequence.
5. ! Latence.
6. ! Dual Ranks
7. ! Refroidissement
8. Desgin

Bureautique: ~4Go-8Go
Gaming: ~8Go-16Go => 32Go futurproof
Rendu: ???
Serveur: ~4Go-4To => en fonction de l'utilisation

#### Multiranks

Singlerank: grand publique, une seul sortie pour la RAM

Dualrank: grand publique, Sortie de la RAM separe en deux

Multirank: serveurs, Plusiseurs sorties de la RAM

#### Multi-Channel Dual-channel

Dual-Channel :permet d'acceder a des couples de barettes de RAM.
!! MEME RAM PAR COUPLE OU BRIDAGE A LA MOINS BONNE !!

Multi-Channel: permet d'acceder a plusieurs barrettes de RAM en meme temps.

utlise a savoir
```
Deux 8Go dual channel = MOINS CHERS = MIEUX
Un 16Go = PLUS CHERS = MOINS BIEN

diff de perf ~-10% jeux
diff de perf ~-20% logiciel
```

#### UDIMM vs RDIMM

UDIMM = Ram classique, gestion de l'adressage par le CPU, domestique
RDIMM = RAM + puce de gestion d'adressage a la place du CPU, serveurs

#### Sources d'erreurs en informatique

1. Utilisateurs
2. Developpeurs
3. Pannes/Usures materielle
4. bit-flips (bits qui changes de valeurs tout seul)

#### Memoires ECC
Memoire qui ajoute des bits de detections d'erreurs, serveurs
evite les bit-flips

#### Quand la RAM deborde.

SWAP: Stocke des donnees sur le disque dur si la RAM deborde

#### Meilleurs RAM classiques.

DRAM < SDRAM < DDR < DDR2 < DDR3 < DDR4 < DDR5

#### Meilleurs RAM de cartes graphiques

...

### La RAM DDR

Double Data Rate
```
/⎻\_/⎻\_/⎻\_/⎻\_/⎻\
```

#### Formules lie a la RAM

debit = frequence * largeur_bus
!! Certains logiciels affiche une frequence /2 !!

#### Utilite d'avoir plus de RAM.

La Quantite de RAM est utilse seulement si une quantite moindre deborde, sinon ne change rien.

#### Terme lie a la RAM.

Memoire RAM : Random Acess Memory, information peut etre accedee directement (adresse aleatoire)
Memoire vive: est sollicite pendant les calculs du CPU
Memoire volatile: perte de toutes les donnees si plus alimente.

#### Acces aux donnees de la RAM

Command ACTIVE = requete lecture
Command RAS (Row Acces Strobe) = Requete

#### Latence de la RAM

...

#### UDIMM ECC SO DIMM et RDIMM en meme temps dans la synthese

### HDD et SSD

HDD = Disque dur mechanique
SSD = Disque dur electronique
SSHD = HDD incluant un petit SSD
eMMC = Stockage soude carte mere
USB drive

#### HDD

plateau qui contient les donnees
tete de lecture/ecriture / electro-aimants
plus le disque tourne vite plus de debit et moins de latence.
plus de debit vers l'exterieur du plateau


#### Choix HDD

1. Debit
    1. Taille 2.5" ou 3,5"
    2. Vitesse e rotation
    3. Nombres de plateaux
    4. Densite
        - Radiale en tpi = ?
        - Lineare en bpi = ?
        - Surfacique en Bi^2
5. Techno enregistrement (SMR ou PMR)
6. Inteface (SATA ou SAS)
7. Latence
8. IOPS
9. Cache

