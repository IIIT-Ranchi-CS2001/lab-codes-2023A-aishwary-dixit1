# Write a python script to find the number of occurrences of a particular character present in the given string 
# using a loop. (Don’t use string methods).


string = input("Enter a string: ")
target = input("Enter the character to count: ")
count = 0

for char in string:
    if char == target:
        count += 1 
print(f"The character '{target}' occurs {count} time(s) in the string.")
