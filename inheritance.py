class Factorymumbai: #parent class /super class
    a = "Factory class attribute"
    def hello(self):
        print("hello form factory")
class Factorydelhi(Factorymumbai):#child  subclass [inheritance class ko inherit kar rha hai]
     pass#Agar aap us samay kuch likhna nahi chahte (empty chhodna chahte ho), to pass likh dete ho.
obj = Factorymumbai()
print(obj.a)
obj2 = Factorydelhi()
print(obj2.hello())
