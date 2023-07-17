def LinearSearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i

    return -1  # Return -1 if the target is not found

array = [4, 2, 6, 8, 1, 3, 5, 7]
target = 6
index = LinearSearch(array, target)
print(index)
