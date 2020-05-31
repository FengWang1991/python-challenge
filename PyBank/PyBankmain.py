import os
import csv

month_count=0
TPnL=0
PnL=[]
month=[]

csvpath=os.path.join('Resources','PyBank_budget_data.csv')

with open (csvpath,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)
    for rows in csvreader:
        month_count+=1
        TPnL=TPnL+int(rows[1])
        month.append(rows[0])
        PnL.append(rows[1])

Average_Change=round((int(PnL[month_count-1])-int(PnL[0]))/(month_count-1),2)

highest_increase_PnL=int(PnL[1])-int(PnL[0])
highest_decrease_PnL=int(PnL[1])-int(PnL[0])
for i in range(month_count-1):
    if int(PnL[i+1])-int(PnL[i])>highest_increase_PnL:
        highest_increase_month=month[i+1]
        highest_increase_PnL=int(PnL[i+1])-int(PnL[i])
    if int(PnL[i+1])-int(PnL[i])<highest_decrease_PnL:
        highest_decrease_month=month[i+1]
        highest_decrease_PnL=int(PnL[i+1])-int(PnL[i])

output_path=os.path.join('Analysis','PyBank.txt')
with open(output_path,'w') as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("----------------------------\n")
    datafile.write(f"Total Months: {month_count}\n")
    datafile.write(f"Total: ${TPnL}\n")
    datafile.write(f"Average  Change: ${Average_Change}\n")
    datafile.write(f"Greatest Increase in Profits: {highest_increase_month} (${highest_increase_PnL})\n")
    datafile.write(f"Greatest Decrease in Profits: {highest_decrease_month} (${highest_decrease_PnL})\n")

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${TPnL}")
print(f"Average  Change: ${Average_Change}")
print(f"Greatest Increase in Profits: {highest_increase_month} (${highest_increase_PnL})")
print(f"Greatest Decrease in Profits: {highest_decrease_month} (${highest_decrease_PnL})")