#import csv modules
import os
import csv

#set path for csv fle
csvpath = os.path.join('..', 'Resources','election_data.csv')
#open csv file and skip header row
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
    #set variables for candidates and vote counts
    CCS = "Charles Casper Stockham"
    DD = "Diana DeGette"
    RAD = "Raymon Anthony Doane"
    tot_votes = 0
    CCS_votes = 0
    DD_votes = 0
    RAD_votes = 0
    #loop through csv file and count the number of rows(total_votes)
    for r in csv_reader:
        tot_votes = tot_votes + 1
        #if statements that count # of votes for each candidate if column reads that specific candidate
        if r[2] == CCS:
            CCS_votes = CCS_votes + 1
        elif r[2] == DD:
            DD_votes = DD_votes + 1
        elif r[2] == RAD:
            RAD_votes = RAD_votes + 1
            #if statements to find out winner based on highest vote total 
            if CCS_votes > DD_votes and RAD_votes:
                winner = CCS
            elif DD_votes > CCS_votes and RAD_votes:
                winner = DD
            elif RAD_votes > DD_votes and CCS_votes:
                winner = RAD 
#create variables to calculate percent votes for each candidate of the total           
    CCS_percent = round((CCS_votes / tot_votes) * 100, ndigits=3)
    DD_percent = round((DD_votes / tot_votes) * 100, ndigits=3)
    RAD_percent = round((RAD_votes / tot_votes) * 100, ndigits=3) 
#print results to terminal  
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {tot_votes}')
    print("-------------------------")
    print(f'{CCS}: {CCS_percent}% ({CCS_votes})')
    print(f'{DD}: {DD_percent}% ({DD_votes})')
    print(f'{RAD}: {RAD_percent}% ({RAD_votes})')
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")
#print results to textfile
txtfile = os.path.join("..", "Analysis", "py_poll_analysis.txt")

with open(txtfile, 'w') as text:
    text.write("Election Results \n")
    text.write("------------------------- \n")
    text.write(f'Total Votes: {tot_votes} \n')
    text.write("------------------------- \n")
    text.write(f'{CCS}: {CCS_percent}% ({CCS_votes}) \n')
    text.write(f'{DD}: {DD_percent}% ({DD_votes}) \n')
    text.write(f'{RAD}: {RAD_percent}% ({RAD_votes}) \n')
    text.write("------------------------- \n")
    text.write(f'Winner: {winner} \n')
    text.write("------------------------- \n")