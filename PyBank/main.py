import csv

csvpath = "Resources/budget_data.csv"

totalmonths = 0
totalprofitloss = 0
month_year = []
pandl = []
maxmonth = ["", 0]
lowmonth = ["", 9999999999999999999]
prev_net = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    
    for row in csvreader:
        totalmonths = totalmonths + 1
        totalprofitloss = totalprofitloss + int(row[1])
        net_change = int(row[1]) - prev_net
        low_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        if net_change > maxmonth[1]:
            maxmonth[0] = row[0]
            maxmonth[1] = net_change
        if low_change < lowmonth[1]:
            lowmonth[0] = row[0]
            lowmonth[1] = low_change

        months = row[0]
        profitloss = row[1]
        pandl.append(int(profitloss))
        month_year.append(months)
        changes = 0

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

