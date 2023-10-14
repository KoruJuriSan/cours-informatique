def insertion_sort(list, condtion):
    tempon = 0
    transmutation = 0
    for key in range(1, len(list)):
        tempon = list[key]
        transmutation = key - 1
        while transmutation > 0 and condtion(tempon, list[transmutation]):
            list[transmutation + 1] = list[transmutation]
            transmutation -= 1
        list[transmutation + 1] = tempon


def condition(element_1, element_2):
    return element_1 <= element_2


my_list = [1, 4, 3, 2, 6, 5]
insertion_sort(my_list, condition)
print(my_list)