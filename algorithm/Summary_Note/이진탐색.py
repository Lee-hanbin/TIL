def binarySearch(n, lst, key):
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high)//2
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1