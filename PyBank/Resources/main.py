# Look for the data file 
import csv
import io

csvpath = "C:/Users/manen/Desktop/class/ASU/Homework/python-challenge/PyBank/Resources/budget_data.csv"
output_path = "C:/Users/manen/Desktop/class/ASU/Homework/python-challenge/PyBank/Resources/summary.csv"

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    
    csv_header = next(csvreader)
   

#Set variables

    total_months = 0
    total_profit_losses = 0
    last_losses = 0
    change = 0
    sum_profit_losses =0
    greatest_increase =0
    greatest_decrease=0
    greatest_increase_date = ""

#Start the Loop
 
    for row in csvreader:
        
        date= row[0]
        profit_losses = int(row[1])

        total_months= total_months+1
    
        total_profit_losses = total_profit_losses+ profit_losses

        if total_months> 1:
            change= profit_losses-last_losses
            sum_profit_losses = sum_profit_losses + change

            if change > greatest_increase:            
                greatest_increase = change
                greatest_increase_date = date

            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = date
    


        last_losses=profit_losses

       

#calculate average change
average_change = sum_profit_losses/(total_months-1)



# After the loop, print the summary

print('Module 3 challenge')
print('Maria Valdivieso')

print("                                  ")

print('Financial Analysis Summary')
print('------------------------------------------------------------')
print(f'Total Months: {total_months}')
print(f'Total Profit/Losses: $ {total_profit_losses}')
print(f'Average Change: {average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})')

 #Write txt file
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Module 3 challenge'])
    csvwriter.writerow(['Maria Valdivieso'])
    csvwriter.writerow([''])
    csvwriter.writerow(['Financial Analysis Summary'])
    csvwriter.writerow(['------------------------------------------------------------'])
    csvwriter.writerow([f'Total Months: {total_months}'])
    csvwriter.writerow([f'Total Profit/Losses: $ {total_profit_losses}'])
    csvwriter.writerow([f'Average Change: {average_change}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})'])