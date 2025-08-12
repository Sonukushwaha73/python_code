
#multiple function save in one file is called data structure
#in-built function
#--->i list,tuple dictionary ,set




#custom data structrue
#------>[i]stack, queue, linked list,tree,graph  


#list power  
# ->[i] mutable  ------> change value
# ->[ii] duplicates-------> multiple duplicates
# ->[iii] ordered---------->data maintans
# ->[iv]  hetergenous-------> or vlaue save



a=12,2,34
print(a)


#index in slicing 
a="hello"
print(a[0])



#slicing 
a="hello"
print(a[::])


#list 
a=[23,34,4,56,45,47,87]
print(a[4])



# def pollindrome(st):
#     rev=""
#     for i in range(len(st)-1,-1,-1):
#         rev=rev+st[i]
#     if rev == st:
#         print("polindrome")
#     else:
#         print("not pollindrome")    
# pollindrome("sonu kushwaha")
# pollindrome("golu kushwaah")        
a=[23,34,4,56,45,47,87] 
for i in range(len(a)):
     print(a[i])  
 
#2nd way directly on value
for i in a:
    print(a[i])