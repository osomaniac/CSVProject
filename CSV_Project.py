import csv
from datetime import datetime
err = False
open_file = open("death_valley_2018_simple.csv", "r")
open_file_b = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")
csv_file_b = csv.reader(open_file_b, delimiter=",")

header_row = next(csv_file)
header_row_b = next(csv_file_b)

for c, val in enumerate(header_row):
    if(val == "TMIN"):
        min_index = c
    elif(val == "TMAX"):
        max_index = c
    elif(val == "DATE"):
        date_index = c
    elif(val == "NAME"):
        name_index = c

for c, val in enumerate(header_row_b):
    if(val == "TMIN"):
        min_index_b = c
    elif(val == "TMAX"):
        max_index_b = c
    elif(val == "DATE"):
        date_index_b = c
    elif(val == "NAME"):
        name_index_b = c


highs = []
highs_b = []
lows = []
lows_b = []
days = []
days_b = []

for row in csv_file:
    try:
        name = row[name_index]
        high = int(row[max_index])
        low = int(row[min_index])
        current_date = datetime.strptime((row[date_index]), '%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {current_date}.")
        err = True
    else:
        highs.append(high) 
        lows.append(low)
        days.append(current_date)

for row in csv_file_b:
    try:
        name_b = row[name_index_b]
        high = int(row[max_index_b])
        low = int(row[min_index_b])
        current_date = datetime.strptime((row[date_index_b]), '%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {current_date}.")
        err = True
    else:
        highs_b.append(high) 
        lows_b.append(low)
        days_b.append(current_date)


import matplotlib.pyplot as plt

##fig = plt.figure()
fig, ax = plt.subplots(2,1)#

ax[1].plot(days, highs,  c="red", alpha = .75)
ax[1].plot(days, lows, c="blue", alpha = .75)
ax[0].plot(days, highs_b,  c="red", alpha = .75)
ax[0].plot(days, lows_b, c="blue", alpha = .75)
ax[0].set_title(name_b, fontsize=8)
ax[1].set_title(name,fontsize=8)
fig.suptitle(("Temperature comparison between "+name+" and "+name_b), fontsize = 10)
'''ax[0].title("Daily High & Low Temperatures, 2018\nDeath Valley & Sitka", fontsize=16)
ax[0].xlabel("")
ax[0].ylabel("Temperature (F)",fontsize=16)
ax[0].tick_params(axis="both",labelsize=16)
'''
fig.autofmt_xdate()
ax[1].fill_between(days, lows, highs,facecolor='blue',alpha=.10) #x, y1, y2
ax[0].fill_between(days, lows_b, highs_b,facecolor='purple',alpha=.10)


plt.show()

