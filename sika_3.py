
#1. changing the file to inclue all the data from the year of 2018 
#2. change the title to - daily low and high temperature - 2018 
#3. extract low temps from the file and add to chart 
#4. shade in the area between high and low 



import csv
#from shutil import which
from datetime import datetime 

#STEP 1 change the file to the whole year file 
open_file = open("sitka_weather_2018_simple.csv","r")

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

#STEP 3 - lows 
lows = [] 

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
    lows.append(int(row[6]))

print(highs)
print(dates)
print(lows)

import matplotlib.pyplot as plt 

#create figure object 
fig = plt.figure()

#the line is red 
#STEP3 - ADD LOW TO THE CHART 
plt.plot(dates, highs, c="red")
#ADD ANOTHER LINE FOR LOWS 
plt.plot(dates, lows, c="blue")


#STEP 4 - FILL THE COLOR IN BETWEEN 
#we need x-axis location and two y-axis location 
#alpha - to make it light 0 - 1 very heavy 
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)




#the title is on the top 
#STEP 2 change the title 
plt.title("Daily low and high temperatures - 2018", fontsize=16)
#x-axis is none 
plt.xlabel("Month of 2018")
#y-axis 
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)

#for the x-axis 
fig.autofmt_xdate()


#TO COMMENT OUT THE FIRST GRAPH SHOW - THEN THE FIRST GRAPH WILL NOT SHOW UP 

plt.show()


#subplot - 2 rows and 1 column 
#WE HAVE TO CLOSE THE FIRST GRAPH TO LET THE SECOND GRAPH SHOW UP 
plt.subplot(2,1,1)
plt.plot(dates,highs,c='red')
plt.title("Highs")

plt.subplot(2,1,2)
plt.plot(dates,lows,c='blue')
plt.title("Lows")

#which index we are working with 

plt.suptitle("Highs and Lows of Sitka, Alaskas 2018")

plt.show()