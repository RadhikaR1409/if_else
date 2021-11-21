quantity=int(input("inter quantity of your item"))
cost= quantity*100
if cost>=1000:
    print("total value:",cost-cost*0.1)
else:
    print("total value:",cost)