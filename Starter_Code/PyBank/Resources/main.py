import os
import csv

csvpath = os.path.join('..', 'Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, deliimiter=',')
    print(csvreader)