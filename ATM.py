print("welcome to baroda ATM")
print("insert your card here")
language=input("select your language from - hindi and emnglish :")
if language=="hindi" or language=="english":
    print("processing")
    pin_number=input("enter your pin : ")
    if pin_number=="1409":
        print("processing")
        account_type=input("select your account type (saving or current) : ")
        if account_type=="saving" or account_type=="current":
            print("processing")
            balance=12000
            process=input("please selct any process from- withdrawal and balance inquiry : ")
            if process=="withdrawal":
                print("processing")
                ammount=int(input("inter ammount to be withdrawn : "))
                if ammount<=12000:
                    print("your transaction is processing")
                    print("your remaining balance is:",balance-ammount)
                    receipt=input("do you want receipt of the transaction : ")
                    if receipt=="yes":
                        print("your receipt is being processing")
                    else:
                        print("thank for visiting")
                else:
                    print("enter ammount under 12000")
            else:
                print("balance=12000 ")
        else:
            print("please select account type")
    else:
        print("pin number is incorrect")
else:
    print("please select any valid language")

print(" thanks for visiting us")






#account=['saving','current','salary']
#pin=int(input("enter your four digit pin number:"))
#number=int(input("enter any number between 1 to 25:"))
#option=['withdrawal','balance inquiry']
#ammount=int(input("enter withdrawal amount"))
#balance=12000
#if number>=1 and number<=25:
    #if account in account:
 #       if 0<=pin<=9:
  #          if option=='withdrawal':
   #             if ammount>=balance:
    #                if ammount<=balance:
     #                   print("your transaction is being processed")
      #              else:
       #                 print("can't process")
        #        else:
                   # print("enter ammountless than balance")
         #   else:
#                print("enter any valid option")
 #       else:
  #          print("enter any valid pin number")
   # else:
    #    print("please enter valid account type")
#else:
 #   print("enter any valid number")

