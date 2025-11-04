year = int(input("Enter the Year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"The Year {year} is a leap year")
else:
    print(f"The Year {year} is not a leap year")