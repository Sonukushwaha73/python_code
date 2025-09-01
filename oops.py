# a=12
# b=45
# print(a+b)


# #function apporach
# def  addition(x,y):
#     print(x-y)
# addition(10,8)    
# addition(110,18)


#object oriented programing
class calculator:
    a=12#atribute
    def  addition(self):#methodself kya hai?

# self object ko represent karta hai jo class se banaya gaya hai.

# Jab bhi tum class ke method ke andar attribute ya method ko access karte ho, to self ki zarurat hoti hai.

# Matlab self ek placeholder hai current object ke liye.
        print("hellow  how are you")
    print("hello who are you i am fine")    

print(calculator().a)
calculator().addition()



#object in oops
class calculator:
    a=12#atribute
    def  addition(self):
        print("hellow  how are you")
obj= calculator()
print(obj.a)




#constuctor in oops
class calculator:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
    def show(self):
         print(f"you object is made of {self.material}, {self.zips},{self.pockets}")
reebol = calculator("lather", 2 ,4)
print(reebol.pockets)

reebol.show()  



#trype of atribute
#i class of atribute----->normal variable of class atribute
class Animals:
    
    name = "lion"#clas atribute
    def __init__(self ,age):
        
        self.age =age#instance atribute

        def show(self):# instance method
             print("how are you")
clasasmethod
        @classmethod
        def hello(cls):#$cls is class target(Animal)
            print("hello who are you brother")

#staticmethod
        @staticmethod#class par kaam karne wala method

#@staticmethod → normal function jaise, sirf class ke andar
        def static():
            print("how are you")

obj= Animals(5)
print("hello")