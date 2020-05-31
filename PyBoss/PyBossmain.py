import os
import csv

#dictionary reference from: https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5#file-us_state_abbrev-py

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'}

csvpath=os.path.join('Resources','PyBoss_employee_data.csv')

Emp_ID=[]
First_Name=[]
Last_Name=[]
DOB=[]
SSN=[]
State=[]
with open(csvpath,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header=next(csvreader)
    for rows in csvreader:
        Emp_ID.append(rows[0])
        FirstName,LastName=rows[1].split(" ")
        First_Name.append(FirstName)
        Last_Name.append(LastName)
        Year,Month,Day=rows[2].split("-")
        DOB.append(Month+'/'+Day+'/'+Year)
        SSN1,SSN2,SSN3=rows[3].split("-")
        SSN.append('***-**-'+SSN3)
        State.append(us_state_abbrev[rows[4]])

roster=zip(Emp_ID,First_Name,Last_Name,DOB,SSN,State)
output=os.path.join('Analysis','PyBoss.csv')
with open (output,'w',newline= "") as datafile:
    csvwriter=csv.writer(datafile,delimiter=',')
    csvwriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
    csvwriter.writerows(roster)