def MergeSort(array):
    if len(array) > 1:
        #divide and conquer
        Mid = len(array) // 2
        Left = array[:Mid]
        Right = array[Mid:]

        MergeSort(Left)
        MergeSort(Right)

        i = j = k = 0
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                array[k] = Left[i]
                i += 1
            else:
                array[k] = Right[j]
                j += 1
            k += 1
        while i < len(Left):
            array[k] = Left[i]
            i += 1
            k += 1
        while j < len(Right):
            array[k] = Right[j]
            j += 1
            k += 1
            
MyNum = [100,-12,3,64,132,521,10,32]
MergeSort(MyNum)
print(MyNum)
#MergeSort