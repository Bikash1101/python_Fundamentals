num = int(input("Enter A number : "))

fact = 1
for i in range (1 , num+1):
    fact *= i

print(f"The Factorial Of the number {num} is {fact}")