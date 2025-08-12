
# set{}
# mutable------------>you can change the vlues of set

# duplicates--------->extra value is one is repeated 22222--->2
# unordered---------->set is no index value
# hetergenous____________-----> it can store the tuple ,number


# mutable------------>you can change the vlues of set

a = { 1,2,3,4,5}

print(a)


# #duplicates--------->extra value is one is repeated 22222--->2 
a = { 1,1,2,3,3,2,3,4,5}

print(a)


# unordered---------->set is no index value
a = { 1,1,2,3,3,2,3,4,5}

print(a[0]) #is erorr program



#hash vlaue 
b = hash("hello")
print(b)
   

c = hash(1,2,3444,56)   
print(c)


#set method

#[i] s.add
#[ii]s.remove
#[iii]s.discard----->remove 
#[iv]s.clear


s ={1,2,3,4}
s.add(6)
print(s)



#s.remove
s ={1,2,3,4}
s.remove(3)
print(s)



#s.clear
s ={1,2,3,4}
s.clear()
print(s)


#[i]a.union
#[ii]A.intersection
#[iii]A.difference
#[iv]A.symmetric_difference

#[i]a.union------>sub one chance repeated
A = {1,2,3}
B = {3,4,5}
s = A.union(B)
print(s)


#[ii]A.intersection----->jo two likha hoga vah one bar likha jayega


A = {1,2,3}
B = {3,4,5}
s = A.intersection(B)
print(s)


#[iii]A.difference(B)------------>A में जो elements हैं, लेकिन B में नहीं हैं — उन्हें निकाल दो।

A = {1,2,3}
B = {3,4,5}
s = A.difference(B)
print(s)



#[iv]A.symmetric_difference------->repeat value not written
A = {1,2,3}
B = {3,4,5}
s = A.symmetric_difference(B)
print(s)

