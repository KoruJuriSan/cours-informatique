
# Prise de note - elec - N01

### les unites

#### Apere-heure

un ampere-heure (Ah) = 3600 Coulombs (C)

#### Vitesse

V = d / t

- V = Vitesse
- d = distance
- t = temps

#### Sous-Multiples

| prefixe | symbole | rapport |
| ------- | ------- | ------- |
| deci    | d       | 10^-1   |
| centi   | c       | 10^-2   |
| mili    | m       | 10^-3   | 
| micro   | u       | 10^-6   | 
| nano    | n       | 10^-9   |
| pico    | p       | 10^-12  |
| femto   | f       | 10^-15  |
| atto    | a       | 10^-18  |

#### temps

- 1 heure => 60 minutes
- 1 minutes => 60 secondes
- 1 seconde => 100 mili-secondes

> ex: 1 heure => 3600 secondes

#### Generateur

- generateur CC: dipole actif. Il fournis l'energie.

- force electromoatrice: la diference de potenteil entre les deux poles met en mouvement les electrions libres. (Volt)

#### Pile

- pile: generateur CC

U = V<sub>P</sub> - V<sub>N</sub>

- V<sub>P</sub> = manque d'electrons
- V<sub>N</sub> = eces d'electrons
- U<sub>PN</sub> = difference de potentiel

#### Poentiel electrique

U = W / Q

- U = potentiel electrique
- W = travail electrique
- Q = Quantite de charge

### Courant

Courant = Intensite (I) = Ampere

I = Q / t

- Q = Coulombs
- t = temps en secondes

### Resistance

Resistance: L'aptitude d'un materiau a s'opposer au passage du courant = R = Ohms

#### Loi de pouillet
R = p.l / S

- p = raw = Resistance du materiaux
- l =  longeur en m,
- S = Surface du conducteur en m<sup>2</sup>

#### Loi de Mathiessen
R<sub>T</sub> = R<sub>0</sub>(1 + a.T)
- R<sub>T</sub> = Resistance a une certaine temperature (Ohms).
- R<sub>0</sub> = Resistance sans le facteur de temperature. (Ohms)
- a = Coef de temperateure du materiaux (alpha)
- T = Temperature en degre Celsius

#### Representation

- Resistance classique: `__/\/\/\__` (Resistance)
- Resistance purement calorique: `__|⎻|_|⎻|__` (Chauffage)

#### Couleur des resisatances.

| Color   | cent  | dix   | unit | multi Ohms | Tolerance |
| ------- | ----- | ----- | ---- | ---------- | --------- |
| Noir    | 0     | 0     | 0    | 1 Ohm      | -         |
| Marron  | 1     | 1     | 1    | 10 Ohms    | ±1%       |
| Rouge   | 2     | 2     | 2    | 100 Ohms   | ±2%       |
| Orange  | 3     | 3     | 3    | 1 kOhm     | -         |
| Jaune   | 4     | 4     | 4    | 10 kOhms   | -         |
| Vert    | 5     | 5     | 5    | 100 kOhms  | ±0.5%     |
| Bleu    | 6     | 6     | 6    | 1 MOhm     | ±0.25%    |
| Violet  | 7     | 7     | 7    | 10 MOhms   | ±0.1%     |
| Gris    | 8     | 8     | 8    | 100 MOhms  | ±0.05%    |
| Blanc   | 9     | 9     | 9    | 1 GOhm     | -         |
| Or      | -     | -     | -    | 0.1 Ohm    | ±5%       |
| Argent  | -     | -     | -    | 0.01 Ohm   | ±10%      |

##### Sous-tableaux

Hierarchie des couleurs.
| Color   | Unit | Ohms       |
| ------- | ---- | ---------- |
| Argent  | -    | 0,01       |
| Or      | -    | 0,1        |
| Noir    | 0    | 1          |
| Marron  | 1    | 10         |
| Rouge   | 2    | 100        |
| Orange  | 3    | 1k         |
| Jaune   | 4    | 10k        |
| Vert    | 5    | 100k       |
| Bleu    | 6    | 1M         |
| Violet  | 7    | 10M        |
| Gris    | 8    | 100M       |
| Blanc   | 9    | 1G         |

Hierarchie des Tolerances.
| Color  | Tolerance |
| ------ | --------- |
| Gris   | ±0.05%    |
| Violet | ±0.1%     |
| Bleu   | ±0.25%    |
| Vert   | ±0.5%     |
| Marron | ±1%       |
| Rouge  | ±2%       |
| Or     | ±5%       |
| Argent | ±10%      |



#### Sens du courant electrique

- Le courant va du - au + en physique
- Le courant va du + au - dans les conventions

#### Ne pas faire

- fermer un circuit avec un generateur uniquement.

## Exo

1. Pendant combien de temps faut-il faire passer un courant de 0,5A pour que la charge delivree soit de 5000C ?

2h46
- I = Q / t
- 0,5A = 5000C / t
- t = 5000C / 0,5 = 10000s
- 10000s = 2h 46m 40s

2. Quelle est la quantite de charge transportee par un courant de 5A pendant 3s en C et en A.h

- I = Q / t
- 5A = Q / 3s
- 5A*3s = 15C
- 1Ah = 3600C
- Ah = 15 / 3600
- Ah = 4,167 * 10<sup>3</sup>

3. Quelles sont les valeurs des courants a prevoir pour delivrer une charge de 60 Ah ? pour 20s, 20min, 20h

- Ah = I * ts/3600
1. 60 = I * 20s/3600
2. 60 = I * 20m/60
3. 60 = I * 20
- I = 60 / (ts/3600)
1. 60 / 20s/3600 = 10800A
2. 60 / 20m/60 = 180A 
3. 60 / 20 = 3A