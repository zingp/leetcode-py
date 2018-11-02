
def merge(array, low, mid, high):
    i = low
    j = mid
    tmpl = []
    while i <= mid and j <= high-1:
        if array[i] < array[j]:
            print(array[i], array[j])
            tmpl.append(array[i])
            i += 1
        else:
            tmpl.append(array[j])
            j += 1
        
    while i <= mid:
        tmpl.append(array[i])
        i += 1
    while j <= high - 1 :
        tmpl.append(array[j])
        j += 1
    array[low: high] = tmpl[:]
    print(tmpl)
    return array

import random

arr = [1, 3, 5, 7, 2, 6, 9, 10]
print(merge(arr, 0, 4, len(arr)))