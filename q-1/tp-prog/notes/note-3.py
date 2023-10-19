def list():
    index = 3
    my_list = ["Michel", 12, 1.0, False] # Liste d'elements
    print(my_list[index]) # Print l'element a l'index 'index' a partir de 0 => False

    index = -1 # Un index negatif permet de rechercher un element a partir de la fin
    print(my_list[index]) # => False

    print(len(my_list)) # Print le nombre d'element dans la liste 'my_list' => 4

    my_list.append("Hello") # Ajoute l'element '"Heloo"' a la fin de la liste 'my_list'
    print(my_list) # => ["Michel", 12, 1.0, False, "Hello"]

    index = 5
    my_list.insert(index, "World!") # Ajoute l'element '"Wolrd!"' a l'index 'index' de la liste 'my_list'
    print(my_list) # => ["Michel", 12, 1.0, False, "Hello", "Wolrd!"]

    index = 5
    my_list.pop(index) # Supprime l'element a l'index 'index' de la la liste 'my_list'
    print(my_list) # => ["Michel", 12, 1.0, False, "Hello"]

    index = 0
    del my_list[index] # equivalent 'my_list.pop(index)' mais en plus moderne
    print(my_list) # => [12, 1.0, False, "Hello"]

    my_list.remove("Hello") # Supprime la premiere iteration d'un element '"Hello"' dans la liste 'my_list'
    print(my_list) # => [12, 1.0, False]

def variables():
    var1, var2 = 12, 32
    # equivalent:
    var1 = 12
    var2 = 32

def foreach():
    my_list = ["Jean", "Paul", "Jack"]
    for e in my_list: # itere autant de fois qu'il y a d'element dans la liste et le stocke dans 'e' a chaque iteration
        print(e) # print l'element e de la liste
    
def list_comprehension():
    number
    my_list = [x*2 for x in range(number)] # Cree une liste avec 'number' dynamiquement avec x++ pour chaque element 'x*2'

def bubble_sort():

    def condition(element_1, element_2):
        return element_1 <= element_2

    list = [1, 4, 3, 2, 6, 5]
    tempon = 0
    for key in range(len(list)):
        for transmutation in range(len(list)-1, key, -1):
            tempon = list[transmutation]
            if (condition(tempon, list[transmutation - 1])):
                list[transmutation] = list[transmutation - 1]
                list[transmutation - 1] = tempon

    print(my_list) 

def exo1():
    list = [1, 2, 3, 4, 5]
    replacement = int(input("Entrer le nouveau numero de la maison du milieu: "))
    list[len(list)//2] = replacement
    list.pop(len(list)-1)
    print(len(list))
    print(list)

def exo2():
    group = []
    group.append("Johan le Preteur")
    group.append("Denis seins doux")
    group.append("Yoan l'impononcable")
    for new_member in ["Joakim Synagogue", "David Art nouveau"]:
        input("Ajouter " + new_member)
        group.append(new_member)
    group.remove("David Art nouveau")
    group.remove("Denis seins doux")
    group.insert(0, "Erwin le schmet")
    print(group)
    

def main():
    list()


if __name__ == "__main__":
    main()