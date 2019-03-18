class Rectangle:
    width = 0
    length = 0

    def setWidth(self,w):
        self.width = w

    def setLength(self, l):
        self.length = l
        return self.length + 1



rec1 = Rectangle()
print(rec1.setLength(20))
print(rec1.setWidth(30))

print(rec1.width, rec1.length)



