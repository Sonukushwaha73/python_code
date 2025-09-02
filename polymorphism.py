# Polymorphism = ek hi function/operator ka alag-alag objects ke saath alag behavior dikhाna
# def show():
#    print("hwllo how are you")
# def show():
#    print("you are best friend")
# show()


#method overriding
class Animal:
    def show(self):
        print("Animals is showing")
class Dog(Animal):
    def show(self):
        print("Dog is barking") #yaha overriding ho jata hai

obj=Dog()
obj.show()



#Duck typin 
# Agar ek object duck ki tarah chalti hai, duck ki tarah bolti hai, toh hum usse duck maan lenge — chahe woh actual me duck class ka object ho ya na ho."

class Duck:
    def show(self):
        print("Duck is quacking")
class cat:
    def show(self):

        print("cat is meonig")  
        obj1 =Duck()
        obj2 = cat()      
        obj1.show()
        obj2.show()