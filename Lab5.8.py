
# Sort the list of tuples constructed above with and without sorted function. 

customer_names = [input(f"Enter name for customer {i+1}: ") for i in range(3)]
customer_ids = [int(input(f"Enter ID for customer {i+1}: ")) for i in range(3)]
shopping_points = [int(input(f"Enter shopping points for customer {i+1}: ")) for i in range(3)]

customer_data_zip = list(zip(customer_names, customer_ids, shopping_points))

#Using Sorted Function
sorted_customer_data = sorted(customer_data_zip, key=lambda x: x[1])

print("Sorted list of tuples using sorted():")
print(sorted_customer_data)

customer_data_manual_copy = customer_data_zip.copy()

#Without Using Sorted function (Bubble Sort Algorithm)
for i in range(len(customer_data_manual_copy)):
    for j in range(0, len(customer_data_manual_copy) - i - 1):
        if customer_data_manual_copy[j][1] > customer_data_manual_copy[j + 1][1]:
            customer_data_manual_copy[j], customer_data_manual_copy[j + 1] = customer_data_manual_copy[j + 1], customer_data_manual_copy[j]

print("Sorted list of tuples without using sorted():")
print(customer_data_manual_copy)
