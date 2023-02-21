import os #standard library
import csv
from statistics import mean

# import the cvs file of raw data
FilePath= os.path.join("Resources", "Resources", "budget_data.csv")
MonthList = []
ProfitMargin = []

with open(FilePath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        MonthList.append(row[0])
        ProfitMargin.append(int(row[1]))

# Changes in profit from month to month
ProfitChange = []

# Calculates the difference of profit gain to loss in loop
for i in range(1,len(ProfitMargin)):
    ProfitChange.append(ProfitMargin[i]-ProfitMargin[i-1])
        # think in terms of ojects (make lists)
# sum Date column
TotalMonths = len(MonthList)

# net of profit/loss within a period
TotalProfitLoss = sum(ProfitMargin)

# average of the changes
AvProfitChanges = mean(ProfitChange)

# largest increase change over a period
MaxProfit = max(ProfitChange)

# largest decrease change over a period
MinProfit = min(ProfitChange)

MaxMonth = MonthList[ProfitChange.index(MaxProfit) + 1]
print(MaxMonth)

MinMonth = MonthList[ProfitChange.index(MinProfit) + 1]
print(MinProfit)

# Summary output
# \ indicated new line in python
with open("CompleteAssign3.txt", "w", newline="") as textfile:
    textfile.write(f"FinacialAnalysis \n TotalMonths: {TotalMonths} \n \
        Total: {TotalProfitLoss} \n AverageChange: {AvProfitChanges} \n \
            GreatestProfitIncrease: {MaxProfit} MaxMonth: {MaxMonth} \n \
                GreatestProfitDecrease: {MinProfit} MinMonth: {MinMonth}")

# For dataset too big to see in Excel

# NOTE: Analysis should show up in the terminal and exported to a text file
# NOTE: repo needs to have detailed 'README.md' file
