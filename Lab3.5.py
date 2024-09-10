# Write a python script to check whether all the characters present in a string are alphanumeric (uppercase 
# letters, lowercase letters or digits) using for  with else. Print True if all characters are alphanumeric. 
# Otherwise print False.


s = input("Enter a string: ")
flag = 0
for char in s:
    if not char.isalnum(): 
        print(False)
        flag = 0
        break
    else:
        flag = 1
if flag == 1:
    print(True)
