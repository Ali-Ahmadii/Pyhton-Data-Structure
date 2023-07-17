def QuickSort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return QuickSort(left) + middle + QuickSort(right)

MyNum = [100,-12,3,64,132,521,10,32]
Qsorted  = QuickSort(MyNum)
print(Qsorted)