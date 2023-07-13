Something = ["A","B","C","D","E"]
print(Something)
x = Something[2] #gets C for x
print(x)
Something.append("Ali")
print(Something)
anotherlist = ["S","T","U","D"]
Something.extend(anotherlist) #another list extended to end of something list
print(anotherlist)
Something.insert(1,"S") #insert to specific index
print(Something)
Something.remove("D") #it removes D element in list (first one)
print(Something)
#and we have other methods like pop(i) that removes the elemnt in determined position and also returns us that elemnet
#clear() that removes all of elements
#count(e) returnt how many e element we have in list
#sort() for sorting list
#reverse() reverses list
#copy() this method is used for having another list with same elements of base list and also it's the same as list=base that list is copies of elements of base
