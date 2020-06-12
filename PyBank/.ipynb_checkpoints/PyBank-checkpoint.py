# -*- coding: UTF-8 -*-
# Ian Davies
# Following Python script reads data from budget_data.csv file and outputs a report file.
# Report an analyises of the records to calculate each of the following:
#    The total number of months included in the dataset.
#    The net total amount of Profit/Losses over the entire period.
#    The average of the changes in Profit/Losses over the entire period.
#    The greatest increase in profits (date and amount) over the entire period.
#    The greatest decrease in losses (date and amount) over the entire period.
"""PyBank Homework Starter."""

# @TODO: Import libraries
from pathlib import Path
import csv

# @TODO: Set the path for source and output files
csv_path = Path("Resources/budget_data.csv")
output_path = Path("report.txt")

# @TODO: Initialize the total variables
total = 0
month_count = 0
net_change = 0
prior_change = 0

# @TODO: Initialize the change variables
changes= {} # dict for net changes
profit = 0
p_year =''
loss = 0
l_year=''
change_total = 0
average = 0

underline = "-"*45 #Report title underline

# @TODO: Open the csv file as an object
with open(csv_path, 'r') as csvfile:
           
    # @TODO: Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # @TODO: skip header row
    next(csvreader)
           
    # @TODO: Read each row of data after the header
    for row in csvreader:

        # @TODO: Logic to determine change amount and add to change dict - month and value
        total += int(row[1])
        month_count += 1
        net_change = int(row[1]) - prior_change
        prior_change = int(row[1])
        changes[row[0]] = net_change

# @TODO: Remove first month from dict - not required in calculation 
changes.pop("Jan-2010")

# @TODO: Logic to determine min and max change month
for key, value in changes.items():
    change_total += value
    if loss == 0:
        loss = value
        l_year = key
    elif value < loss:
        loss = value
        l_year = key
    elif value > profit:
        profit = value
        p_year = key

# @TODO: Calculate average of changes         
average = round(change_total/len(changes),2)

# @TODO: Print number of months, total, average, greatest profit and loss to screen
print("Financial Analysis")
print(f"{underline}")
print(f"Total Months: {month_count}")
print(f"Total: ${total}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {p_year} ($ {profit})")
print(f"Greatest Decrease in Profits: {l_year} ($ {loss})")    

# @TODO: Open the output path as a file object
with open(output_path,'w') as file:
    # @TODO: Write number of months, total, average, greatest profit and loss to report file
    file.write("Financial Analysis\n")
    file.write(f"{underline}\n")
    file.write(f"Total Months: {month_count}\n")
    file.write(f"Total: ${total}\n")
    file.write(f"Average Change: ${average}\n")
    file.write(f"Greatest Increase in Profits: {p_year} ($ {profit})\n")
    file.write(f"Greatest Decrease in Profits: {l_year} ($ {loss})\n")  
   
   
