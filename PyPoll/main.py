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
    "votes": [],
    "percent": []}

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
            candidates["percent"].append(0)
        
        #adding votes to existing candidates
        else:
            currentCandidate = candidates["name"].index(row[2])
            candidates["votes"][currentCandidate] = (candidates["votes"][currentCandidate] + 1)


#determine winner
maxVotes = max(candidates["votes"])
winnerIndex = candidates["votes"].index(maxVotes)
winner = candidates["name"][winnerIndex]

#code to test tie-break functionality
#candidates["votes"][0] = maxVotes
#candidates["votes"][1] = maxVotes

#check for a tie
if candidates["votes"].count(maxVotes) > 1:
    winner = "TIE!"

#printing results

dashes = "----------------------"
openingLines = ["ELECTION RESULTS",dashes,f"Total Votes: {int(maxVotes)}",dashes]
endLines = [dashes,f"Winner: {winner}",dashes]
candidateIndex = 0
percentVote = 0.0

textFile = os.path.join('analysis', 'results.txt')

with open(textFile,"w") as analysisFile:

    analysisFile.writelines("\n".join(openingLines))
    print(len(candidates))
    for candidate in candidates["name"]:
        
        print(candidateIndex)
        percentVote = float((candidates["votes"][candidateIndex]) / rowCount * 100)
        candidates["percent"][candidateIndex] = percentVote
        
        nameString = str(candidates["name"][candidateIndex])
        percentString = str(candidates["percent"][candidateIndex])
        voteString = str(candidates["votes"][candidateIndex])
        
        analysisFile.write("\n")
        analysisFile.write(f"{nameString}: {percentString}% ({voteString})")
        
        candidateIndex = (candidateIndex +1)
    analysisFile.write("\n")
    analysisFile.writelines("\n".join(endLines))


print(candidates)

