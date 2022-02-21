
#using the datetime module 
#adding dates to the x axis for the month of July 2018 



import csv
#from shutil import which
from datetime import datetime 

open_file = open("sitka_weather_07-2018_simple.csv","r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

#print(type(header_row))

for index,column_header in enumerate(header_row):
    print(index,column_header)

    #matplotlib - lists (work with a lot of lists)
    #value highs 

highs = []
#create a new list for dates 
dates = []

#script time function -- use to test how to transform a string to date 
#test_date = datetime.strptime('2018-07-01', '%y-%m-%d')
#print(test_date)

#use the same for loop to append dates too 
for row in csv_file:
    highs.append(int(row[5]))
    #before append dates, we need to transform the string to date first 
    # we need a big Y for 4 letters 
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(current_date)

print(highs)
print(dates)

import matplotlib.pyplot as plt 

#create figure object 
fig = plt.figure()

#the line is red 
plt.plot(dates, highs, c="red")

#the title is on the top 
plt.title("Daily high temperatures, July 2018", fontsize=16)
#x-axis is none 
plt.xlabel("Month of July 2018")
#y-axis 
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)

#for the x-axis 
fig.autofmt_xdate()

plt.show()