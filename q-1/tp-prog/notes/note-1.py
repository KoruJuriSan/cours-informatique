def main() :
    # theorie du cours 1
    def theorie() :
        print() # Correct ecrit une tab
        print("Hello World!") # Correct " ", ecrit Hello world
        print('Hello World!') # Correct ' ', exrit Hello world
        # print(hello) => NameError: hello is not defined.
        # print(Hello world!) => SyntaxError: invalid syntax.
        # print"Hello world!" => SytaxError: Missing parentheses in call to 'print'.
        print("Hello \nWorld!") # \n fait un retour a la ligne
        print("Hello,", "World" + "!") # Concatenation de chaines de caracteres => Hello, World!
        print("Hello", " World!", end=" fin.") # L'argument end permet d'ecrire un message a la fin du print. par defaut, c'est un retour a la ligne => Hello World! fin.
        print("Hello", "World!", sep="-") # L'arguement sep, permet de mettre une separation entre les concatenations => Hello-World
        print("My", "hello ", sep=" ", end="World! \n")
        print("je me repete, " * 3) # Permet de faire une multiplication de concatenation => je me repete, je me repete, je me repete
        
        print(1 + 2)  # addition
        print(1 - 2)  # soustraction
        print(1 * 2)  # multiplication
        print(1 / 2)  # division
        print(1 // 2) # division entiere
        print(1 % 2)  # modulo. Reste d'une division entiere
        print(1**2)   # exposant
        # la priorite des operation est d'application en python !

        une_variable: str = "une valeur"

    #exo1
    def exo1() :
        print("Les Profs","sont","génial", sep="***", end="... ")
        print("surtout Mr Mandoux")  

    #exo2
    def exo2() :
        print(
            "\"I'm\"",
            "\"\"Learning\"\"",
            "\"\"\"Python\"\"\"",
            sep=" \n"
        )
    
    #exo3
    def exo3() :
        jean: int = 3
        marie: int = 5
        adam: int = 6
        print(jean, marie, adam)
        total_apple: int = jean + marie + adam
        print(total_apple)
    
    def exo4() :
        kilometers = 12.25
        miles = 7.38
        miles_to_kilometers = 11.88
        kilometers_to_miles = 7.61
        print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
        print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

    

if __name__ == "__main__" :
    main()
