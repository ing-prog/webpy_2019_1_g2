x = []

for i in range(0,1000000):
    if i %2 == 0:
        x.append(i)

#print(x)

y = [j for j in range(0,100000)  if j %2 == 0]
print(y)
