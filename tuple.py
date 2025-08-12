#tupl 

#  1immutable-------->you cannot change vlaue of tuple
# 2 duplicates------->duplicates value is tuple 
 #3ordered --------------->you can access them through index value
#heterogenous------------>diffent type of data structure



#tuple method______________>index,count
a=(1,3,3,3,4,5)
print(type(a))

#  #3ordered --------------->you can access them through index value

a=(1,3,3,3,4,5)
print(a[0])

# #heterogenous------------>diffent type of data structure
a=(1,3,3,3,4,5,5.6, print(),tuple)
print(a)



a=(1,3,3,3,4,5)
for i in a:
      print(a[i])


# #tuple method______________>index,count
t = (3,4,8,4,0,1,6)
index = t.index(5)
print(index)



t = (3,4,8,4,0,1,6) 
count = t.count(3) 
print(count)


a,b,c,d = (1,2,3,4)
print(a)
print(b)
print(c)
print(d)
