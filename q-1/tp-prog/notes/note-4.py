
def function_base():
    # Fait qq chose.
    # ex: print
    print("Une fonction permet de faire de bout de code reutilisable n'importe quand dans le code (remplace ctrl+ c, ctrl + v)\n")


def function_parameters(param_1, param_2): # les parametres sont des variables de la fonction (variable locale a la fonction)
    return param_1 + param_2

def function_default_value(nom="Paul", prenom="Michel"): # nom et prenom on une valeur par defaut 'Paul' et 'Michel'.
    return "mon nom est " + nom + " " + prenom


def function_recursive(value): # !value en math
    print("Un call recursif")
    if (value <= 1):
        return 1
    result = value * function_recursive(value-1)
    return result

def is_year_leap_exo1(year):
    return year%4 == 0 and year%100 != 0 or year%400 == 0


def exo1():
    test_data = [1900, 2000, 2016, 1987]
    test_results = [False, True, True, False]
    for i in range(len(test_data)):
        yr = test_data[i]
        print(yr,"->",end="")
        result = is_year_leap_exo1(yr)
        if result == test_results[i]:
            print("OK")
        else:
            print("KO")


def days_in_month_exo2(year, month):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (month == 2 and is_year_leap_exo1(year)):
        return 29
    return months[month-1]


def exo2():
    test_years = [1900, 2000, 2016, 1987]
    test_months = [2, 2, 1, 11]
    test_results = [28, 29, 31, 30]
    for i in range(len(test_years)):
        yr = test_years[i]
        mo = test_months[i]
        print(yr, mo, "->", end="")
        result = days_in_month_exo2(yr, mo)
        if result == test_results[i]:
            print("OK")
        else:
            print("KO")

def day_of_year_exo3(year, month, day):
    days_per_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    for i in range(month-1):
        if (i == 1 and is_year_leap_exo1(year)):
            days += 29
        else:
            days += days_per_months[i]
    days += day
    return days


def exo3():
    print(day_of_year_exo3(2000, 12, 31))

def main():
    # call la fonction 'function_base'
    function_base()

    # call une deuxieme fois la fonction 'function_base' dans la fonction 'print'
    function_base()

    # call la fonction 'function_parameters'
    function_parameters(param_1=10, param_2=2) # donne les arguments pour param_1 et param_2, ici 10 et 2

    # call la fonction 'function_default_value' dans la fonction 'print'
    print(function_default_value(nom="Jaqueline")) # done la velur 'jaqueline' a l'arguement 'nom' et laisse la valeur par defaut a prenom

    # call la fonction 'function_recursive' dans la fonction 'print'
    print(function_recursive(4))

    exo3()

if __name__ == "__main__":
    main()