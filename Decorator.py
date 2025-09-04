
#Decorator = Function ko input lo → usme kuch add karo → new function return karo
#say_hello = my_decorator(say_hello)

def decorate(func):
    def wrapper():#ye originals value hai
        print("hello")
        func()
        print("welcome to python")
    return wrapper
@decorate
def hello():
    print("how are you")

hello()





def decorate(func):
    def wrapper(a,b):#ye originals value hai
        print("the addtion to your number are")
        func(a,b)
        print("thankyou i") 
    return wrapper
@decorate
def addition(a,b):
    print(f"your total is {a+b}")

addition(23,45)




# *args, #function ke andar unlimited number of arguments accept karna (as a tuple).

# **kwargs → K = Keyword arguments

# Result hamesha dictionary banega
def addition(*args):
    sum = 0
    for i in args:
        sum = sum +i
    print(sum)
addition(1,2,3,4,5,6,7,8,933333)    




# **kwargs → K = Keyword arguments

# Result hamesha dictionary banega



def addition(**kwargs):
    print(kwargs)
addition(a = 2,b = 6,c = 8)