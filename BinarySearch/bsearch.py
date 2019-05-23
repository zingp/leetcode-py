

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

def binary_search2(array, val):
    #print(array)
    mid = (len(array) -1) // 2
    if array[mid] == val:
        return val
    elif array[mid] > val and mid - 1 > 0:
        #print(">val:", array[mid])
        return binary_search2(array[:mid], val)
    elif array[mid] < val and mid + 1 <len(array):
        #print("<val:", array[mid])
        return binary_search2(array[mid+1:], val)
    else:
        return 
    

if __name__ == '__main__':
    array = list(range(1000))
    r = binary_search2(array, 999)
    print(r)
