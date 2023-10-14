def bubble_sort(list, condition):
    tempon = 0
    for key in range(len(list)):
        for transmutation in range(len(list)-1, key, -1):
            tempon = list[transmutation]
            if (condition(tempon, list[transmutation - 1])):
                list[transmutation] = list[transmutation - 1]
                list[transmutation - 1] = tempon


def condition(element_1, element_2):
    return element_1 <= element_2


my_list = [1, 4, 3, 2, 6, 5]
bubble_sort(my_list, condition)
print(my_list)