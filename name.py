a=int(input("inter first number "))
b=int(input("inter second number"))
c=int(input("enter third number"))
if a>b and a>c:
    if b>c:
        print(a,"is greatest",c,"is greatest")
    else:
        print(a,"is greatest", b,"is smaalest")
elif b>a and b>c:
    if a>c:
        print(b,"is greatest",c,"is small")
    else:
        print(b,'is great', a,'is small')
elif c>a and c>b:
    if a>b:
        print(c,'is great',b,'is small')
    else:
        print(c,'is great',a,'is small')
    