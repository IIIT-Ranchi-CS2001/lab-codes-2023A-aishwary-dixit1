# Create a list of int using list comprehension [multiple input from keyboard].  Find the mean, median, and mode of 
# the given list (usage of specific modules such as statistics is strictly prohibited. Lab problems are for you to 
# build-up logic and strengthen your understanding of the topic & its concepts).

numbers = [int(x) for x in input("Enter multiple integers separated by spaces: ").split()]

mean = sum(numbers) / len(numbers)

sorted_numbers = sorted(numbers)
n = len(sorted_numbers)

if n % 2 == 0:
    median = (sorted_numbers[(n//2)-1] + sorted_numbers[n//2])/2
else:
    median = sorted_numbers[n//2]
    
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
mode = max(frequency, key=frequency.get)

print(f"\nMean: {mean} \n Median: {median} \n Mode: {mode}")
