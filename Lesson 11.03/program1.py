def funcName(a,b):
    return a+b

print(type(funcName))

a = funcName
print(a(2,3))

##################################
#Args type

def Sum(a,b):
    return a+b


#
def Sub(a = 0,b = 1):

    return a - b
print(Sub())
print(Sub(2,5))
print(Sub(b = 1000, a = 99999999))

#

def Mult(*temp):
    return temp

numerics = [1,2,3, "Lol","Petya", False, "BAN", 42]
#print( Mult(numerics[0], numerics[1])  )
print(Mult(*numerics))

#def Div(**argsNew):
#    return args

numericsDict = {"x":1, "y":2}


print(type(*numericsDict))



