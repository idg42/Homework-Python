# Ian Davies
#Following Python script reads data from two source files and outputs a report file.
#
#Report outputs an analyises of items from the menu items data set with matching items in the sales data to calulate for each item the following:
#1. Count - the total quantity for each menu item sold
#2. Revenue - the total revenue for each menu item sold
#3. COGS - the total cost of goods sold for each menu item sold
#4. Profit - the total profit for each menu item sold
#
# Source File - /Resources/menu_data.csv
#             - /Resources/sales_data.csv
#
# Report File - /Reports/report.txt
#
# Report Format
#
#    menu item {'01-count': 0, '02-revenue': 0, '03-cogs': 0, '04-profit': 0}
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv, sales_data.csv and output path for report
menu_filepath = Path("Resources/menu_data.csv")
sales_filepath = Path("Resources/sales_data.csv")
output_path = Path("Reports/report.txt")

# @TODO: Initialize list objects to hold menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
with open(menu_filepath, 'r') as m_csvfile:
           
    # @TODO:
    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    m_csvreader = csv.reader(m_csvfile, delimiter=',')
   
    # @TODO: skip header row
    next(m_csvreader)
           
    # @TODO: Read each row of data after the header
    for row in m_csvreader:
        menu.append(row)
        
# @TODO: Read in the sales data into the sales list
with open(sales_filepath, 'r') as s_csvfile:
           
    # @TODO:
    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    s_csvreader = csv.reader(s_csvfile, delimiter=',')
   
    # @TODO: skip header row
    next(s_csvreader)
           
    # @TODO: Read each row of data after the header
    for row in s_csvreader:
        sales.append(row)

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for sale in sales:

    # Line_Item_ID(sale[0]), Date(sale[1]), Credit_Card_Number(sale[2]), Quantity(sale[3]), Menu_Item(sale[4])
    # @TODO: Initialize sales data variables
    s_quantity = 0
    
    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if sale[4] not in report.keys() :
        report[sale[4]] = {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0}
   
    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for menu_item in menu:
        
        # Item(menu[0]), Category(menu[1]), Description(menu[2]), Price(menu[3]), Cost(menu[4])
        # @TODO: Initialize menu data variables
        m_price = 0
        m_cost = 0
        
        # @TODO: Calculate profit of each item in the menu data
        m_price = float(menu_item[3])     #capture Price(menu[3])
        m_cost = float(menu_item[4])      #capture Cost(menu[4]) 
        s_quantity = float(sale[3])       #capture Quantity(sale[3])
        revenue = m_price*s_quantity
        cogs = m_cost*s_quantity
        profit = (m_price - m_cost)*s_quantity
        
        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if sale[4] == menu_item[0]:
            
            # @TODO: Print out matching menu data
            print("Sale item:")
            print(sale)
            print()
            print("Menu item:")
            print(menu_item)
            print()
            # @TODO: Cumulatively add up the metrics for each item key
            report[sale[4]]['01-count'] += s_quantity
            report[sale[4]]['02-revenue'] += revenue
            report[sale[4]]['03-cogs'] += cogs
            report[sale[4]]['04-profit'] += profit
            
        # @TODO: Else, the sales item does not equal any of the item in the menu data, therefore no match
        else:
            print(f"{sale[4]} does not equal {menu_item[0]}! NO MATCH!")
            print()
    
    # @TODO: Increment the row counter by 1menu_item[0]
    row_count += 1

# @TODO: Print total number of records in sales data
print(f"Row count {row_count}")

# @TODO: Write out report to a text file (won't appear on the command line output)
with open(output_path,'w') as file:

    for item, stats in report.items():
     file.write(f"{item} {stats}\n")