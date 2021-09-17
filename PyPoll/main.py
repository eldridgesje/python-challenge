#importing modules
import os
import csv

#declaring variables
rowCount = 0
candidates = []

#reading CSV
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #establishing header
    csv_header = next(csvreader)
    
    #ITERATING THROUGH VOTES
    for row in csvreader:

        #counting total votes
        rowCount = (rowCount + 1)

        if row[2] not in candidates:
            candidates.append(row[2])



#printing results

print(f"There are {rowCount} total votes.")
print(candidates)


