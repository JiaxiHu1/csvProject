
#using the datetime module 
#adding dates to the x axis for the month of July 2018 



import csv
from shutil import which

open_file = open("sitka_weather_07-2018_simple.csv","r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

#print(type(header_row))

for index,column_header in enumerate(header_row):
    print(index,column_header)

    #matplotlib - lists (work with a lot of lists)
    #value highs 

highs = []

for row in csv_file:
    highs.append(int(row[5]))

print(highs)

import matplotlib.pyplot as plt 

#the line is red 
plt.plot(highs, c="red")

#the title is on the top 
plt.title("Daily high temperatures, July 2018", fontsize=16)
#x-axis is none 
plt.xlabel("")
#y-axis 
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)

plt.show()