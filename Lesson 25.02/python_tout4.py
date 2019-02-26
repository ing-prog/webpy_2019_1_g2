

#This code for sqrt() calculation

a = float(input('Enter some num: '))


x = 100000000000
i = 0


while True:

    oldValue = x

    x = 1/2*(x**2 +a)/x
    i+=1

    if abs(x - oldValue) < 0.0000000001:
        break
    
print("The sqrt(%f) is equal to %f as %i iterations "%(a,x, i))


