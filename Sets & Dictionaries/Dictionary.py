Dic = {'Al' : 3,'ca' : 2 , 'X' : 0}
print(Dic['Al']) #3
#functions of Dictionary
#we can change value of Dictionary element by refering to its key
Dic['X'] = 1400
print(Dic) #{'Al': 3, 'ca': 2, 'X': 1400}

#we can also add new item to Dictionary assigning value to a new key
Dic['New'] = 1401
print(Dic) #{'Al': 3, 'ca': 2, 'X': 1400, 'New': 1401}

#deleting an element from Dictionary

del Dic['New']
print(Dic) #{'Al': 3, 'ca': 2, 'X': 1400}

#we can also use pop() function for deleting an element refered to specified key
Dic.pop('X')
print(Dic)

#Membership Test with *in* keywork(it returns True or False)  ((Key exists or not?))
print('Al' in Dic)
print(3 in Dic)

#update()	Add or change Dictionary items.
newDic = {'B' : 9}
Dic.update(newDic)
print(Dic)


#clear()	Remove all the items from the Dictionary.
newDic.clear()
print(newDic) #{'Al': 3, 'ca': 2, 'B': 9}


#keys()	Returns all the Dictionary's keys.
print(Dic.keys()) #dict_keys(['Al', 'ca', 'B'])


#values()	Returns all the Dictionary's values.
print(Dic.values()) #dict_values([3, 2, 9])


#get()	Returns the value of the specified key.
print(Dic.get('Al')) #3


#popitem()	Returns the last inserted key and value as a tuple.
#copy()	Returns a copy of the Dictionary.