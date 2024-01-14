def quick_sort(arr, condition):
    if (len(arr) <= 1):
        return arr
    else:
        pivot = arr.pop(0)
    sub_arr1, sub_arr2 = [], []
    for e in arr:
        if (condition(pivot, e)):
            sub_arr1.append(e)
        else:
            sub_arr2.append(e)
    return quick_sort(sub_arr1, condition) + [pivot] + quick_sort(sub_arr2, condition)


def condition(element_1, element_2):
    return element_1 <= element_2


my_list = [9, 4, 3, 2, 6, 5]
print(quick_sort(my_list, condition))