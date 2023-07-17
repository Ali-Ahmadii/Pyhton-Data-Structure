def Bubble(array) :
    for i in range(len(array)):
        for j in range(0,len(array) - i -1):
            if(array[j] > array[j+1]):
                x = array[j]
                array[j] = array[j+1]
                array[j+1] = x
                
MyNum = [100,-12,3,64,132,521,10,32]
Bubble(MyNum)
print(MyNum) #[-12, 3, 10, 32, 64, 100, 132, 521]
        
    