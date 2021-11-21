day=input("enter the day")
if day=="sunday":
    print("ok")
    health_coordinator=input("have you asked to health-coordinator ")
    if health_coordinator=='yes':
        print("health cordinator permission granted")
        place=input("enter place,where you have to go :")
        if place=='hospital':
            print("ok")
            #hospital_name=input("enter hospital name")
            #if hospital_name=='govt hospital'
            #print("hospital name")
            precautoin=input("enter precaution you have taken")
            if precautoin=='mask' or precautoin=='sanitizer':
                print("precation taken")
                disco=input("have you taken permission to DISCO")
                if disco=='yes':
                    print("disco permission granted")
                    time=input("enter time to return between 7am to 7pm")
                    if time<='7':
                        print("time is correct")
                        slack_message=input("write message on slack")
                        if slack_message=='yes':
                            print("permission granted ")
                            retun_slack_message=input("enter return slack message")
                            if retun_slack_message=='yes':
                                print("type message when you return")
                                vaccinated=input("are you vaccinated : ")
                                if vaccinated=='yes':
                                    print("you wont be quarantine")
                                else:
                                    print("you will be quarantine")
                            else:
                                print("type return slack mesaage is necessary")
                        else:
                            print("write slack message first")
                    else:
                        print("enter time between 7am to 7pm")
                else:
                    print("take permission to disco ")
            else:
                print("take mask and sanitizer")
        else:
            print("you cant go")
    else:
        print("ask to health coordinator,it is necessary")
else:
    print("you can go only sunday ")



                                



#b=str(input("have you asked to fm"))
#c#=int(input("enter time between 7am tp 7pm"))
#d=#str(input("have you asked to health co-ordinator"))
#e=yes"
#f="nos"
#if a ==e:
 #   print(b)
  #  if b==e:
   #     print(c)
    #    if 7>=c<=7:
     #       print(d)
      #      if d==e:
       #         print("permission granted")
        #    else:
         #       print("permission not granted")
        #else:
         #   print("time should be between 7am to 7pm")
    #else:
     #   print("take permission to fm now")
#else:
 #   print("ask manager first")
