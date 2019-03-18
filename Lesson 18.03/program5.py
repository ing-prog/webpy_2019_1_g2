class Bank:
    __cardHolder = "1234999922221133"

    def __bankChecker(self):
        if self.__cardHolder[:4] =="1234":
            return True

    def InBank(self):
        if( self.__bankChecker()):
            print("THis Card in bank!")

        

bank = Bank()
bank.InBank()
print(bank._Bank__bankChecker())
