Mark = int(input("Enter the marks: "))

if Mark >= 101:
    print("Please Verify Your Mark Again")
    exit();

if Mark >= 90:
    print("Grade:A")
elif Mark >= 80:
    print("Grade:B")
elif Mark >= 70:
    print("Grade:C")
elif Mark >=60:
    print("Grade:D")
else:
    print("Fail")