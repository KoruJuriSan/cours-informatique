# Conversions Binary, hexadecimal, octal, decimal


## Binary, Hexadecimal, Octal and Decimal

| base | bits | range                                          |
| ---- | ---- | ---------------------------------------------- |
|    2 |    1 |                                           0, 1 |
|    8 |    3 |                         0, 1, 2, 3, 4, 5, 6, 7 |
|   10 |    - |                   0, 1, 2, 3, 4, 5, 6, 7, 8, 9 |
|   16 |    4 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F |

# Conversions

### Binary -> Octal

Example of binary: (...xxxxxxxx)$_2$ (x == 0 or 1)

1. Cut the number every **three digits** from the right: (...xx)$_2$ | (xxx)$_2$ | (xxx)$_2$
2. Calculate each piece individually (conversion table $2^n$): (...x)$_8$ | (x)$_8$ | (x)$_8$
3. Put them back together: (...xxx)$_8$

### Binary -> Hexadecimal

Example of binary: (...xxxxxxxxxx)$_2$ (x == 0 or 1)

1. Cut the number every **four digits** from the right: (...xx)$_2$ | (xxxx)$_2$ | (xxxx)$_2$
2. Calculate each piece individually (conversion table $2^n$): (...xx)$_{16}$ | (xx)$_{16}$ | (xx)$_{16}$
3. If a piece is > 9, then change the digit with the corresponding letter (10->A, 11->B, ...): (...x)$_{16}$ | (x)$_{16}$ | (x)$_{16}$
4. Put them back together: (...xxx)$_{16}$

### Hexadecimal/Octal -> Binary

Example Hexadecimal or Octal: (..xxx)$_{8/16}$ (x in [0-7] or [0-F])

...

### Binary -> Decimal

Example of binary: (...11010101)$_2$

1. Create a table of $2^n$ starting from the right where the first value of n is 0. The table length is equal to the number of digits in the binary number.

| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| --- | -- | -- | -- | - | - | - | - |
| 1   | 1  | 0  | 1  | 0 | 1 | 0 | 1 |

2. For every element of the first line with a 1 in the second line, add them together to get the decimal number.

| *128* | *64* | ~~32~~ | *16* | ~~8~~ | *4* | ~~2~~ | *1* |
| ----- | ---- | ------ | ---- | ----- | --- | ----- | --- |
| 1     | 1    | 0      | 1    | 0     | 1   | 0     | 1   |

128 + 64 + 16 + 4 + 1 = 213

### Decimal -> Binary

Example of decimal (225)

1. Create a table of $2^n$ starting from the right where the first value of n is 0. Continue the table until the result is higher than your decimal number.

| 255 | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| --- | --- | -- | -- | -- | - | - | - | - |
| x   | x   | x  | x  | x  | x | x | x | x |

2. Starting from the left now, check if the number can fit into your decimal. If it can't, leave it as 0; if it can, set it to 1 and keep it. Continue by adding the kept number to the next one, apply this algorithm until your kept number is equal to your decimal one.

| 255 | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| --- | --- | -- | -- | -- | - | - | - | - |
| 0   | 1   | 1  | 1  | 0  | 0 | 0 | 0 | 1 |

Cache = 0
255 > 225 => 0
128 < 225 => 1
Cache += 128
Cache(128) + 64 < 225 => 1
Cache += 64 = 192
Cache(192) + 32 < 225 => 1
Cache += 32 = 224
Cache(224) + 16 > 225 => 0
Cache(224) + 8 > 225 => 0
Cache(224) + 4 > 225 => 0
Cache(224) + 2 > 225 => 0
Cache(225) + 1 == 225 => 1

3. Remove not useful zero on the left. 011100001 -> ~~0~~ 11100001