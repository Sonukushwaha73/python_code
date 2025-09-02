#bles) aur methods (functions) ko ek hi class ke andar bundle karna aur data ko direct access se hide karke sirf methods ke through access karna.

#key point
# Encapsulation = Data Hiding + Data Protection.

# Class ke andar __ (double underscore) se private members banate hain.

# Object data ko sirf methods ke through access kar paata hai.

# ---------->ncapsulation ka simple matlab:

# Data (variables) + Functions (methods) → ek jagah(class) me rakhna
# Aur data ko lock ka dena taki koi bahar se direct change na kar sake.
# Data ko access ya change karne ke liye sirf functions ka use karna pade
 



class Factory:
    _a = "pune"   # public variable (_a likho to protected ho jayega)

    def show(self):
        print("this is show method")

class bhopal(Factory):
    def show2(self):
        print(super()._a)   # parent ka variable access

# object banana
obj = bhopal()

# methods call
obj.show()    # parent class method
obj.show2()   # child class method jisme super() use hua
   







#
# 
#    agar [__a] doble underscorre lagane se variable bante hain wo private ho jayta hai
class Factory:
    _a = "pune"   # public variable (_a likho to protected ho jayega)

    def show(self):
        print("Factory. __a")# class ke ander access kar sakte hai
obj =Factory()
obj.show()