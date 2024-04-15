# python-challenge
In the main.py code of the PyBank part of the homework, I needed assitance with how to calculate the changes in the profit/loss column, summing the changes and calculating the average. I kept getting errors when I tried to create a variable for the change and eventually I asked the BCS Xpert Learning Assistant how to fix the error with my variable.
I was able to to gather the dates on my own but the variable calling is what the learning assistant helped me with. Please see code below for the part in which I referred to the learning assitant for. Also seen in lines 14-16, 28-29, 36 of the main.py file:
pro_loss_sum = 0
pl_diff_sum = 0
prev_row_delta = 0
pl_diff_row = int(r[1]) - prev_row_delta\
pl_diff_sum = pl_diff_row + pl_diff_sum
prev_row_delta = int(r[1])