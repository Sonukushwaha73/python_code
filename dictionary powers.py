
# dictionary powers---->hashmap  esme colon:used hota ahi
#  mutable---------> you can add or remove key-value pairs afert creation
# duolicates------->you can have duplicates in value
# herterogeneous---->key and value ,likeinters,string,list,or  even another dictionary


a={}
print(a)


a ={10:100,20:200,30:300 }
print(a)

a = {"name":"sonu","age":22}
print(a)


#index jisme convert value 
a ={10:100,20:200,30:300 }
print(a[20])
  


  #index value change
a ={10:100,20:200,30:300 }
a[30] = 30000000
print(a)



#new value update

a ={10:100,20:200,30:300 }  
a.update({8000:50000000})
print(a)



#delete value
a ={10:100,20:200,30:300 }
del a[30] 
print(a)





#dictionary ke upr loop kaise chalate hai
a ={10:100,20:200,30:300 }
for i in a:
    print(i)

    #output
   # key  print hoga
# 10
# 20
# 30

a ={10:100,20:200,30:300 }
for i in a:
    print(a[i])
#output
   # value print hoga
#    100
# 200
# 300