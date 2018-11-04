
import random
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
   
# low,high分别代表第一个和最后一个元素的索引
def merge_sort(array, low, high):
    if low < high:    # 至少有两个元素
        mid = (low+high) // 2
        merge_sort(array, low, mid)
        merge_sort(array, mid+1, high)
        merge(array, low, mid, high)
    

# 测试归并
# arr = [1, 3, 5, 7, 2, 6, 9, 10]
# print(merge(arr, 0, 3, len(arr)-1))

array = list(range(10000))
random.shuffle(array)
merge_sort(array, 0, len(array)-1)
print(array)