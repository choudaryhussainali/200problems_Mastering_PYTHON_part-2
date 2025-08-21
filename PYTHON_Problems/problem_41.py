# Create a CSV file named 'data.csv' with this content:
# name,age
# Ali,21
# Sara,22
# Hassan,23

# Task:
# Write a program that reads the CSV and prints total number of data rows (excluding the header).

# Expected Output:
# Total rows: 3

import csv

def count_csv_rows(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        count = sum(1 for row in reader)
    print("Total rows:", count)

count_csv_rows('data.csv')


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
