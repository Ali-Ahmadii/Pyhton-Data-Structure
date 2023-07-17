def SelectionSort(array):
    n = len(array)

    for i in range(n-1):
        min_index = i

        # Find the index of the minimum element in the unsorted region
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j

        # Swap the minimum element with the first element of the unsorted region
        array[i], array[min_index] = array[min_index], array[i]

    return array

MyNum = [100,-12,3,64,132,521,10,32]
Ssorted  = SelectionSort(MyNum)
print(Ssorted)