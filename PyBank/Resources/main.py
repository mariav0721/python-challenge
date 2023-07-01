# Look for the data file 
import csv
import io

csvpath = "C:/Users/manen/Desktop/class/ASU/Homework/python-challenge/PyBank/Resources/budget_data.csv"

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    
    csv_header = next(csvreader)
   

#Set variables

    total_months = 0
    total_profit_losses = 0
    last_losses = 0
    change = 0

#Start the Loop

    for row in csvreader:
        
        date= row[0]
        profit_losses = int(row[1])

        total_months= total_months+1
    
        total_profit_losses = total_profit_losses+ profit_losses
        
        change()
    
    # After the loop, print the summary
    print('Module 3 challenge')
    print('Maria Valdivieso')

    print("                                  ")

    print('Financial Analysis Summary')
    print('------------------------------------------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total Profit/Losses: {total_profit_losses}')


