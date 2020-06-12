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

# @TODO: Initialize the metric variables
total = 0
month_count = 0
profit = 0
p_year =''
loss = 0
l_year=''
average = 0
underline = "-"*45 #Report title underline

# Initialize list of records
records={}

# @TODO: Open the csv file as an object
with open(csv_path, 'r') as csvfile:
           
    # @TODO:
    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # @TODO: skip header row
    next(csvreader)
           
    # @TODO: Read each row of data after the header
    for row in csvreader:

        # @TODO: Logic to determine month count minimum and maximum profit/loss
        total += int(row[1])
        month_count += 1
        
        if loss == 0:
            loss = int(row[1])
            l_year = row[0]
        elif int(row[1]) < loss:
            loss = int(row[1])
            l_year = row[0]
        elif int(row[1]) > profit:
            profit = int(row[1])
            p_year = row[0]
            
# @TODO: Calculate the average 
average = round(total/month_count,2)

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
   
   
