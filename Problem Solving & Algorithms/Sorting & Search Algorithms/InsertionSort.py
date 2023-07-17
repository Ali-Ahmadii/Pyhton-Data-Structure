def InserionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1      
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

MyNum = [100,-12,3,64,132,521,10,32]
InserionSort(MyNum)
print(MyNum)