n1 = int(input("Note 1:"))
n2 = int(input("Note 2:"))

media = (n1+n2)/2

if media <= 4:
    print ("Concept : E - Reproved!")
elif media > 4 and media < 5.9:
    print ("Concept : D - Reproved!")
elif media >= 6.0 and media < 7.4:
    print ("Concept : C - Approved!")
elif media >= 7.5 and media <= 9.0:
    print ("Concept : B - Approved!")
elif media > 9.1 and media < 10:
    print ("Concept : A - Approved!")