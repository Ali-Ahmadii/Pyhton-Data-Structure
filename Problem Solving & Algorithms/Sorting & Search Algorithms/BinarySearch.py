def BinarySearch(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if the target is not found

array = [1, 2, 3, 4, 5, 6, 7, 8]
target = 6
index = BinarySearch(array, target)
print(index)  #5
print(BinarySearch(array,100)) # -1 not found
