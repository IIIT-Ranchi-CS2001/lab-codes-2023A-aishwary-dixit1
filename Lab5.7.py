
# Enter three lists using list comprehension: Customer name, Customer ID, and shopping points. 
# Construct a list of tuples with and without using built-in function zip().


customer_names = [input(f"Enter name for customer {i+1}: ") for i in range(3)]
customer_ids = [int(input(f"Enter ID for customer {i+1}: ")) for i in range(3)]
shopping_points = [int(input(f"Enter shopping points for customer {i+1}: ")) for i in range(3)]

#Using ZIP function
customer_data_zip = list(zip(customer_names, customer_ids, shopping_points))

print("List of tuples using zip():")
print(customer_data_zip)

#Without Using ZIP function.
customer_data_manual = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(min(len(customer_names), len(customer_ids), len(shopping_points)))]

print("List of tuples without using zip():")
print(customer_data_manual)
