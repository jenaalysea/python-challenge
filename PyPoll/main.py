import csv

csvpath = "Resources/election_data.csv"

totalvote = 0
mydict = {"Charles Casper Stockham": 0, "Diana DeGette": 0, "Raymon Anthony Doane": 0}
candidatevote = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)

    for row in csvreader:
        totalvote = totalvote + 1
        mydict["Charles Casper Stockham"] += 1
        mydict["Diana DeGette"] += 1
        mydict["Raymon Anthony Doane"] += 1





print("Election Results")    
print("------------------------------------") 
print(f"Total Votes: ", + totalvote)
print("------------------------------------")
print(f"Charles Casper Stockham: ", mydict["Charles Casper Stockham"])
print(f"Diana DeGette: ", mydict["Diana DeGette"])
print(f"Raymon Anthony Doane: ", mydict["Raymon Anthony Doane"])

