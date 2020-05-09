#assigning elements to different lists
list1=["apple","banana","cherry"]
list2=["cricket","football","tennis"]
#to assign at last
list1.append("orange")
list2.append("rugby")
#to assign in specified position
list1.insert(1,"berry")
list2.insert(2,"kabbadi")
print(list1)
print(list2)

#accessing elements from a tuple
tup1=("tamil","english","hindi")
print (tup1[0])
print (tup1[1])
print (tup1[2])

#deleting different dictionary elements
dict1={1:'chocolate',2:'ice cream',3:'burger'}
del dict1[1]
del dict1[3]
print(dict1)
