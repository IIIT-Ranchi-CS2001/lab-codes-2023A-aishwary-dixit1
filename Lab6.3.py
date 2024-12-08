# Write program to define a function my_max() to complete the following tasks: 
# [Usage of built-in function max() is strictly prohibited]
# If a list of integers is passed as the input argument, the function shall return maximum value present in the list
# If a set is passed, maximum value present in the list
# If a tuple is passed, maximum value present in the tuple
# Hint: Pass the container type unpacked using *


def my_max(*args):
    if len(args) == 0:
        raise ValueError("Empty container passed.")
    max_value = args[0]
    for num in args[1:]:
        if num > max_value:
            max_value = num
    return max_value

my_list = [3, 5, 7, 2, 8]
print("Maximum in list:", my_max(*my_list))

my_set = {4, 9, 1, 6}
print("Maximum in set:", my_max(*my_set))

my_tuple = (10, 15, 8, 20, 13)
print("Maximum in tuple:", my_max(*my_tuple))
