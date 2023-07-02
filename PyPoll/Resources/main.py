#look fro the data file
import csv

csvpath = "C:/Users/manen/Desktop/class/ASU/Homework/python-challenge/PyPoll/Resources/election_data.csv"
output_path = "C:/Users/manen/Desktop/class/ASU/Homework/python-challenge/PyPoll/Resources/summary.csv"

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

    # Set variables
    charles_votes = 0
    diana_votes = 0
    raymon_votes = 0
    total_votes = 0

    # Start the loop
    for row in csvreader:
        if row[2] == "Charles Casper Stockham":
            charles_votes =charles_votes+ 1
        elif row[2] == "Diana DeGette":
            diana_votes = diana_votes+1
        elif row[2] == "Raymon Anthony Doane":
            raymon_votes = raymon_votes+1  
    

# After the loop, print the summary

print('Module 3 challenge')
print('Maria Valdivieso')

print("                                  ")

print('Elections Results')
print('------------------------------------------------------------')
#print(f'Total Votes: {total_votes}')

print('------------------------------------------------------------')

print(charles_votes)
print(diana_votes)
print(raymon_votes)
#print(f'Charles: {charles_percentage:}% ({charles_votes})')
#print(f'Diana: {diana_percentage:}% ({diana_votes})')
#print(f'Raymon: {raymon_percentage:}% ({raymon_votes})')
#print('------------------------------------------------------------')


 #Write txt file
#with open(output_path, 'w', newline='') as csvfile:
    #csvwriter = csv.writer(csvfile)
    #csvwriter.writerow(['Module 3 challenge'])
    #csvwriter.writerow(['Maria Valdivieso'])
    #csvwriter.writerow([''])
    #csvwriter.writerow(['Financial Analysis Summary'])
    #csvwriter.writerow(['------------------------------------------------------------'])
    #csvwriter.writerow([f'Total Months: {total_months}'])
    #csvwriter.writerow([f'Total Profit/Losses: $ {total_profit_losses}'])
    #csvwriter.writerow([f'Average Change: {average_change}'])
    #csvwriter.writerow([f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})'])
    #csvwriter.writerow([f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})'])