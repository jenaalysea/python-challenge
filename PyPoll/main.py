import csv
import os 

#pathway to csv data
csvpath = "Resources/election_data.csv"

#set the value for total vote count 
totalvote = 0

#create empty lists for candidate names to use for individual count and winner counts below
candidatenames = []
electionwinner = []

#create a dictionary that defines the keys / values within our rows 
mydict = {"Charles Casper Stockham": 0, "Diana DeGette": 0, "Raymon Anthony Doane": 0}

#set value for maximum vote counts. Max votes value must be set before the for loop otherwise the iteration started at line 43 would start over with every row rather than each candidate
maxvotes = 0

# read the csv data file, set the delimiter which in this case is a "," and define the headers so the data counts begin on the second row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)

# Begin a for loop to read through the data and begin counting totals
    for row in csvreader:

# Find the total votes count by adding each row one by one (refer to totalvote value set to 0 above)
        totalvote = totalvote + 1
# define the data to start reading on column 3 (candidate names)
        candnames = row[2]
# create an if loop that iterates through the list to group identical names together to get the individual voter counts. Use the "not in" operator in the if loop that will identify when
# a value does not match. 
# Use the .append method to add each unique value together, then referencing the dictionary defined above to group the names together, setting the value count to start at 0, then adding
# the "+ 1" in line 39 to tell each key in the dictionary to iterate through each name to determine individual vote counts.
        if candnames not in candidatenames:
            candidatenames.append(candnames)
            mydict[candnames] = 0
        mydict[candnames] = mydict[candnames] + 1
        
# this for loop will iterate over the candidatenames list (referenced above) to see if the values in the dictionary are greater than maxvotes, which is set at a 0 value above.
# Line 44 reviews if the value now associated for candidates(key in mdict) is greater than the value for maxvotes. Maxvotes is then updated to match the highest value in line 45
    for candidates in candidatenames:
        if mydict[candidates] > maxvotes:
            maxvotes = mydict[candidates]
# Line 47 then sets the value of winningcandidate to the value associated with candidates, which was determined in line 45 within the next values of the dictionary
            winningcandidate = candidates
        

# use the round function to speciy three decimal points as demonstrated in the answer key. Create a list that references the dictionary values now established to show the candidate
# percentage of votes by dividing the value of each key by the total vote for each key, then multiplying by 100 to show a readable percentage figure.   
           
percentagevote = round(mydict["Charles Casper Stockham"]/totalvote * 100,3)
percentagevote1 = round(mydict["Diana DeGette"]/totalvote * 100,3)
percentagevote2 = round(mydict["Raymon Anthony Doane"]/totalvote * 100,3)

#print statements to reflect the values above
print("Election Results")    
print("------------------------------------") 
print(f"Total Votes: ", + totalvote)
print("------------------------------------")
print(f"Charles Casper Stockham: ", percentagevote, mydict["Charles Casper Stockham"])
print(f"Diana DeGette: ", percentagevote1, mydict["Diana DeGette"])
print(f"Raymon Anthony Doane: ", percentagevote2, mydict["Raymon Anthony Doane"])
print(f"-----------------------------------")
print(f"Winner :", winningcandidate)
print(f"-----------------------------------")


    