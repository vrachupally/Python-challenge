import csv
import os

inputfile = os.path.join('Resources', 'budget_data.csv')
outfile = os.path.join('Analysis', 'PyBank.txt')

#Declaring variables
Months_total = 0
Net_total = 0
Previous_budget = 0
Change_total = 0
Greatest_increase = 0
Greatest_decrease = 0
Greatest_increase_date = ""
Greatest_decrease_date = ""

#Accessing csv files
with open(inputfile) as csvfile:

    csvfile.readline()
    
    rows = csv.reader(csvfile)

    Change_count = 0
    change = 0

    for row in rows:
        Months_total += 1

        Current_budget = int(row[1])
        Net_total += Current_budget

#Total Change
        if Previous_budget != 0:
            change = Current_budget - Previous_budget
            Change_total += change
            Change_count +=1

        Previous_budget = Current_budget
#Greatest increase in profit 
        if change > Greatest_increase:
            Greatest_increase = change
            Greatest_increase_date = row[0]
#Greatest decrease in profit
        if change < Greatest_decrease:
            Greatest_decrease = change
            Greatest_decrease_date = row[0]

#Final results
output = (f"""
Financial Analysis
----------------------------
Total Months: {Months_total}
Total: ${Net_total:,}
Average  Change: ${Change_total/Change_count:,.2f}
Greatest Increase in Profits: {Greatest_increase_date} (${Greatest_increase:,})
Greatest Decrease in Profits: {Greatest_decrease_date} (${Greatest_decrease:,})
""")

print(output)

with open(outfile, 'w') as outputfile:
    outputfile.write(output)