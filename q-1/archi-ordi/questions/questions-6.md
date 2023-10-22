Quelles sont les deux grandes technologies d'ecriture sur un HDD ? Quel est la difference entre elles.
```
- PMR (Perpendicular Magnetic Recording): ecriture normale (plus utilise)
- SMR (Shingled Magnetic Recording): superposition des donnees (plus efficace pour l'archivage)
```

Quelles sont les differents duplex sur un HDD ?
```
- Half duplex: ecriture et lecture pas en meme temps
- Full duplex: ecriture et lecture possible en meme temps
```

Comment calculer le temps d'acces reele d'un HDD ?
```
temps moyen: temps de deplacement des tetes
temps de latence: rpm / 2
temps d'acces reele: temps moyen + temps de latence
```

Qu'est-ce que la fragmentation d'un HDD ?
```
L'eparpilation d'une ou plusieurs donnees liees entre elles sur l'HDD, ce qui rend la donnees plus longue a traiter.
```

Qu'elle sont les deux methodes d'acces aux donnees sur un HDD ou SSD ? Donne un avantage du SSD en rapport avec ces methodes.
```
- sequentiel: donnees contigue, plus rapide (HDD == SSD)
- direct: donnees non contigue, plus lent (HDD extremement lent)
```

Comment bien effacer les donnees d'un HDD ?
```
Il faut le reecrire entierement au MOINS 7 fois (mieux plus)
```

Donne le temps de retention min d'un HDD.
```
5ans
```

Donne le temps de retention moyen d'un SSD
```
1-10ans
```

Quels sont les quatres types de SSD quand on parle de duree de vie ? Donne les dans l'ordre du meilleur au pire.
```
1. SLC
2. MLC (certains TLC ou QLC sont confondus MLC)
3. TLC
4. QLC
```

Qu'est-ce que fait le wear leveling sur un SSD ?
```
Il reparti les donnees pour eviter d'utiliser tout le temps les meme cells.
```

Qu'est-ce qu'une page et un bloc dans un SSD ?
```
Page : La plus petite unité de stockage d'un SSD.
Bloc : Un nombre prédéfini de pages rassemblées ensemble.
```

C'est quoi le principe de RAID sur les disques de stockages ?
```
assemblage de disque physique pour faire un seul disque logique.
```

Quels sont les trois grands moyen de mettre en place un RAID sur des disques dur ?
```
Logiciel: depend d'un logiciel en particulier
Pseudo-Materiel: depend d'une carte mere percise
Materiel: depend d'une carte externe

la dependance dit que si le materiel lache il faudra avoir exactement le meme (logiciel, carte mere ou carte externe) pour pouvoir recup les donnees du RAID.
```

Quels sont les deux types de BIOS possible ?
```
- BIOS: Ancien, avec moins de fonctionnalites
- UEFI: Nouveau, avec plus de fonctionnalites (curseur par exemple)
```

Ou son garder les parametres du BIOS ?
```
dans la puce CMOS (RAM)
```

Par quoi est alimenter la puce CMOS ?
```
Pile CMOS
```

Donne le nombre d'ecriture par cells moyen d'un SSD SLC.
> card type: entry
```
100.000
```

Donne le nombre d'ecriture par cells moyen d'un SSD MLC.
> card type: entry
```
10.000
```

Donne le nombre d'ecriture par cells moyen d'un SSD TLC.
> card type: entry
```
3.000
```

Donne le nombre d'ecriture par cells moyen d'un SSD QLC.
> card type: entry
```
1.000
```

Quelle connectique utilise-on sur les vieux HDD / Lecteur de CD ?
> card type: entry
```
IDE
```