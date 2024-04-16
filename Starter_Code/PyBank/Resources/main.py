#import csv modules
import os
import csv

#set path for file
csvpath = os.path.join('..', 'Resources','budget_data.csv')

#open csv file and skip header row
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
    #setting variables to 0 for iteration counting/summing
    mon_count = 0
    pro_loss_sum = 0
    pl_diff_sum = 0
    prev_row_delta = 0
    #set max and min values to large numbers to return max/min later
    largest_inc = int(-1000000000000)
    largest_dec = int(1000000000000)

#loop through csv file
    for r in csv_reader:
        #counter to count number of rows, adding sum to profit/loss column
        mon_count = mon_count + 1
        pro_loss_sum = pro_loss_sum + int(r[1])
        #Skip row 1 of data to calculate change in profit/loss for each row in data and sum it
        if mon_count > 1:
            pl_diff_row = int(r[1]) - prev_row_delta
            pl_diff_sum = pl_diff_row + pl_diff_sum
            if pl_diff_row > largest_inc:
                largest_inc = pl_diff_row
                inc_date = r[0]
            if pl_diff_row < largest_dec:
                largest_dec = pl_diff_row
                dec_date = r[0]
        prev_row_delta = int(r[1])
#Take average of calculated sum of all profit/loss changes and round to 2 decimal places
    avg_change = round(pl_diff_sum / (mon_count-1) ,ndigits= 2)
 #print out the results to terminal
    print("Financial Analysis")
    print("--------------------------------")
    print(f'Total Months: {mon_count}')
    print(f'Total: ${pro_loss_sum}')
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increase in Profits: {inc_date} (${largest_inc})')
    print(f'Greatest Decrease in Profits: {dec_date} (${largest_dec})')
#print out results to a textfile  
    txtfile = os.path.join("..", "Analysis", "py_bank_analysis.txt")

    with open(txtfile, 'w') as text:
        text.write("Financial Analysis \n")
        text.write("-------------------------------- \n")
        text.write(f'Total Months: {mon_count} \n')
        text.write(f'Total: ${pro_loss_sum} \n')
        text.write(f'Average Change: ${avg_change} \n')
        text.write(f'Greatest Increase in Profits: {inc_date} (${largest_inc}) \n')
        text.write(f'Greatest Decrease in Profits: {dec_date} (${largest_dec}) \n')