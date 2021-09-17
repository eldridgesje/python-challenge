#importing modules
import os
import csv

### DECLARING VARIABLES ###

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

#variables for use in writing results
candidateIndex = 0
percentVote = 0.0


#reading CSV
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #establishing header
    csv_header = next(csvreader)
    


    ### ITERATING THROUGH VOTES ###

    for row in csvreader:

        #counting total votes
        rowCount = (rowCount + 1)

        #adding new candidates to the dictionary
        if row[2] not in candidates["name"]:
            candidates["name"].append(row[2])
            candidates["votes"].append(int(1))
            candidates["percent"].append(0)
        
        #adding votes to existing candidates
        else:
            currentCandidate = candidates["name"].index(row[2])
            candidates["votes"][currentCandidate] = (candidates["votes"][currentCandidate] + 1)


### DETERMINE WINNER ###

#finding the maximum number of votes
maxVotes = max(candidates["votes"])

#finding the index of the maximum number of votes
winnerIndex = candidates["votes"].index(maxVotes)

#finding the candidate with the winning index
winner = candidates["name"][winnerIndex]


### code to test tie-break functionality
### candidates["votes"][0] = maxVotes
### candidates["votes"][1] = maxVotes

#check for a tie by counting number of candidates with winning vote count
if candidates["votes"].count(maxVotes) > 1:
    winner = "TIE!"

#printing results to CSV

#creating dashed-line variable for use throughout printing
dashes = "------------------------"

#creating list of lines for the first part of the summary
openingLines = ["ELECTION RESULTS",dashes,f"Total Votes: {int(maxVotes)}",dashes]

#creating list of lines for the last part of the summary
endLines = [dashes,f"Winner: {winner}",dashes]

#creating and opening text file to hold results
textFile = os.path.join('analysis', 'results.txt')

with open(textFile,"w") as analysisFile:

    #writing first part of summary
    analysisFile.writelines("\n".join(openingLines))

    #looping through candidates to create body of summary
    for candidate in candidates["name"]:
        
        #calculating percent vote for each candidate
        percentVote = round(float((candidates["votes"][candidateIndex]) / rowCount * 100),2)
        candidates["percent"][candidateIndex] = percentVote
        
        #turning candidate data to string to write to file
        nameString = str(candidates["name"][candidateIndex])
        percentString = str(candidates["percent"][candidateIndex])
        voteString = str(candidates["votes"][candidateIndex])
        
        #writing body to file
        analysisFile.write("\n")
        analysisFile.write(f"{nameString}: {percentString}% ({voteString})")
        
        #advancing the candidate index
        candidateIndex = (candidateIndex +1)

    #writing the end of the summary
    analysisFile.write("\n")
    analysisFile.writelines("\n".join(endLines))

#reading from the csv file
with open(textFile) as analysisFile:

    printOut = analysisFile.read()

    #displaying the csv data on the console
    print(printOut)

