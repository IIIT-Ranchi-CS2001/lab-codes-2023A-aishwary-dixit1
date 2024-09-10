#Write a python script to find the squares of first n natural numbers. Display both the number and the square as #shown below. Use while loop
#Number    	Square
#1              	1
#2               	4
#…		…

#n		n


n = int(input("Enter the value of n: "))
i = 1
print("Number\tSquare")
while i <=n :
    print(f"{i}\t{i**2}")
    i += 1
