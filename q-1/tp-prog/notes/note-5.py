def factoriel_recursif(n):
    if (n == 1): return n
    return n *  factoriel_recursif(n-1)


def factoriel_iteratif(n):
    factoriel = n
    for turn in range(n-1, 1, -1):
        factoriel *= turn
    return factoriel


def fibonacci_recursif(n):
    if (n <= 0 or type(n) != int): return
    if (n == 1 or n == 2): return 1
    return fibonacci_recursif(n-2) + fibonacci_recursif(n-1)


def fibonacci_iteratif(n):
    if (n <= 0 or type(n) != int): return
    if (n == 1 or n == 2): return 1
    a, b = 1, 1
    for turn in range(1, n-1):
        a, b = b, a+b
    return b
        

def main():
    print(factoriel_recursif(5)) # 120
    print(factoriel_iteratif(5)) # 120
    print(fibonacci_recursif(9)) # 34
    print(fibonacci_iteratif(9)) # 34

if __name__ == "__main__":
    main()