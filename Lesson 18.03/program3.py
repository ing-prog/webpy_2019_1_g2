class Rectangle:

    def __init__(self, w= 1,l = 1):
        print("Construct Working")
        self.width = w
        self.length = l

   
line = list()
rec1 = Rectangle(4 ,5)
print(rec1.width)
del rec1
print(rec1.width)

    