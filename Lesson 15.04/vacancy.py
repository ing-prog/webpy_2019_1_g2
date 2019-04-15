
"""WHAT IS IT"""
class Vacancy:
    def __init__(self, title = "", href = "", company = "", requirement = "",salary = "-1"):
        self.__salary = self.__salary_parser( salary)
        self.__title = title
        self.__href = href
        self.__requirement = requirement
        self.__company = company
        
    def get_salary(self):
        return self.__salary 
    def get_requirement(self):
        return self.__requirement 
    def get_title(self):
        return self.__title 
    def get_href(self):
        return self.__href 
    def get_company(self):
        return self.__company 

    def __salary_parser(self, salary):
        temp = salary.split()
        try:
            t = (int(temp[0]) + int(temp[1].split('-')[1]))/2*1000
        except:
            t = (int(temp[1])*1000)

        return t
