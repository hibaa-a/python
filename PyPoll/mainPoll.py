    # importing the modules (operating system library and csv file)
import os
import csv

    # set the path to the csv file
election_data = r"C:\Users\haldu\UBHM-VIRT-DATA-PT-08-2022-U-LOLC\02-Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv"

    # defining variables
votersamount = 0
highestvotes = 0

    # creating dictionaries to store data
candidates = {}
candidatepercentages = {}
candvotes = {}

    # reading the data and splitting by commas
csvfile = open(election_data, 'r')
csvreader = csv.reader(csvfile, delimiter=',')

    # reading the header
header = next(csvreader)

for voter in csvreader:
    votersamount = votersamount + 1
    candidatevotedfor = voter[2]

    try:
        candidates[candidatevotedfor] = candidates[candidatevotedfor] + 1

    except:
        candidates[candidatevotedfor] = 1

    # finding the candidates percentages
for c in candidates:
    votesamount = candidates[c]
    print(votesamount)
    percentage = (votesamount/votersamount) * 100
    candidatepercentages[c] = percentage

    if votesamount > highestvotes:
        highestvotes = votesamount

for c in candidates:
    votesamount = candidates[c]
    candvotes[c] = votesamount
    if votesamount == highestvotes:
        winner = c


   #printing
print("Election Results")
print("----------------")
print(f"Total votes: {votersamount}")
print("----------------")
    # print(candidates)
for c in candidates:
    print(f"{c}: {str(round(candidatepercentages[c], 3))}%  ({candvotes[c]})")
print("----------------")
print(f"Winner: {winner}")
print("----------------")

    # writing the results
f = open(r"C:\Users\haldu\python-challenge\PyPoll\analysis\candidate_data_analysis.txt", 'w')


f.write('Election Results\n')
f.write('----------------\n')
f.write(f"Total votes: {votersamount}\n")
f.write("----------------\n")
    
for c in candidates:
    f.write(f"{c}: {str(round(candidatepercentages[c], 3))}%  ({candvotes[c]})\n")
f.write("----------------\n")
f.write(f"Winner: {winner}\n")
f.write("----------------\n")

csvfile.close()


