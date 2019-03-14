def PrintStr(newLine : str):
    print(newLine)



def NewPrinter(abcd):
    abcd("New Printer Works Here")


NewPrinter(PrintStr)

funcList = [PrintStr, NewPrinter]
funcList[0]("List works here")

funcDict = {PrintStr :" Here", NewPrinter:"Here too"}

print("\n\n\n\n")
print(funcDict[PrintStr])


#funcList.sort()
