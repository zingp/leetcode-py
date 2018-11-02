
# 归并
# arr = [1, 3, 5, 7, 2, 6, 9, 10]
# low = 0
# mid = (low+high) // 2
# high = len(arr) -1 
def merge(array, low, mid, high):
    i = low
    j = mid + 1
    tmpl = []
    while i <= mid and j <= high:
        if array[i] < array[j]:
            tmpl.append(array[i])
            i += 1
        else:
            tmpl.append(array[j])
            j += 1
        
    while i <= mid:
        tmpl.append(array[i])
        i += 1
    while j <= high:
        tmpl.append(array[j])
        j += 1
    array[low: high+1] = tmpl[:]
    return array

import random

arr = [1, 3, 5, 7, 2, 6, 9, 10]
print(merge(arr, 0, 3, len(arr)-1))