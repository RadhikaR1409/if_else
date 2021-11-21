physics=float(input("inter marks p"))
chemistry=float(input("inter marks c"))
biology=float(input("inter marks b"))
mathematics=float(input("inter marks m"))
computer=float(input("inter marks co"))
sum=physics+chemistry+biology+mathematics+computer
per=sum*100/500
if 100>=per>=90:
    print("Grade A")
elif 90>per>=80:
    print("Grade B")
elif 80>per>=70:
    print("Grade C")
elif 70>per>=60:
    print("Grade D")
elif 60>per>=40:
    print("Grade E")
else: 
    print("Grade F")
                        