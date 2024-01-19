# Matrix Calculations.

## Rules

### Row Matrices

- $A_{1\times n} =
    \left[ {\begin{array}{c}
        a_{11} & a_{12} & ... & a_{1 \times n} \\
    \end{array} } \right]
    $

> Only one row.

### Column Matrices

- $A_{m\times 1} =
    \left[ {\begin{array}{c}
        a_{11} \\ a_{21} \\ ... \\ a_{m \times 1} \\
    \end{array} } \right]
    $

> Only one column.

### Zero Matrix

- A matrix where every element == 0. ( $ 0_{m \times n}$ )

### Square/Diagonal Matrices

- A matrix where n == m.
- The diagonal of a square matrix is the set of points where "n == m."
- $ A_{m\times n} =
    \left[ {\begin{array}{c}
        (a_{11}) & a_{21} & ... \\
        a_{21} & (a_{22}) & ... \\
        ... & ... & (...) \\
    \end{array} } \right]
    $

### Triangular and Diagonal Matrices

A matrix is ... if ...
- **Upper** triangular if every element below the diagonal is == 0.
- $ A_{m\times n} =
    \left[ {\begin{array}{c}
        (a_{11}) & x & x \\
        0 & (a_{22}) & x \\
        0 & 0 & (...) \\
    \end{array} } \right]
    $

- **Lower** triangular if every element above the diagonal is == 0.

- $ A_{m\times n} =
    \left[ {\begin{array}{c}
        (a_{11}) 0 x & 0 \\
        x & (a_{22}) & 0 \\
        x & x & (...) \\
    \end{array} } \right]
    $

- Diagonal if it is both upper and lower triangular at the same time.

- $ A_{m\times n} =
    \left[ {\begin{array}{c}
        (a_{11}) & 0 & 0 \\
        0 & (a_{22}) & 0 \\
        0 & 0 & (...) \\
    \end{array} } \right]
    $

### Identity Matrices

- A diagonal matrix where nm == 1 + size n.

- $ I_{n} =
    \left[ {\begin{array}{c}
        1 & 0 & 0 \\
        0 & 1 & 0 \\
        0 & 0 & (...) \\
    \end{array} } \right]
    $

> $A \times A^{-1} = I_1$

### Idempotence

- if $A = A^2$ then, A is Idempotent.

## Operations

### Addition / Subtraction / Scalar Multiplication

- Preconditions,
    - $n_A == n_B$
    - $m_A == m_B$
> Must be of the same dimension.

- Add or subtract each element at the same index from both matrices.

$ A+B =
    A\left[ {\begin{array}{c}
        1 & 2 & 3 \\
        4 & 5 & 6 \\
        7 & 8 & 9 \\
    \end{array} } \right]
    +
    B\left[ {\begin{array}{c}
        9 & 8 & 7 \\
        4 & 5 & 6 \\
        3 & 2 & 1 \\
    \end{array} } \right]
    =
    \left[ {\begin{array}{c}
        1+9 & 2+8 & 3+7 \\
        4+4 & 5+5 & 6+6 \\
        7+3 & 8+2 & 9+1 \\
    \end{array} } \right]
    $

### Scalar Multiplication

- Multiply each element of the matrix by the scalar.

- $ x \times A\left[ {\begin{array}{c}
        1 & 2 & 3 \\
        4 & 5 & 6 \\
        7 & 8 & 9 \\
    \end{array} } \right] =
    \left[ {\begin{array}{c}
        1x & 2x & 3x \\
        4x & 5x & 6x \\
        7x & 8x & 9x \\
    \end{array} } \right]
    $

### Transposition

- Column and row inversion ( $A^T$ ):
    - Row1 = Column2
    - Column1 = Row2

- $ A\left[ {\begin{array}{c}
        1 & 2 & 3 \\
        4 & 5 & 6 \\
        7 & 8 & 9 \\
    \end{array} } \right]
    $

- $ A^T\left[ {\begin{array}{c}
        1 & 4 & 7 \\
        2 & 5 & 8 \\
        3 & 6 & 9 \\
    \end{array} } \right]
    $

### Determinant |!|

- To calculate the determinant of a 2x2 matrix A, use:
    - $(a \times d) - (b \times c)$

    - $ det(A)\left[ {\begin{array}{c}
            a & b \\
            c & d \\
        \end{array} } \right]
    $

    To calculate the determinant of an n x n matrix B, use:
    - $a_{11} \times det(A_{11}) - a_{12} \times det(A_{12}) + a_{13} \times det(A_{13})$ ... $\pm a_{1n} \times det(A_{1n})$
    - $B\left[ {\begin{array}{c}
        {+} & - & ..\pm \\
        a_{11} & a_{12} & ..a_{n3} \\
        a_{21} & a_{22} & ..a_{n3} \\
        ..a_{3n} & ..a_{3n} & ..a_{nn} \\
    \end{array} } \right]
    $

> the minor, is the determinant of a specific point of the original matrix.

> This method works by recursion for those who like programming.

### Inversion |!|

- $A^{-1}$ is the inverse of A. To determine the inverse of a matrix, first, check if it is possible.

- To check if a matrix is invertible, its determinant must be != 0.

- If it is invertible, to obtain its inverse, use the rule $A \times A^{-1} = I_1$

### Matrix Multiplication |!|

- Preconditions:
    - If $n_A$ == $m_B$, then $A \times B$ is possible.

- $C = A \times B$
- $c_{mn} = \sum_{k=1}^{n} a_{mk} \times b_{kn}$ ( $c_{11} = (a_{11} \times b_{11}) + (a_{12} \times b_{21}) + ... + (a_{1k} \times b_{k1})$ )
