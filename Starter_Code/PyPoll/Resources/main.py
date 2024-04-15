import os
import csv

csvpath = os.path.join('..', 'Resources','election_data.csv')

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
    CCS = "Charles Casper Stockham"
    DD = "Diana DeGette"
    RAD = "Raymon Anthony Doane"
    tot_votes = 0
    CCS_votes = 0
    DD_votes = 0
    RAD_votes = 0
    for r in csv_reader:
        tot_votes = tot_votes + 1
        if r[2] == CCS:
            CCS_votes = CCS_votes + 1
        elif r[2] == DD:
            DD_votes = DD_votes + 1
        elif r[2] == RAD:
            RAD_votes = RAD_votes + 1 
            if CCS_votes > DD_votes and RAD_votes:
                winner = CCS
            elif DD_votes > CCS_votes and RAD_votes:
                winner = DD
            elif RAD_votes > DD_votes and CCS_votes:
                winner = RAD 
    CCS_percent = round((CCS_votes / tot_votes) * 100, ndigits=3)
    DD_percent = round((DD_votes / tot_votes) * 100, ndigits=3)
    RAD_percent = round((RAD_votes / tot_votes) * 100, ndigits=3)   
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
