# Importing the os, csv and statistics packadges
import os 
import csv
import statistics

# Creating the path to the budget_data
csvpath= os.path.join("HomeWork_3", "budget_data.csv")
filename ="Homework_3/bank_results.txt"
# creating the lists 
total= []
month =[]
change = []

# Reading the csv file
with open(csvpath, newline ='', encoding='utf-8') as csvfile:
    csvreader= csv.reader(csvfile,delimiter= ',')
    print(csvreader)
    header= next(csvreader)
# for loop pulling out data into the lists for total and month
    for row in csvreader:
        month.append(row[0])
        total.append(int(row[1]))
# for loop pulling out the data of change btwn months 
    for i in range(len(total)-1):
        change.append(total[i +1]- total[i])

# Final variables 
sumTotal = sum(total)
avgChange= statistics.mean(change)
maxChange= max(change)
minChange = min(change)
monthCount = len(month)


print("Financial Analysis")
print("-------------------------------")
print("Total Months: " + str(monthCount))
print("Total Profits: " + str(sumTotal))
print("Average Change :" + str(avgChange))
print("Greatest Increase in Profits: " + str(maxChange))
print("Greatest Decrease in Profits: " + str(minChange))

# writing the new file
with open(filename, 'w') as file:
    file.write("Financial Analysis \n")
    file.write("-------------------------------\n")
    file.write("Total Months: " + str(monthCount) + "\n")
    file.write("Total Profits: " + str(sumTotal) + "\n")
    file.write("Average Change :" + str(avgChange) + "\n")
    file.write("Greatest Increase in Profits: " + str(maxChange) + "\n")
    file.write("Greatest Decrease in Profits: " + str(minChange) + "\n")








