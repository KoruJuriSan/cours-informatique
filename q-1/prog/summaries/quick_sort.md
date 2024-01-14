# Quick sort

## Principle

- Choose a "pivot" in the list; it can be any element.

- eparate the initial list into two new lists. Every element that satisfies the condition with the "pivot" goes into the first list, and the others go into the second one. The pivot is not in either of these lists.

- Apply steps 1 and 2 for every sublist obtained until you have lists with only one element or less in any array.

- At each step, concatenate the first sub-array with the pivot followed by the second sub-array. Continue doing this until you have only one array.

> The algorithm above is recursive.

## Example

- [4, 2, 1, 3]

```
pivot = 3 (last one, but could be 4, 2 or 1 in this case)
[4, 2, 1, -]
```

```
sub_array 1 et 2 = []
```

```
Compare every element in the array [4, 2, 1, -] with the pivot. If the condition is valid, add this value to the first sub-array, then to the second.
[4, 2, 1] (3) []
```

```
Repeat this for every sub-array until you get only arrays of one element or less...
  [2, 1]     (3) [4]
    |             
[] (1) [2]
```

```
Now from every sub-array FROM THE BOTTOM, concatenate them in this order: sub_array_1 + pivot + sub_array_2
  [1, 2] + (3) + [4] = [1, 2, 3, 4]
    |             
  [] + (1) + [2] = [1, 2]
```

## Code in python

```py
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
```
