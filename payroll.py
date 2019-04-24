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


print("Salário bruto      : %0.2f " % salary)
print("(-) IR ({}%)       : {} " .format(ir,_ir))
print("(-) INSS (10 %)    : {} " .format(inss) )
print("FGTS               : %0.2f " % fgts)
print("Total de descontos : %0.2f" % descount)
print("Total Liquido      : %0.2f " % liquid)