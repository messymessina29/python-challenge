import os
import csv

csvpath = os.path.join('..', 'Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
    mon_count = 0
    pro_loss_sum = 0
    pl_diff_sum = 0
    prev_row_delta = 0
    largest_inc = int(-1000000000000)
    largest_dec = int(1000000000000)

    for r in csv_reader:
        mon_count = mon_count + 1
        pro_loss_sum = pro_loss_sum + int(r[1])
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

    avg_change = round(pl_diff_sum / (mon_count-1) ,ndigits= 2)
    
    print("Financial Analysis")
    print("--------------------------------")
    print(f'Total Months: {mon_count}')
    print(f'Total: ${pro_loss_sum}')
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increase in Profits: {inc_date} (${largest_inc})')
    print(f'Greatest Decrease in Profits: {dec_date} (${largest_dec})')


    
        