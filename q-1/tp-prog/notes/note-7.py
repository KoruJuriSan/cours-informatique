def try_except():
    try:
        code = 1 / 0 # Produit une erreur
    except ZeroDivisionError: # Execute si le code du try produit une erreur de type 'ZeroDivisionError'
        print("Attention on ne peut pas diviser par 0 !")
    except: # Execute si le code du try produit une erreur en general
        print("Attention le code du dessus produit une erreur !")
    else:
        # Execute si le code du try est execute sans erreur
        pass
    finally:
        # est toujours execute
        pass

def main():
    try_except()

if __name__ == "__main__":
    main()