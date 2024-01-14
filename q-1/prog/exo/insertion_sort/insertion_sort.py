def insert_sort(list, condition):
    for i in range(1, len(list)):
        cache = list[i]
        j = i - 1
        while j >= 0 and condition(cache, list[j]):
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = cache


def condition(element_1, element_2):
    return element_1 <= element_2


my_list = [9, 4, 3, 2, 6, 5]
insert_sort(my_list, condition)
print(my_list)