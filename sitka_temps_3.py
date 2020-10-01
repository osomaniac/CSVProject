import csv
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)
'''
print(header_row)

for index, column_header in enumerate(header_row): ## tells us the position(index) and the value(column_header)
    print(index,column_header)
'''
highs = []#
lows = []
days = []
for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    days.append((datetime.strptime((row[2]), '%Y-%m-%d')))
#print(highs)
#print(days)
#print(lows)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(days, highs,  c="red", alpha = .75)
plt.plot(days, lows, c="blue", alpha = .75)
plt.title("Daily High & Low Temperatures, 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis="both",labelsize=16)

fig.autofmt_xdate()
plt.fill_between(days, lows, highs,facecolor='blue',alpha=.10) #x, y1, y2#
plt.show()

