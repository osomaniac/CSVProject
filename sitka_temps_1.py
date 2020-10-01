import csv

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)
'''
print(header_row)
#
for index, column_header in enumerate(header_row): ## tells us the position(index) and the value(column_header)
    print(index,column_header)
'''
highs = []
lows = []#
for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
print(highs)
print(lows)

import matplotlib.pyplot as plt

plt.plot(highs, c="red")
plt.plot(lows, c="blue")
plt.title("Daily High & Low Temps, July 2018", fontsize=16)
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)

plt.show()

