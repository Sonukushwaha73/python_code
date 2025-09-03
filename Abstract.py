#Abstraction = "Kya karna hai dikhana" + "Kaise karna hai chhupana"

# from abc import ABC, abstractmethod

# Python me abstraction ke liye abc (Abstract Base Class) module use hota hai.

# ABC = ek base class jo batati hai ki ye abstract class hai.

# @abstractmethod = ek aisa method jiska sirf naam hota hai, body nahi hoti.

#--------------------abstraction
   #     car key se start               bike self start
from abc import ABC,abstractmethod
class abstract(ABC):
     @abstractmethod#ye method ko abstract banta hai decorator
#      ABC → abstract class banane ke liye base class.

# abstractmethod → jo method child class ko implement karna compulsory hai.
     def perimeter(self):
          pass
     def area(self):
          pass
class circle(abstract):
    
    def __int__(self,side):# object banate hi value set ho jayegi
         self.side = side
class square(abstract):
     def __init__(self,redius):
          self.redius = redius
          def perimeter(self):
               print("i have a create")
          def area(self):
               print(" i have a create this")
obj = circle()

