# From Truth Table to Logical Formula

### Truth Tables

- For x input values with a single value between 1 and 0, all possibilities are given.

Example with XOR.
| a | b | result |
| - | - | ------ |
| 0 | 0 |   0    |
| 0 | 1 |   1    |
| 1 | 0 |   1    |
| 1 | 1 |   0    |

More complex example. (3 input variables)
| a | b | c | result |
| - | - | - | ------ |
| 0 | 0 | 0 |   0    |
| 0 | 0 | 1 |   1    |
| 0 | 1 | 0 |   1    |
| 0 | 1 | 1 |   0    |
| 1 | 0 | 0 |   1    |
| 1 | 0 | 1 |   0    |
| 1 | 1 | 0 |   0    |
| 1 | 1 | 1 |   1    |

It is possible to have an infinite number of input variables.

### Karnaugh Map

- Simplification of a truth table, half of the input variables are placed in the column, and the other half in the row.

Example with XOR.
| a/b | 0 | 1 |
| --- | - | - |
|  0  | 0 | 1 |
|  1  | 1 | 0 |

More complex example. (4 input variables)
| ab/cd | 00 | 01 | 11 | 10 |
| ----- | -- | -- | -- | -- |
|  00   |  0 |  1 |  0 |  1 |
|  01   |  1 |  0 |  1 |  0 |
|  11   |  0 |  1 |  1 |  1 |
|  10   |  1 |  0 |  1 |  1 |

> Concerning the row one / column one, the order 00, 01, 11, 10 is mandatory.

### From Karnaugh Map to Logical Formula

Original table.
| ab/cd | 00 | 01 | 11 | 10 |
| ----- | -- | -- | -- | -- |
|  00   |  0 |  0 |  1 |  0 |
|  01   |  1 |  1 |  1 |  1 |
|  11   |  1 |  1 |  0 |  0 |
|  10   |  0 |  0 |  0 |  0 |

We form rectangles that contain only '1' and are as large as possible (overlapping allowed!). The rectangles must consist of 2<sup>x</sup> number of cells.

![1699020485039](image/table-to-formula/1699020485039.png)

Now, we will take each rectangle individually and calculate its logical formula. We combine all individual results with AND operator '+' to form the final formula.

Red rectangle.
- $\overline{A}.B$

Pink rectangle.
- $\overline{A}.C.D$

Yellow rectangle.
- $B.\overline{C}$

Final result:
- $\overline{A}.B+\overline{A}.C.D+B.\overline{C}$