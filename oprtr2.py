name =(input("please enter your name"))
password=int(input("enter your passcode"))
num=int(input("please inter mobile number"))
if name==str(""):
    print(password)
    if password==int():
        print(num)
        if num==int(len(10)):
            print("login")
        else:
            print("incorrect num")
    else:
        print("incorrect password")
else:
    print("incorrect name")  