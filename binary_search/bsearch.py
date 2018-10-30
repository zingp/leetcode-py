

def binary_search1(array, n):
    high = len(array) - 1
    low = 0
    while low <= high:
        mid = (low+high) // 2
        if array[mid] == n:
            return n
        elif array[mid] > n:
            high = mid - 1
        else:
            low = mid + 1
    return


if __name__ == '__main__':
    array = list(range(1000))
    r = binary_search1(array, 999)
    print(r)
