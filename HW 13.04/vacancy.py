

"""Make nice doc"""
class Vacancy:
    def__init__(self,company = "BMSTU", title = "Uborshik",...):
        self.__company = company #all fields in __ini__ should be __private
        self.__title = title
        pass

    def get_company(self):          #for each field in __init__ u should make get and set methods
        return self.__company

    def set_company(self, new_company):
        self.__company = new_company

    def get_title(self):
        pass

    #....
    #....
    #....
