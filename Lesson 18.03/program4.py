class Figure:
    
    def __init__ (self,c = "green", w = 10, l= 20):
        print("Construct Here for Figure!")
        self.color = c
        self.width = w
        self.length = l

    temp1 = 10
    _temp2 = 20
    __temp3 = 30

    def get_color(self):
        return self.color
    

fig = Figure()

print(fig.temp1)
print(fig._temp2)
print(fig.__temp3)

