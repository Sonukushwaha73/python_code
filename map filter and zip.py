#kishi list ke har element par ek function lagna aur newbresult bannana----->map()

a=[1,2,3,44,5]
result = map(lambda x : x*2,a)
print(list(result))



#filter()----->kishi list ke har element pae ek function laganna aurbjo true return kare usko new list me add karna
def even(x):
    if x%2==0:
        return true
    else:
        return False


a = [1,2,3,4,5,6]
reult = filter(even,a)
print(list(result))
