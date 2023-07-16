#A tuple consists of a number of values separated by commas
MyTupple = 100312 , 123123 , 512512 , 'A'
print(MyTupple[3]) #A

#nested Tuple
nested = MyTupple , (12312,12312312312,12312312312312321)
print(nested)#((100312, 123123, 512512, 'A'), (12312, 12312312312, 12312312312312321))
#Also Tupples are immutable and we cannot change them after intitalize specified value to them for example
#MyTupple[0] = 90909 will give us an exception
#if we define an string and put , beside the value our class will be tupple
var1 = 'Ali'
print(type(var1)) #<class 'str'> it's from class of string
varrr = 'Ali',
print(type(varrr)) #<class 'tuple'> it's from calss of tuple

#count() returns elements of our tupple
#also like dictionaries we can check wether there is or not an elemen in a tupple with *in* keyword
