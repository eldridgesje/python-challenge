#importing modules
import os
import csv

#declaring variables

#row counter
rowCount = 0

#current candidate tracker
currentCandidate = ""

#variables to track the winner
maxVotes = 0
winnerIndex = 0
winner = ""

#dictionary to store candidates
candidates = {"name": [],
    "votes": []}

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

        #adding new candidates to the dictionary
        if row[2] not in candidates["name"]:
            candidates["name"].append(row[2])
            candidates["votes"].append(float(1))
        
        #adding votes to existing candidates
        else:
            currentCandidate = candidates["name"].index(row[2])
            candidates["votes"][currentCandidate] = (candidates["votes"][currentCandidate] + 1)


#determine winner

maxVotes = max(candidates["votes"])
winnerIndex = candidates["votes"].index(maxVotes)
winner = candidates["name"][winnerIndex]


#printing results

print(f"There are {rowCount} total votes.")
print(candidates)
print(maxVotes)
print(winnerIndex)
print(winner)

