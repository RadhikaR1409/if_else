

a= float(input("inter elctricity unit"))
bill1= a*0.50
bill2= a*0.75
bill3= a*1.20
bill4= a*1.50
if a<=50:
    print(bill1)
    if a>50 and a<=100:
        print(bill2)
        if a>100 and a<=200:
            print(bill3)
else:
    print(bill4)
    
