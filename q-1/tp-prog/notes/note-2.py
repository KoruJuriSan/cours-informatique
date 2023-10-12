from time import sleep # Permet d'importer la fonction 'sleep' du module 'time' pour l'exo 6

def main():

    def conditionnal_operators():
        x = 1
        y = 10
        # Operateurs de comparaison.
        print(x == y) # verifie une egalite / 1 == 10 / faux
        print(x != y) # verifie une inegalite / 1 != y / vrai
        print(x > y) # verifie une superiorite / 1 > 10 / faux
        print(x < y) # verifie une inferiorite / 1 < 10 / vrai
        print(x >= y) # verifie une superiorite ou egalite / 1 >= 10 / faux
        print(x <= y) # verifie une inferiorite ou egalite / 1 <= 10 / vrai
        # print(x = y) # TypeError: "x" is an invalid keyword argument for print()

        def struct_conditionnels():
            condition = True
            condition_2 = False

            if (condition): # execute son code si la condition est vraie
                print("Execute cette ligne si condition est vraie")
                
            elif (condition_2): # execute son code si le if et les elif precedant sont faux et que ca condition est vraie
                print("Execute cette ligne si condition et fausse et que condition_2 et vraie")

            else: # execute son code si le if et les elif sont faux
                print("Execute cette ligne si condition et condition_2 sont fausses")
            
            # Il n'est pas obliger d'avoir des elif ou else dans un programme,
            # on peut avoir plusieurs elif.
            # un if et un else au MAX !
    
    def whileloop():
        while (condition): # repete son code tant que condition est vraie, ne ce lance que si elle est vraie par defaut
            print("code repete")

    def forloop():
        x = 10
        for iteration in range(x):
            print("Iteration: ", str(iteration)) # Code repete 'x' fois avec iteration vaut les nombres de 0 a 'x' -1 => 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        print("Fin.")
        y = 20
        for iteration in range(x, y):
            print("Iteration: ", str(iteration)) # Code repete 'y' - 'x' fois avec iteration vaut les nombres de 'x' a 'y' -1 => 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
        print("Fin.")
        z = 2
        for iteration in range(x, y, z):
            print("Iteration: ", str(iteration)) # Code repete 'y' - 'x' fois avec iteration vaut les nombres de 'x' a 'y' -1 avec un pas de 'z' => 10, 12, 14, 16, 18
        print("Fin.")


    def break_a_loop():
        while True:
            print("Code qui sera execute")
            break # casse la boucle et passe la ligne qui suit la fin de celle-ci
            print("Code qui ne sera pas execute")
        
        # Fonctionne aussi dans les boucles for
    
    def continue_a_loop():
        for i in range(10):
            print("Code qui sera execute x10")
            continue # passe les instructions suivante sans casse la boucle
            print("Code qui ne sera pas execute")

    def exo1():
        n = int(input("entrez un nombre: "))
        print(n >= 100)
    

    def exo2():
        name = input("Write the name of the worst teacher: ")
        if (name == "Depreter") : print("Good answer ! The WORST teacher is Mr Depreter.")
        elif (name == "depreter") : print("NO! I Want the real Mr Depreter.")
        else: print("Wrong ! The right answer was 'Depreter', not '" + name + "'")


    def exo3(salary_funcoin):
        impot = 0
        if (type(salary_funcoin) == 'int' or type(salary_funcoin) == 'float'): 
            print("funcoin n'est pas au bon format: ", type(salary_funcoin))
            return 0
        

        if (salary_funcoin <= 85_528):
            impot += ((salary_funcoin / 100) * 18) - 556.02
        else:
            impot += ((salary_funcoin - 85_528) / 100) * 32
            impot += 14_839.002
        if (impot < 0): impot = 0
        return round(impot)


    def exo4(year):
        if (year < 1582): return None
        if (year % 4 != 0): return False
        elif (year % 100 == 0): return True
        elif (year % 400 == 0): return False
        else: return True


    def exo5():
        number = 24
        choice = None
        while choice != number:
            try:
                choice = int(input("Si tu veux sortir de ma boucle tu dois trouver le nombre sercet !! Mouah hah haha !! \n Enter a number: "))
            except:
                print("Tu ne sais meme pas entrer un nombre tu risque de rester ici pour toujours !! Mouah hahahah !")
            else:
                if (choice != number): print("FAUX !! Le nombre a trouver n'est pas ", str(choice))
        print("COMMENT !!! Tu as trouver mon nombre sercret qui etait", number)


    def exo6():
        for count in range(1, 6):
            print(str(count), "Mississippi")
            sleep(1)
        print("Pret ou pas, j'arrive !")


    def exo7():
        while True:
            entry = input("Entrez le mot de passe: ")
            if entry == "elpsykangoro":
                print("L'organisation est a cinq minutes de votes position, termine.")

    def exo8(word):
        for letter in word:
            if (letter.upper() not in ["A", "E", "I", "O", "U"]): print(letter)


    def exo9(nb_blocks):
        stage = 0
        blocks_per_stage = 0
        while blocks_per_stage < nb_blocks:
            stage += 1
            blocks_per_stage += stage
        if (blocks_per_stage == nb_blocks): return stage
        else: return stage - 1

    def exo10(start):
        current = start
        steps = []
        while current != 1:
            if (current%2 == 0):
                current/= 2
            else:
                current = current*3 +1
            steps.append(current)
        return [steps, len(steps)]


    def exo11_1():
        for iteration in range(0, 11):
            if (iteration % 2 != 0): print(iteration)


    def exo11_2():
        iteration = 1
        while iteration < 10:
            print(iteration)
            iteration += 2
    

    def exo11_3():
        name = ""
        for ch in "joulian.colle@std.heh.be":
            if (ch == "@"): break
            name += ch
        return name
    

    def exo11_4(chain):
        new_chain = ""
        for digit in chain:
            if digit == "0": new_chain += "x"
            else: new_chain += digit
        return new_chain
    

    def exo11_5():
        n = 3
        while n > 0:
            print(n + 1)
            n -= 1
        else:
            print(n)
    

    def exo11_6():
        n = range(4)
        for num in n:
            print(num - 1)
        else:
            print(num)


    def exo11_7():
        for i in range(0, 6, 3):
            print(i)

if __name__ == "__main__":
    main()