import os
import csv

candidate_list=[]
votes_count=[]
Total_Votes=0
csvpath=os.path.join('Resources','PyPoll_election_data.csv')

with open(csvpath,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header=next(csvreader)
    for rows in csvreader:
        if rows[2] not in candidate_list:
            candidate_list.append(rows[2])
            votes_count.append(0)

with open(csvpath,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header=next(csvreader)
    for rows in csvreader:
        votes_count[candidate_list.index(rows[2])]+=1
        Total_Votes+=1

def space():
    print("-------------------------")

output_path=os.path.join('Analysis','PyPoll.txt')
with open (output_path, "w") as datafile:
    print("Election Results")
    datafile.write("Election Results\n")
    space()
    datafile.write("-------------------------\n")
    print(f"Total Votes: {Total_Votes}")
    datafile.write(f"Total Votes: {Total_Votes}\n")
    space()
    datafile.write("-------------------------\n")

    winner=candidate_list[0]
    for i in range(len(votes_count)):
        Vote_Percentage=votes_count[i]/Total_Votes
        if votes_count[i]>votes_count[candidate_list.index(winner)]:
            winner=candidate_list[i]
        print(f"{candidate_list[i]}: {'%.3f%%' % (Vote_Percentage * 100)} ({votes_count[i]})")          #The format of voting_percentage should be in "%" and keep 3 decimal points.
        datafile.write(f"{candidate_list[i]}: {'%.3f%%' % (Vote_Percentage * 100)} ({votes_count[i]})\n")

    space()
    datafile.write("-------------------------\n")
    print(f"Winner: {winner}")
    datafile.write(f"Winner: {winner}\n")
    space()
    datafile.write("-------------------------\n")