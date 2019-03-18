title = []
salary = []
description = []
stack = []


vac1 = "Python Developer"
title.append(vac1)
vac1_salary = 135000
salary.append(vac1_salary)

class Vacancy:
    title = "/"
    salary = 0
    description = "/"
    stack = "/"

vac1 = Vacancy()
vac1.title = "Python Dev"
vac1.salary = 135000


vac2 = Vacancy()
vac2.title = "JS Dev"
vac2.salary = 70000

print(vac1.title, vac1.salary, vac1.description)
print(vac2.title, vac2.salary, vac2.description)
print(type(vac1))

