#append method----.>add the value

a=[1,2,3,4,5]
a.append(6)
a.append(6)
print(a)


#insert the value------->number missing
a=[1,3,4,5]# is 2 number is missing
a.insert(1,2)# jiske baad chahiye number uske baad add ho gaya number
a.insert(5,7)
print(a)


#remove method
a=[1,2,3,4,5]
a.remove(4) #is number 4 remove
print(a)

#pop method
a=[1,2,3,4,5]
a.pop(0)#index is pop hoga method
print(a)


#count method
a=[1,2,3,4,5]
a.count(4)
print(a)



#sort method-------->list the acending order

a=[1,6,8,5,9]
a.sort()
print(a)



#revers method
a=[1,6,8,5,9]
a.reverse()
print(a)


#number copy method--------->creat the list copy
a=[1,6,8,5,9]
a.copy()
print(a)



#clear method
a=[1,6,8,5,9]
a.clear()
print(a)