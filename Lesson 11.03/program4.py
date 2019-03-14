def Something(a,b):
    return a+b/(a-b)**2


a = lambda x,y: x+y/(x-y)**2

print(type(a))
print(a(2,3))