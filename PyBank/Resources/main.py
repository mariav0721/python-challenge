# Look for the data file 
import csv

csvpath = "C:/Users/manen/Desktop/class/ASU/Homework/python-challenge/PyBank/Resources/budget_data.csv"

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Skip the header row if it exists
    csv_header = next(csvreader)

    # Read and process each row of the CSV file
    for row in csvreader:
        # Access the data in each row
        date = row[0]
        # Testing conection
        print(date)