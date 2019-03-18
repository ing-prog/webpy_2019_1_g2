class Style:
    def __init__(self, c = "red",m  = "jigul"):
        #print("Concstruct working here for Auto!")
        self.color = c
        self.model = m

    def getColor(self):
        
        return self.color

    def info(self):
        print("Info for Style Class")
        print(self.color, self.model)


class Auto(Style ):
    def __init__(self, c = "green",m = "bmw", mph=1000, nWheels = 4):
        #print("Auto Construct Work here (before super)")
        super().__init__(c,m)
        #print("Auto Construct Work here (posle super)")
        self.mph = mph
        self.wheels = nWheels

    def info(self):
        print("Info For Auto Class")
        print(self.color, self.model, self.mph, self.wheels)

    


auto = Auto()
style = Style()

auto.info()

print("#############################")
style.info()

    





