a=int(input("inter first number "))
b=int(input("inter second number"))
c=int(input("enter third number"))
if a>b and a>c:
    if b>c:
        print(a,"is greatest",c,"is greatest")
    else:
        print(a,"is greatest", b,"is smallest")
elif b>a and b>c:
    if a>c:
        print(b,"is greatest",c,"is smallest")
    else:
        print(b,'is greatest', a,'is smallest')
elif c>a and c>b:
    if a>b:
        print(c,'is greatest',b,'is smallest')
    else:
        print(c,'is greatest',a,'is smallest')
    