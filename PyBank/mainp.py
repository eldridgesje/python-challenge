#importing modules
import os
import csv

#reading CSV
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #printing header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
