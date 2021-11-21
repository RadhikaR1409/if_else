# password=input("enter the strong password:")
# s=("@,#,$,%,&,*,<,>")
# if password>='a' or password<='z':
#     # if password>='A' or password<='Z':
#     if 0<=password<=9:
#         if password in s:
#             print("this is a strong password")
#         else:
#             print("not a strong password")
#     else:
#         print(" password doesnt include any number")
# else:
#     print("password dont have capital word")
# # else:
# #     print("password dont have lower case")


alphabetes=input("enter the aplphabet: ")
if alphabetes>="a" and alphabetes<="z":
    print("enter the alphabets")
    special_character=input("netr the sprcial_character :")
    if special_character=="@" or special_character=="#":
        print("enter the special characters :")
        number =int(input("enter the number :"))
        if number>=0:
            print(alphabetes+special_character+str(number))
        else:
            print("it is not number")
    else:
        print("it is not a special character")
else:
    print("it is not alphabet")
