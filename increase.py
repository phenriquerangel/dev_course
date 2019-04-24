salary=int(input("Actual salary: "))
newsalary=0
percent =0
if salary < 280:
    newsalary = salary+((salary*20)/100)
    percent = 20
elif salary > 281 and salary < 700:
    newsalary = salary+((salary*15)/100)
    percent = 15
elif salary > 701 and salary < 1500:
    newsalary = salary+((salary*10)/100)
    percent = 10
elif salary > 1501 :
    newsalary = salary+((salary*5)/100)
    percent = 5

difference = newsalary-salary

print("Salary before ajust: %d " % salary)
print("Percent of increase: %d " % percent)
print("Difference on salary: %d" % difference)
print("Salary after ajust: %d " % newsalary)