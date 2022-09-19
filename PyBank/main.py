    # importing the modules (operating system library and csv file)
import os
import csv

    # set the path to the csv file
budget_data = r"C:\Users\haldu\UBHM-VIRT-DATA-PT-08-2022-U-LOLC\02-Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv"

    # defining variables
total_months = 0
total = 0
old = 0

    # creating lists to store the data
profit_loss = []
dates = []

    # reading the data and spliiting by commas
csvfile = open(budget_data, 'r')
csvreader = csv.reader(csvfile, delimiter=',')

    # reading the header
header = next(csvreader)

for row in csvreader:
    dates.append(row[0])
    profit_loss.append((int(row[1])) - old)

    total_months = total_months + 1
    total = total + int(row[1])
    old = int(row[1])

del profit_loss[0]

    #finding the average change
total = sum(profit_loss)
averagechange = round((total / (total_months - 1)), 2)

    #finding the min/max profit change
max_val = max(profit_loss)
min_val = min(profit_loss)

indexmax = profit_loss.index(max_val) +1
indexmin = profit_loss.index(min_val) +1

    #finding the min/max dates
maxdate = dates[indexmax]
mindate = dates[indexmin]

    #printing
print("Financial Analysis")
print("-----------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: ${averagechange}')
print(f'Greatest Increase in Profits: {maxdate} (${max_val})')
print(f'Greatest Decrease in Profits: {mindate} (${min_val})')


csvfile.close()