class Calculus:
    num1 = 0
    num2 = 0

    def __init__(self, x=0, y=1):
        self.num1 = x
        self.num2 = y

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mult(self):
        return self.num1 * self.num2 

    def div(self):
        return self.num1/self.num2




calc = Calculus()