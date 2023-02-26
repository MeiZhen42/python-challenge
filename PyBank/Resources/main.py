import os #standard library
import csv
from statistics import mean

# import the cvs file of raw data
FilePath= os.path.join("Resources", "budget_data.csv")
MonthList = []
ProfitMargin = []

# formatting csv and placing specific columns from csv into 
# empty lists from above
with open(FilePath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        MonthList.append(row[0])
        ProfitMargin.append(int(row[1]))

# read the for loop and place the monthly change in profit in to empty list
ProfitChange = []

for i in range(1,len(ProfitMargin)):
    ProfitChange.append(ProfitMargin[i]-ProfitMargin[i-1])
        # think in terms of ojects (make lists)

# sum of total months in period
TotalMonths = len(MonthList)

# sum of profit
TotalProfitLoss = sum(ProfitMargin)

# average profit 
AvProfitChanges = mean(ProfitChange)

# most profit made in a month
MaxProfit = max(ProfitChange)

# most profit lost in a month 
MinProfit = min(ProfitChange)

# month that had the most profit gain   
MaxMonth = MonthList[ProfitChange.index(MaxProfit) + 1]

# month that had the most profit loss
MinMonth = MonthList[ProfitChange.index(MinProfit) + 1]

# Summary output
# \ indicated new line in python
print(f"FinacialAnalysis \n------------------------\nTotalMonths: {TotalMonths} \n\
    Total: {TotalProfitLoss} \nAverageChange: {AvProfitChanges} \n\
    GreatestProfitIncrease: {MaxMonth} ${MaxProfit} \n\
    GreatestProfitDecrease: {MinMonth} ${MinProfit}"
)

with open("CompleteAssignPyBank.txt", "w", newline="") as textfile:
    textfile.write(f"FinacialAnalysis \n TotalMonths: {TotalMonths} \n \
    Total: {TotalProfitLoss} \n AverageChange: {AvProfitChanges} \n \
    GreatestProfitIncrease: {MaxMonth} ${MaxProfit} \n \
    GreatestProfitDecrease: {MinMonth} ${MinProfit}")

# For dataset too big to see in Excel

# NOTE: Analysis should show up in the terminal and exported to a text file
# NOTE: repo needs to have detailed 'README.md' file
