
# Prise de note - prog - N08

### Extension de fichier

#### Types de compresions

- sans perte: Aucune perte des donnees d'origine (fichiers textes, archives, configurations), algos (LZW Huffman RLE
)

- avec perte: Perte de certain fragments des donnees d'origine ()

#### LZW

#### Huffman

1. On compte la frequence d'apparition d'un char
2. On les mets dans l'ordre croissant
3. On cree un arbre binaire (deux branches max) avec l'addition des deux plus petits, ex:
4. On recommence l'etape trois jusqu'a n'avoir qu'un seul arbre

> Dans le fichier final, on met l'arbre, dans la compression finale

#### RLE

## Exo

Decompresse avec l'arbre de Huffman suivant

Arbre de Huffman:
```
  0       1
t | 1   e | 1
s | 1   a | n
l | o   
```

10 | 10 | 00 | 10 | 111 | 010 | 00 | 10 | 00 | 010 | __011__
- eetenstets
00 | 10 | 0110 | 111 | 10 | 00
- telnet
00 | 10 | 010 | 00
- test
00 | 10 | __0__
- te

states, notes

states: 010001100010010
notes: 11101110010010


Realiser l\arbre d'huffman pour les frequences suivantes:
E : 102
A : 64
C : 35
G : 12
S : 48
T : 35
H : 9

H : 9 | G : 12 | C : 35 | T : 35 | S : 48 | A : 64 | E : 102

HG: 21 | C: 35 | T: 35 | S : 48 | A : 64 | E : 102
T: 35 | S : 48 | HG-C: 56 | A : 64 | E : 102
HG-C: 56 | A : 64 | TS: 83 | E : 102
TS: 83 | E : 102 | HG-C-A: 120
HG-C-A: 120 | TS-E: 185
HG-C-A--E-TS: 305

```
  0       1
A | 1   E | 1
C | 1   T | S
H | G   
```

copresse et decompresse la suite de char suivante en LZ:

TOBEORNOTTOBEORTOBEORNOT
