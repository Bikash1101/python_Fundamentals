num = int(input("Enter a number : "))

fact_sum = 0
for i in range (1 , num):
    if num % i == 0:
        fact_sum += i
print(fact_sum)

if fact_sum == num:
    print("The Number is a perfect number ")
else:
    print("The Number is not a perfect number")

