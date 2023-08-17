grade = int(input("Enter your grade: "))

if grade>= 0  and grade <= 30:
    print("You failed")
elif 30 <= grade <= 49:
    print("You scored a D")
elif 50 <= grade <= 59:
    print("You scored a C")
elif 60 <= grade <= 79:
    print("You scored a B")
elif grade>=80 and grade<=100:
    print("You scored an A")
else:
    print("INVALID INPUT")