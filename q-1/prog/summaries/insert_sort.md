# Insert sort

## Principe

1.Iterate through each element starting from the second one in the list.

2. Remove this element from the list and keep it in a cache.

3. Check if this element meets the sorting condition when placed one element back OR if there are no more elements to the left.

    3.1 If yes, move the checked element one to the right, go back to instruction 3, but check one more element to the left.

    3.2 If no, end the loop and proceed to instruction 4.

4. Place our cache in the new location created in instruction 3.1.

## Exemple Theorique

- [3, 2, 1]
```
cache = 2
[3, -, 1]
```

```
if cache < 3 or there are no more elements?
Yes.
cache = 2
[-, 3, 1]
```

```
if cache < 3 or there are no more elements?
No more elements. End of loop.
cache = 2
[-, 3, 1]
```

```
Place the cache in the empty location
[2, 3, 1]
```

... Repeat for the next elements.

## Code in python

```py
def insertion_sort(list, condition):
    for i in range(1, len(list)):
        cache = list[i]
        j = i - 1
        while j >= 0 and condition(cache, list[j]):
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = cache
```