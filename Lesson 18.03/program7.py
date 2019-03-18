name = "Dorek"


class MyString(str):
    def correct(self, pos=1, letter="a"):
        return self[:pos] + letter + self[pos+1:]


nameNew = MyString(name)
name = nameNew.correct(2, "Y")
# print(nameNew.correct(1,"e"))
print(name)
