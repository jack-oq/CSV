#sitka5.py

# Automatic Indexes: We hard coded the indexes corresponding to the TMIN and TMAX
# columns. Use the header row to determine the indexes for these values, so your program can work
# for Sitka or Death Valley. Use the station name to automatically generate an appropriate title
# for your graph as well.

# create 2 subplot graphs in one visualization so you can see both graphs to compare side by side.

# Matplotlib's pyplot API has a convenience function called subplots() which acts as a
# utility wrapper and helps in creating common layouts of subplots, including the
# enclosing figure object, in a single call.

#dynamic title from file


import csv
from datetime import datetime
import matplotlib.pyplot as plt

fig = plt.figure()

#Sitka Airport Upper Half

infile = open('sitka_weather_2018_simple.csv', 'r')

csv_file = csv.reader(infile)

header_row = next(csv_file)

for index, col_header in enumerate(header_row):
    print(index, col_header)

highs = []
dates = []
lows = []

some_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(type(some_date))

for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    some_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(some_date)
    location1 = row[1]

print(highs[:5])
print(dates[:5])

plt.subplot(2,1,1)

plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title(location1, fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)

fig.autofmt_xdate()

infile.close()

#Death Valley Lower Half
infile = open('death_valley_2018_simple.csv', 'r')

csv_file = csv.reader(infile)

header_row = next(csv_file)

for index, col_header in enumerate(header_row):
    print(index, col_header)

highs = []
dates = []
lows = []

some_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(type(some_date))



for row in csv_file:
    try:
        some_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        location2 = row[1]
    except ValueError:
        print(f"Missing data for {some_date}")
    else:
        highs.append(int(row[4]))
        lows.append(int(row[5]))
        dates.append(some_date)


print(highs[:5])
print(dates[:5])

plt.subplot(2,1,2)

plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title(location2, fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)

fig.autofmt_xdate()

plt.suptitle(f"Temperature comparison between {location1} and {location2}")

plt.show()

infile.close()