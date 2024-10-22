
# Define a function my_zip() that can form a list of tuples by iterating the following customer details:- 
# ‘customer Name, customer ID , shopping points’ and based on the keyword parameter ‘strct’: If strct = True, 
# zipping shall be done only if all lists are of equal length. If strct = False, zipping can be done by 
# taking the minimum length of the iterable.


def my_zip(customer_names, customer_ids, shopping_points, strct=True):
    if strct:
        if len(customer_names) == len(customer_ids) == len(shopping_points):
            return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]
        else:
            raise ValueError("Lists are of unequal length. Zipping cannot proceed when strct=True.")
    else:
        min_length = min(len(customer_names), len(customer_ids), len(shopping_points))
        return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(min_length)]

customer_names = ['Alice', 'Bob', 'Charlie']
customer_ids = [101, 102, 103]
shopping_points = [50, 30] 

result = my_zip(customer_names, customer_ids, shopping_points, strct=False)
print("Result with strct=False:", result)

try:
    result_strict = my_zip(customer_names, customer_ids, shopping_points, strct=True)
    print("Result with strct=True:", result_strict)
except ValueError as e:
    print(e)
