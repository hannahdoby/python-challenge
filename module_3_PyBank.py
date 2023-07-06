# Import Dependencies
import os
import csv

# Declare file location
csvpath = os.path.join('module_3_challenge/Mod3_Starter_Code 4','Pybank/Resources','budget_data.csv')

# variables
month_list = []
total_months = 0
total_profit = 0
total_change = 0
avg_change = 0
greatest_inc = 0
month_increase = ""
greatest_dec = 0
month_decrease = ""

# open csv
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header
    csv_header = next(csvreader)
    first_row = next(csvreader)
    
    total_months = 1
    total_profit = int(first_row[1])
    previous = int(first_row[1])

    # go through rows
    for row in csvreader:
        
        # add months and profits
        total_months = total_months + 1

        total_profit = total_profit + int(row[1])

        current = int(row[1])
        change = current - previous
        total_change = change + total_change
        previous = current

        if greatest_inc < change:
            greatest_inc = change
            month_inc = row[0]
        if greatest_dec > change:
            greatest_dec = change
            month_dec = row[0]

    avg_change = round(total_change / (total_months - 1),2)


    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:",total_months)
    print("Total:", "$",total_profit)
    print("Average Change:", "$",avg_change)
    print("Greatest Increase in Profits:", month_inc, "($",greatest_inc,")")
    print("Greatest Decrease in Profits:", month_dec, "($",greatest_dec,")")

    
    output_file = os.path.join("..", "PyBank", "Financial_Analysis.txt")

    with open(output_file,"w") as file:
        file.write("Financial Analysis")
        file.write("\n")
        file.write("----------------------------")
        file.write("\n")
        file.write("Total Months:",total_months)
        file.write("\n")
        file.write("Total:", "$",total_profit)
        file.write("\n")
        file.write("Average Change:", "$",avg_change)
        file.write("\n")
        file.write("Greatest Increase in Profits:", month_inc, "($",greatest_inc,")")
        file.write("\n")
        file.write("Greatest Decrease in Profits:", month_dec, "($",greatest_dec,")")