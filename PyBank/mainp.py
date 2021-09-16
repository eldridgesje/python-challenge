#importing modules
import os
import csv
import locale
locale.setlocale(locale.LC_ALL, '')

#declaring variables

#the number of total rows
rowCount = 0
#the total profit
profitSum = 0
#the profit of the previous row
oldProfit = 0
#the profit of the current row
newProfit = 0
#the difference in profit between the previous and current rows
profitChange = 0
#the maximum increase in profit
maxProfit = 0
#the maximum decrease in profit
maxLoss = 0
#the date of the maximum increase in profit
maxProfitDate = 0
#the date of the maximum decrease in profit
maxLossDate = 0
#the sum of all the changes in profit
changeSum = 0
#the average change in profit
changeAverage = 0

#reading CSV
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #printing header
    csv_header = next(csvreader)

    #LOOPING THROUGH THE DATA
    for row in csvreader:
    
        #counting the number of months of data
        rowCount = (rowCount + 1)
    
        #summing the total Profit/Loss
        profitSum = (profitSum + float(row[1]))

        #DOING THE PROFIT/LOSS CALCULATIONS

        #establish the first value for the prior month's profit
        if rowCount == 1:
            oldProfit = float(row[1])

        #calculate on remaining rows
        else:
            #assign the current month's profit
            newProfit = float(row[1])

            #caculate the change between the current month and the prior month
            profitChange = (newProfit - oldProfit)

            #add the change in profit to the running total
            changeSum = (changeSum + profitChange)

            #assign the current month to the prior month variable for use in the next month
            oldProfit = float(row[1])

            #decide if the current month's change is the highest so far
            if profitChange > maxProfit:
                maxProfit = profitChange
                maxProfitDate = row[0]

            #decide if the current month's change is the lowest so far
            elif profitChange < maxLoss:
                maxLoss = profitChange
                maxLossDate = row[0]
            
    
    #calculate the average change in Profit/Loss
    changeAverage = (changeSum / (rowCount - 1))
        
    #printing results 
    
    line1 = "Financial Analysis"
    line2 = "----------------------------"
    line3 = f"Total Months: {rowCount}"
    line4 = f"Total: {locale.currency(profitSum, grouping=True)}"
    line5 = f"Average Change: {locale.currency(changeAverage, grouping=True)}"
    line6 = f"Greatest Increase in Profits: {maxProfitDate} / {locale.currency(maxProfit,grouping=True)}"
    line7 = f"Greatest Decrease in Profits: {maxLossDate} / {locale.currency(maxLoss,grouping=True)}"

    textFile = os.path.join('analysis', 'analysis.txt')
    analysisFile = open(textFile,"w")
    analysisFile.writelines([line1,"\n", line2, "\n", line3, "\n", line4, "\n", line5, "\n", line6, "\n", line7])

    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    print(line7)
