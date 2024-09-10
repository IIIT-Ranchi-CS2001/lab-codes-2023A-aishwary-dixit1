# Write a python script to find the sum of the digits of the given number using a while loop. Display the number 
#  and the sum.


num = int(input("Enter a number: "))  
sum = 0
dup = num
while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10
print(f"Number: {dup}")
print(f"Sum of digits: {sum}")
    