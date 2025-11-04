password = input("enter your password: ")
password_length = len(password)

if password_length > 10 :
    print("Password is strong")
elif password_length >= 6:
    print("Password is medium")
elif password_length < 6:
    print("Password is Weak")

