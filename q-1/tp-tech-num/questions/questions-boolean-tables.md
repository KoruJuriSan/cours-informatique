C'est quoi une table de verite en algebre de bool ? Construit celle de l'operation "A.ˉB + ˉA.B".
```
C'est un tableau qui represente toutes les entrees possible et leurs resultats sur une Operations logique.

| A | B | S |
| - | - | - |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

On remarque que l'operation du dessus est un XOR.
```

C'est quoi une table de Karnaugh en algebre de bool ? Construit celle de l'operation "A.ˉB + ˉA.B".
```
C'est un tableau qui represente toutes les entrees possible et leurs resultats sur une Operations logique.
C'est aussi une simplification de la table de verite.

| a/b | 0 | 1 |
| --- | - | - |
|  0  | 0 | 1 |
|  1  | 1 | 0 |

On remarque que l'operation du dessus est un XOR.
```

Passe de la table de Karnaugh suivante a la fonction.
| ab/cd | 00 | 01 | 11 | 10 |
| ----- | -- | -- | -- | -- |
|    00 |  0 |  0 |  1 |  0 |
|    01 |  1 |  1 |  1 |  1 |
|    11 |  1 |  1 |  0 |  0 |
|    10 |  0 |  0 |  0 |  0 |
```
S = ˉD.B.A + CˉB + ˉD.C
```