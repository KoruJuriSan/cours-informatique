
# Prise de note - archi-ordi - N06

### HDD suite

#### Technologies d'ecriture HDD

PMR (Perpendicular Magnetic Recording): plus utlise, mieux pour une utilisation classique.

SMR (Shingled Magnetic Recording): Superposition de donnees, permet de stocker plus, mais obligation d'effacer l'ancienne donnes lors de la reecriture. Mieux archivage.

#### Connectique

Nape IDE < SATA I-III < SAS

Connectique SAS accepte le SATA mais pas l'inverse.

#### duplex

Half duplex: ecriture et lecture pas en meme temps

Full duplex: ecriture et lecture en meme temps

#### latences HDD

Temps moyen: temps de deplacement tetes

Temps de latence: temps entre trouver la piste et sync des data = 1/2 tour (60/rpm)/2

Temps d'acces reele: temps moyen + temps de latence

#### Fragmentation

Fragmentation: l'eparpilation des donnees dans un HDD.

Defragmentation: ...


#### Acces de donnes

Change en fonction de comment sont stocke les donnees.
- acces sequentiel: Donnees contigue, plus rapide
- acces direct: Donnees no contigue, moins rapide

#### Effacement des donnees

Il faut ecrire au moins 7 fois une donnes pour quel ne soit plus retrouvable dans le HDD.

#### Temps de retention

min 5ans

### SSD suite

#### Connectique

mSATA: mini PCI-Express, pour les portables

M.2: ...

#### Duree de vie

QLC < TLC < MLC < SLC

| Type | bits/cells | Price      | Perfs     | Write per cells |
| ---- | ---------- | ---------- | --------- | --------------- |
| SLC  | 1 bit      | Tres chers | Tres perf | ~100.000        | 
| MLC  | 2 bits     | chers      | Perf      | ~10.000         |
| TLC  | 3 bits     | Normal     | Normal    | ~3.000          |
| QLC  | 4 bits     | Cheap      | Peu perf  | ~1.000          |

Les cells d'un SSD on une limite d'ecritures avant de mourir.

- wear leveling: permet de repartir les donnees pour eviter d'utiliser tout le temps les meme cells.

#### Modification de donnes

Il faut dire la taille d'un bloc

Ne peut pas modifier un bloc, que del et add un bloc

Garbage collection: ecrit la donnees la ou il y a de l'espace et quand il le juge, il reecrira les donnees au bon endroit.

#### temps de retention

1-10ans

#### IOPS

...

### RAID

RAID: Assemblage de disque physique pour constituer un seul disque logique.

#### Type de RAID

| Type    | Disks | Ecriture  | Lecture | Risks     | Stockage |
| ------- | ----- | --------- | ------- | --------- | -------- |
| RAID-0  | 2     | x1.5~     | x1.5~   | 1d = 2d   | x1       |
| RAID-1  | 2     | x1~       | x1.5~   | 1d = fine | x0.5     |
| RAID-5  | 4     | x1~       | x1      | 1d = fine | x0.75    |
| RAID-10 | 4     | x1.5~     | 1.5~    | 2s = fine | x0.5     |

- RAID Logiciel: Logiciel qui gere le RAID avec le CPU de la machine. Besoin d'avoir un OS deja installe.
- RAID pseudo-materiel: Permet d'installer le RAID via la carte mere. Besoin d'avoir la meme carte mere si l'ancienne meurt
- RAID Materiel: Un carte externet avec CPU integre qui gere le RAID. Besoin d'avoir exactement la meme de rechange.


### Carte mere

Carte mere: Permet de faire communiquer tous les elements de l'ordinateur entre eux.

#### BIOS

installee sur une memoire ROM, premier logiciel lance au demarrage de l'ordinateur. Il gere le fonctionnement des composants de l'ordinateur. Il gere aussi l'ordre de boot.

POST: Verification des composants

#### Type de BIOS

- BIOS: Ancien, sans curseur, moins de fonctionnalites

- UEFI: Nouveau, avec curseur, plus de fonctionnalites

#### Stockage des params du BIOS

CMOS: Une RAM qui stocke les parametres du BIOS

#### Alimentation du CMOS

pile CMOS: pile qui permet de garder le CMOS alume meme si la carte est hors tension.

#### Chipset

Chipset: Gere l'information qui fait des va et viens sur la carte mere.

#### Effacer / Update le BIOS

Si le pc ne demarre pas, on peut le faire en changeant de place le jumper.

flasher le bios: Update le bios avec une autre version.

#### PCIe

Prototcol:
PCIe 1.0 - 5.0

#### Choix

compatibilite Processeur:
- socket
- gamme/version chipset (bas, moyen, haut)
- type de fixation refroidissement

RAM:
- format DIMM vs SoDIMM
- multi-channel ou non
- DDRx

Extension:
- Slot PCIe xXX

M2:
- Type de connecteur (M, B&M, B)
- Longeur (22xx)
- chipset (vitesse max accepte, risque bottleneck)
