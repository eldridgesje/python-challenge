#importing modules
import os
import csv
import locale
locale.setlocale(locale.LC_ALL, '')

#declaring variables
rowCount = 0
profitSum = 0
oldProfit = 0
newProfit = 0
profitChange = 0
changeSum = 0
changeAverage = 0

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

        #finding the change in Profit/Loss
        if rowCount == 1:
            oldProfit = float(row[1])
        else:
            newProfit = float(row[1])
            profitChange = (newProfit - oldProfit)
            print(profitChange)
            changeSum = (changeSum + profitChange)
            oldProfit = float(row[1])
    
    #calculate the average change in Profit/Loss
    changeAverage = (changeSum / (rowCount - 1))
        
    #printing results
    print(f"There are {rowCount} months in the data set.")
    print(f"The total Profit/Loss is {locale.currency(profitSum, grouping=True)}.")
    print(f"The average monthly change in Profit/Loss is {locale.currency(changeAverage, grouping=True)}")