hoursp=int(input("Value hours: "))
hourst=int(input("Worked hours: "))

salary=hoursp*hourst

if salary <= 900:
    ir = 0
elif salary > 901 and salary < 1500:
    ir = 5
elif salary > 1501 and salary < 2500:
    ir = 10
elif salary > 2501:
    ir = 20


sindicate = (salary*3)/100
inss = (salary*10)/100
fgts = (salary*11)/100
current = (salary*ir)/100
_ir=(salary*ir)/100
descount=_ir+inss
liquid= salary-descount


print("Salário bruto      : {:.2f}" .format(salary))
print("(-) IR ({:2.0f}%)       : {:.2f}" .format(ir,_ir))
print("(-) INSS (10 %)    : {:.2f}" .format(inss))
print("FGTS               : {:.2f}" .format(fgts))
print("Total de descontos : {:.2f}" .format(descount))
print("Total Liquido      : {:.2f}" .format(liquid))