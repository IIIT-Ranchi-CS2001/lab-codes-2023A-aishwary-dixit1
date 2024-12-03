import pandas as pd #imported pandas library
import numpy as np #imported numpy library

#Reading the CSV file (taking a variable named "data" for it)
data = pd.read_csv('AQI_Data.csv')

# 1. a) Displaying the first 5 rows of the dataset
print("First 5 rows of the dataset are: \n")
print(data.head(5))
print("\n \n")

#1. b) Displaying the last 6 rows of the dataset
print("Last 6 rows of the dataset are: \n")
print(data.tail(6))
print("\n \n")

#1. c) Showing the summary statistics of all numeric columns
print("Summary statistics of all numeric columns are: \n")
print(data.describe())
print("\n \n")

#1. d) Using numpy to compute the mean of AQI, PM2.5, PM10 
#Mean of AQI
mean_aqi = np.mean(data['AQI'])
print(f"Mean of AQI data: {mean_aqi}\n")
print("\n")

#Mean of PM2.5
mean_pm25 = np.mean(data['PM2.5'])
print(f"Mean of PM2.5 data: {mean_pm25}\n")
print("\n")

#Mean of PM10
mean_pm10 = np.mean(data['PM10'])
print(f"Mean of PM10 data: {mean_pm10}\n")
print("\n")

#------------------------------------------

#Q - A) Check for missing values in the dataset. Write code to replace missing values in numeric columns with the column mean and print the updated dataframe.

# Checking for missing values in the dataset
missing_values = data.isnull().sum()
print("Missing values in each column:\n", missing_values)

#Replacing missing values in numeric columns with the column mean
numeric_columns = ['AQI', 'PM2.5', 'PM10', 'NO2', 'CO', 'O3', 'SO2']
for column in numeric_columns:
    if column in data.columns:
        data[column].fillna(data[column].mean(), inplace=True)

# Printing the updated dataframe
print("Updated dataframe:\n", data)

# ------------------------------------------

#Q - B) Extract the AQI column as a Numpy array. Calculate and display the mean, median, and standard deviation of the AQI values.

#Extracting values of AQI column as a numpy array
aqi_values = data['AQI'].to_numpy()

#Calculating mean of AQI values
mean_aqi = np.mean(aqi_values)

#Calculating median of AQI values
median_aqi = np.median(aqi_values)

#Calculating standard deviation of AQI values
std_aqi = np.std(aqi_values)

print("\n")

#Printing the mean, median and standard deviation of AQI values
print(f"Mean AQI: {mean_aqi} \nMedian AQI: {median_aqi} \nStandard Deviation AQI: {std_aqi}")

