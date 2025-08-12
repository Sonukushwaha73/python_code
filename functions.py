
# def greet():
#     print("hellow world")
# greet()#function call    
# #aor sahi number batata hai



# def sum():
#     print("the sum of your number is-----------------")
# sum()    


# def sum(a,b):
#     print(f"the sum of your number is :- {a+b}")
# sum(12,35) 
# sum(14,35)    



   



   #types of argument is three types argument
#types 1
# def add(a,b)
#     return a+b
# print(add(3,4))



#type 2
# def introduce(name,age):
#     print(f"I am {name} and I am {age} years old")
# introduce(age = 23 , name = "sonu")


#type 3
# def greet(name="sonu"):
#      print(f"hellow{name}")
# greet()    
# greet("golu")









# def hello():
#      return "hello how are you"
# print(hello())



#check not polindrome
def pallindrome(st):
     rev = ""
     for i in range(len(st)-1,-1,-1):
          rev = rev + st[i]
     if rev == st:
          print("it is a polindrome")     
     else:
      print("it is not a polindrome")      
pallindrome("naman")
pallindrome("cursor")



# def sum():
#     print("the sum of the number:- ")
# sum()    




def hello():
    return "hello how are you"# this is a function which return a value

print(hello())#yaha print karna padtta hai kyuki function return value deta hai