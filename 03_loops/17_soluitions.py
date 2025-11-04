num = int(input("Enter a number: "))
odd = 0
even = 0

for i in range (1 , num+1):
    if i % 2 == 0:
        even += i
    else:
        odd += i
print(f"The sum of odd number is {odd} and even number id {even} in between the number {num}")

        

# num = int(input("Enter The Number: "))
# odd_sum , even_sum  = sum(i for i in range (1 , num+1) if i % 2) , sum(i for i in range (1 , num+1) if i % 2 == 0) 
# print(f"The sum of odd number is {odd_sum} and even number id {even_sum} in between the number {num}")