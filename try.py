num = int(input("enter the first number"))
num2 = int(input("enter the second number"))
num3 = int(input("enter the third number"))
num4 = int(input("enter the fourth number"))

if num>num2 and num2>num3:
    print(num, "Is the greatest")


elif num2>num and num2>num3:
    print(num2, "Is the greatest")

elif num3>num and num3>num2:
    print(num3, "Is the greatest")

elif num4 > num and num4 > num2 and num4>num3:
    print(num4, "Is the greatest")
else:
    print("Wrong input")

