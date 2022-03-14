from matplotlib.colors import hexColorPattern
import matplotlib.pyplot as plt
import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")
open_file1 = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")
csv_file1 = csv.reader(open_file1, delimiter=",")

header_row = next(csv_file)
header_row1 = next(csv_file1)


for index, column_header in enumerate(header_row):
    print(index, column_header)
for index, column_header in enumerate(header_row1):
    print(index, column_header)


highs = []
dates = []
lows = []
name1 =[]

fig = plt.figure()

for row in csv_file:
    try:
        the_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        name = row[1]
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs.append(int(row[4]))
        lows.append(int(row[5]))
        dates.append(the_date)
        name1.append(row[1])

plt.subplot(2, 1, 2)
plt.title(name1[1])
plt.xlabel("", fontsize=12)
plt.ylabel("", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)
plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
fig.autofmt_xdate()


highs = []
dates = []
lows = []
name2 = []

for row in csv_file1:
    try:
        the_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        name = row[1]
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs.append(int(row[5]))
        lows.append(int(row[6]))
        the_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(the_date)
        name2.append(row[1])

plt.subplot(2, 1, 1)
plt.title(name2[1])
plt.xlabel("", fontsize=12)
plt.ylabel("", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)
plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
fig.autofmt_xdate()


plt.suptitle("Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US")

plt.show()
