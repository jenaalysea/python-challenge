import csv

#pathway to csv data

csvpath = "Resources/budget_data.csv"

#set the value for total months & profit&loss count within each column 
totalmonths = 0
totalprofitloss = 0

# create open lists to store data for the date column and the profit and loss column - which will aid with the for loop below when iterating through the list
month_year = []
pandl = []

# create lists to store data for greatest and lowest change -- with the maximum change holding 0 as the value for the column to ensure most if not all values are higher than 0, and 
# an extremeley high number in the low month column value to ensure all values are < the value set in the list
maxmonth = ["", 0]
lowmonth = ["", 9999999999999999999]

# set the value at 0 - this value defines the difference in each integer within column 2 which will help define the "great change" figure in the print statement below
prev_net = 0

# read the csv data file, set the delimiter which in this case is a "," and define the headers so the data counts begin on the second row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)

 # Begin a for loop to read through the data and begin counting totals   
    for row in csvreader:

 # Find the total months count by adding each row one by one (refer to totalmonths value set to 0 above)       
        totalmonths = totalmonths + 1
# totalprofitloss value is iterating row by row to determine the overall total dollar amount earned (refer to totalprofitloss set to 0 above)
        totalprofitloss = totalprofitloss + int(row[1])
# determine the difference in column 2 values by continuing the iteration row by row to subtract difference of each row by the next figure listed in column 2
        net_change = int(row[1]) - prev_net
        low_change = int(row[1]) - prev_net
        prev_net = int(row[1])

# the if loop iterates through the list of the previously calculated values to state, within column 2, if the next row has a greater value, then the value of the net change is updated to reflect the greater value
        if net_change > maxmonth[1]:
            maxmonth[0] = row[0]
            maxmonth[1] = net_change

# the if loop iterates through the list of the previously calculated values to state, within column 2, if the next row has a lower value, then the value of the net change is updated to reflect the lower value
        if low_change < lowmonth[1]:
            lowmonth[0] = row[0]
            lowmonth[1] = low_change

# outside of the if statements, created a list to hold the values of column 1 (the months) and then column 2 (the total profit/losses) and within the same for loop created a list to 
# add appended values to each list.
        months = row[0]
        profitloss = row[1]
        pandl.append(int(profitloss))
        month_year.append(months)
        changes = 0

# then take the length of the pandl (profit and loss) list created above and subtract the value of the difference from each row, one by one, using the =+ to increment the values to
# state the total amount of the difference should be deducted from the next row -- pandl[1 + 1] defining all rows within column 2, and pandl[i] referring to the list holding the 
# figure that is the difference in values between the two rows. Once the loop is completed, the changes value goes back to 0 and allows the loop to repeat, appending each "difference" in 
# in the pandl list to reference later to create the average change figure.
# Line 68 then takes the value assigned to changes and divides by the total in the range defined in line 65 of the for loop.

    for i in range(len(pandl) - 1):
        changes += pandl[i + 1] - pandl[i]
        average_change = changes / (len(pandl) - 1)

 
        
print("Financial Analysis")    
print("------------------------------------")   
print(f"Total Months: ", totalmonths)
print(f"Total: $", totalprofitloss)
print(f"Average Change $", average_change)
print(f"Greatest Increase in Profits: (${maxmonth[1]})\n")
print(f"Greatest Decrease in Profits: (${lowmonth[1]})\n")

