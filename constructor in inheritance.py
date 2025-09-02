# 1. Constructor kya hota hai?

# Constructor ek special method hai jo __init__ naam se hota hai.

# Ye object banate hi automatic call hota hai.

# Iska kaam hota hai object ke attributes initialize karna.



#-----------------------------------
# Constructor = __init__, automatic call hota hai.

# Agar child me constructor nahi hai → parent ka call hota hai.

# Agar child me constructor hai → sirf child ka call hota hai.

# Agar dono chahiye → super() use karo.




class Animals:
    def __init__(self,name):
        self.name = name # object ka attribute set kiya
    def show(self):#instance method
        print(f"animals name is {self.name}")#ka matlab hai “animals name is <object ka name>”.
class human(Animals):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
    def show(self):#instance method
        print(f"animals name is {self.name}.{self.age}")#ka matlab hai “animals name is <object ka name>”.


         
# class human(Animals):
#     pass
person1 = human("sonu",24)        
person1.show() 
animals = Animals("tiger")  
   



class Animals:
    name1 = "lion"
class Human:
    name2 = "sonu"
class Dog(Human,Animals):
    name3 = "charli123"
obj = Dog()
print(obj.name1)    





#multiple inheritance with constructor
class Animals:
    def __init__(self,name):
class Human:
   def __init__(self,age,name):
class robots(Human,Animals):
    name3 = "charli123"
    pass
obj = robots()



#multilevel inheritance
# Multilevel inheritance me ek class ko doosri class se inherit karaya jata hai, aur fir ek aur class us inherited class se inherit karti hai. Matlab ek “chain” ban jati hai.

# Isko [“grandparent → parent → child” ]relation bhi bol sakte ho.
class Animals:
    def __init__(self,name):
         pass
class Human:
    def __init__(self,age,name):
class today(Human,Animals):
    name3 = "charli123"
obj = today()




class Factory:
    def __init__(self,material,zips):
     self.material = material
     self.zips = zips
class bhopalFactory(Factory):
    def __init__(self,material,zips,color):
       super().__init__(material,zips)
       self.color = color
class delhiFactory(bhopalFactory):
    def __init__(self,material,zips,color,pockets)    
     super().__init__(material,zips,color)             
     self.pockets = pockets
