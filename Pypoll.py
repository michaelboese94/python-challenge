# Importing the Dependencies
import os
import csv
import pandas as pd

# creating the path
csvpath= os.path.join("HomeWork_3", "election_data.csv")

#creating a data frame for the pandas variable
filename = "Homework_3/election_data.csv"
df = pd.read_csv(filename)

# creating the variables 
candidates = df["Candidate"].unique()
khan = 0
correy = 0
li = 0
otooley = 0
votes = 0
# creating the path
file_output = "Homework_3/poll_results.txt"

# reading the cs file
with open(csvpath, newline ='', encoding='utf-8') as csvfile:
    csvreader= csv.reader(csvfile,delimiter= ',')
    header= next(csvreader)
    for row in csvreader:
# calculating total votes 
        votes += 1
# calculating total votes for each candidate  
        if row[2] == str("Khan"):
            khan += 1
        elif row[2] == str("Correy"):
            correy += 1
        elif row[2] == str("Li"):
            li += 1
        elif row[2] == str("O'Tooley"):
            otooley +=1

# Calculating the percentages     
percent_khan = float((khan / votes) *100)
percent_correy = float((correy / votes) *100)
percent_li = float((li / votes) *100)
percent_otooley = float((otooley / votes) *100)
winner = ""
print(percent_khan)

# if statment which calculates winner
if (khan > correy and khan > li and khan > otooley):
    winner = str("Khan")
elif (correy > khan and correy > li and correy > otooley):
    winner = str("Correy")
elif (li > khan and li > correy and li > otooley):
    winner = str("Li")
elif (otooley > khan and otooley > correy and otooley > li):
    winner = str("O'Tooley")

# printing results 
print("Election Results")
print("------------------------------------------")
print("Total Votes: " + str(votes))
print("------------------------------------------")
print("Khan: " + "%" +str(percent_khan) + "  Total: " + str(khan))
print("Correy: " + "%" +str(percent_correy) + "  Total: " + str(correy))
print("Li: " + "%" +str(percent_li) + "  Total: " + str(li))
print("O'Tooley: " + "%" +str(percent_otooley) + "  Total: " + str(otooley))
print("------------------------------------------")
print("And The Winner is ")
print(str(winner) + "!")


# writing the new file
with open(file_output, 'w') as file:
    file.write("-------------------------------------- \n")
    file.write("Election Results " + "\n")
    file.write("------------------------------------- \n")
    file.write("Total Votes: " + str(votes) +"\n")
    file.write("------------------------------------- \n")
    file.write("Khan: " + "%" +str(percent_khan) + "  Total: " + str(khan) + "\n")
    file.write("Correy: " + "%" +str(percent_correy) + "  Total: " + str(correy) + "\n")
    file.write("Li: " + "%" +str(percent_li) + "  Total: " + str(li) + "\n")
    file.write("O'Tooley: " + "%" +str(percent_otooley) + "  Total: " + str(otooley) + "\n")
    file.write("------------------------------------- \n")
    file.write("Winner: " + winner + "\n" )
    file.write("------------------------------------- ")
