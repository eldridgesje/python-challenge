#importing modules
import os
import csv
import locale
locale.setlocale(locale.LC_ALL, '')

#declaring variables
rowCount = 0
profitSum = 0

#reading CSV
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #printing header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #looping through the data
    for row in csvreader:
    
        #counting the number of months of data
        rowCount = (rowCount + 1)
    
        #summing the total Profit/Loss
        profitSum = (profitSum + float(row[1]))
        
    #printing results
    print(f"There are {rowCount} months in the data set.")
    print(f"The total Profit/Loss is {locale.currency(profitSum, grouping=True)}.")