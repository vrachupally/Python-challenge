import os 
import csv

inputfile = os.path.join("Resources", "election_data.csv")
outfile = os.path.join("Analysis", "PyPoll.txt")

#Declaring variables
Total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0
Max_votes = 0

#Accessing csv file
with open(inputfile, newline='') as csvfile:

    rows = csv.reader(csvfile, delimiter=',')
    csv_header = next(rows)

    for row in rows:

        Total_votes += 1

        if row[2] == "Khan":
            Khan_votes += 1
        elif row[2] == "Correy":
            Correy_votes += 1
        elif row[2] == "Li":
            Li_votes += 1
        elif row[2] == "O'Tooley":
            OTooley_votes += 1

#Candidate Percentages 
Khan_percent = (Khan_votes/Total_votes)*100
Correy_percent = (Correy_votes/Total_votes)*100
Li_percent = (Li_votes/Total_votes)*100
OTooley_percent = (OTooley_votes/Total_votes)*100

#Candidates Dictionary 
candidates_and_votes = {
    "Khan": Khan_votes,
    "Correy": Correy_votes,
    "Li": Li_votes,
    "O'Tooley": OTooley_votes
}

print(candidates_and_votes["Khan"])

#Winner 
for candidate, votes in candidates_and_votes.items():
    if votes > Max_votes:
        Max_votes = votes
        winner = candidate

#Final Results 
output = (f"""
Election Results
-----------------------------
Total Votes: {Total_votes}
-----------------------------
Khan: {(Khan_votes/Total_votes)*100:.3f}%  ({Khan_votes:,})
Correy: {(Correy_votes/Total_votes)*100:.3f}%  ({Correy_votes:,})
Li: {(Li_votes/Total_votes)*100:.3f}%  ({Li_votes:,})
O'Tooley: {(OTooley_votes/Total_votes)*100:.3f}%  ({OTooley_votes:,})
------------------------------
Winner: {winner}
------------------------------
""")

print(output)

with open(outfile, 'w') as outputfile:
    outputfile.write(output)
