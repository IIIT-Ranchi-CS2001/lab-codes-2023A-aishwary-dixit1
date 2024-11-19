# Q1. You are given a dataset that contains daily COVID-19 cases for five countries over a 7-day period. Each row represents a day, and each column represents a country.
# Perform following tasks:
# Basic Statistics:
# Calculate the total number of cases reported in each country over the 7 days.
# Determine the country with the highest total cases.

# Daily Analysis:
# Calculate the average number of cases reported per day across all countries.
# Identify the day with the highest total number of cases across all countries.

# Trends:
# Calculate the percentage increase or decrease in cases for each country from Day 1 to Day 7.
# Find the country with the highest percentage increase.

# Data Transformation:
# Normalize the data (scale all values between 0 and 1) for each country to compare trends more effectively.
# Provide the normalized dataset.

# Visualize the data:
# A line chart showing daily cases for each country
#Highlight the day with the highest total cases across all countries using an annotation or marker.


import numpy as np
import matplotlib.pyplot as plt

# COVID-19 dataset
covid_data = np.array([
    [1500, 2000, 1800, 1200, 900],   # Day 1
    [1600, 2100, 1900, 1300, 950],   # Day 2
    [1700, 2200, 2000, 1400, 1000],  # Day 3
    [1650, 2150, 1950, 1350, 980],   # Day 4
    [1750, 2250, 2050, 1450, 1020],  # Day 5
    [1800, 2300, 2100, 1500, 1050],  # Day 6
    [1900, 2400, 2200, 1600, 1100],  # Day 7
])

countries = ["Country_A", "Country_B", "Country_C", "Country_D", "Country_E"]

# Task 1: Basic Statistics
total_cases = np.sum(covid_data, axis=0)
highest_cases_country = countries[np.argmax(total_cases)]

# Task 2: Daily Analysis
daily_avg_cases = np.mean(np.sum(covid_data, axis=1))
day_with_highest_cases = np.argmax(np.sum(covid_data, axis=1)) + 1

# Task 3: Trends
percentage_changes = ((covid_data[-1] - covid_data[0]) / covid_data[0]) * 100
highest_increase_country = countries[np.argmax(percentage_changes)]

# Task 4: Data Transformation
normalized_data = (covid_data - covid_data.min(axis=0)) / (covid_data.max(axis=0) - covid_data.min(axis=0))

# Task 5: Visualization
plt.figure(figsize=(12, 6))

# Line plot for daily cases
for i, country in enumerate(countries):
    plt.plot(range(1, 8), covid_data[:, i], marker='o', label=country)

# Highlight the day with the highest total cases
highest_day_index = np.argmax(np.sum(covid_data, axis=1))
plt.scatter(highest_day_index + 1, np.sum(covid_data[highest_day_index, :]), color='red', zorder=5, label="Highest Total Cases")

plt.title("Daily COVID-19 Cases for Each Country")
plt.xlabel("Day")
plt.ylabel("Number of Cases")
plt.xticks(range(1, 8))
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("Total cases reported per country:", dict(zip(countries, total_cases)))
print("Country with the highest total cases:", highest_cases_country)
print("Average number of daily cases across all countries:", daily_avg_cases)
print("Day with the highest total cases across all countries:", day_with_highest_cases)
print("Percentage increase/decrease from Day 1 to Day 7 per country:", dict(zip(countries, percentage_changes)))
print("Country with the highest percentage increase:", highest_increase_country)
print("Normalized dataset:")
print(normalized_data)
