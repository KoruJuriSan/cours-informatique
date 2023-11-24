def float_specialities():
    aFloat = 0.1
    anotherFloat = .1 # equivalent to 0.1
    aThridFloat = 1. # equivalent to 1.0

def tuples():
    aList = [1, "2", 3.0]
    aTuple = (1, "2", 3.0) # Tuples = LIST without imuability
    anotherTuple = 1, "2", 3.0 # Prenthesis not needed

    print(f"aList: {aList}, type: {type(aList)}")
    print(f"aTuple: {aTuple}, type: {type(aTuple)}")
    print(f"anotherTuple: {anotherTuple}, type: {type(anotherTuple)}")

    aList[1] = "4" # Work perfectly
    # aTuple[1] = "4" # Does not work ! Throw an error

def dictionnaries():
    aDictionnary = {"a": 1, "b": 2, "c": 3}
    
    print(f"aDictionnary: {aDictionnary}, type: {type(aDictionnary)}, keys: {aDictionnary.keys()}")
    print(f"sorted func: {sorted(aDictionnary)}")
    print(aDictionnary.values()) # Return every elements in an array without keys
    print(aDictionnary.keys()) # Return all keys of every elements
    print(aDictionnary.items()) # Return all items like this [[index, value], [index, value], ...]
    # Un dictionnaire n'est pas inice

    

def main():
    tuples()
    print("\n")
    dictionnaries()

if __name__ == "__main__":
    main()