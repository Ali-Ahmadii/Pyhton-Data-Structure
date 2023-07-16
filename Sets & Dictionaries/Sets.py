# A set is an unordered collection with no duplicate elements.
#now let's define a set with duplicate values
MySet = {"A","B","C","D","A"}
print(MySet)  # result will be {'B', 'C', 'D', 'A'}
#as you can see there is no duplicated vaules in result

#Adding an element to a set
MySet.add(1) #It will be added to first of set
print(MySet) #{1, 'B', 'A', 'D', 'C'}

SecondSet = {"AA","BB","CC","D"}

Unite = MySet.union(SecondSet) #uniton function combines sets in a new set
print(Unite) #{1, 'CC', 'D', 'BB', 'A', 'B', 'AA', 'C'}

intersection = MySet.intersection(SecondSet) #Intersection function finds elements that are present in both sets
print(intersection) #{'D'}

diffrent = MySet.difference(SecondSet) #The difference() function deletes the data present in both and outputs data present only in the set passed

print(diffrent) #{'C', 'A', 'B', 1}

symmetric_d = MySet.symmetric_difference(SecondSet) #The symmetric_difference() does the same as the difference() function but outputs the data which is remaining in both sets

print(symmetric_d) #{1, 'A', 'AA', 'BB', 'C', 'B', 'CC'}