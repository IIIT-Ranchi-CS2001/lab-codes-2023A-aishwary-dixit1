# Write a python script to
# Form a list of K random numbers within a limit N where K and N are set by the user. Minimum value of K should be 10.
# Define a function (or two functions) to return the composite numbers and prime numbers of this list as two separate lists.
# Determine the square of all prime numbers and square root of all composite numbers
# Plot both prime numbers Vs their squares and composites Vs their square roots on the same figure object as scatterplots. ( two different subplots on the same figure object)

import matplotlib.pyplot as plt
import random
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def classify_numbers(num_list):
    primes = [num for num in num_list if is_prime(num)]
    composites = [num for num in num_list if num > 1 and not is_prime(num)]
    return primes, composites

K = int(input("Enter the number of random numbers (minimum 10): "))
while K < 10:
    K = int(input("Please enter at least 10 numbers: "))
N = int(input("Enter the upper limit for the random numbers: "))

random_numbers = random.sample(range(2, N+1), K)

primes, composites = classify_numbers(random_numbers)

prime_squares = [p ** 2 for p in primes]
composite_sqrts = [math.sqrt(c) for c in composites]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

ax1.scatter(primes, prime_squares, color='green')
ax1.set_title("Prime Numbers vs Their Squares")
ax1.set_xlabel("Prime Numbers")
ax1.set_ylabel("Squares")

ax2.scatter(composites, composite_sqrts, color='red')
ax2.set_title("Composite Numbers vs Their Square Roots")
ax2.set_xlabel("Composite Numbers")
ax2.set_ylabel("Square Roots")

plt.tight_layout()
plt.show()
