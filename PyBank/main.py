
import os
import csv


budget_data = r"C:\Users\haldu\UBHM-VIRT-DATA-PT-08-2022-U-LOLC\02-Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv"


profit_loss = []
dates = []

csvfile = open(budget_data, 'r')
csvreader = csv.reader(csvfile, delimiter=',')

header = next(csvreader)

for row in csvreader:
    profit_loss.append(int(row[1]))
    dates.append(row[0])

total_months= len(dates)


total_change = [a - b for b, a in zip(profit_loss[:-1], profit_loss[1:])]

def straight_average(n_list):
    total = 0
    length = len(n_list)

    for n in n_list:
        total += float(n)

    return (total/length)

netamount = sum(profit_loss)
total_months = len(dates)

max_val = max(profit_loss)
min_val = min(profit_loss)
listminmax = list(zip(profit_loss, dates))
max_change = max(profit_loss)
max_date = max(dates)
min_change = min(profit_loss)
min_date = min(dates)

results =(f" Total Months: {total_months} \n Total Revenue: {netamount} \n Average Revenue Change: ({straight_average(total_change)}) \n Greatest Increase in Profits: {max(listminmax)[1]}: {max(listminmax)[0]} \n Greatest Decrease in Profits: {min(listminmax)[1]}: {min(listminmax)[0]}")

print("Financial Analysis")
print("-----------------------")
print(results)


csvfile.close()