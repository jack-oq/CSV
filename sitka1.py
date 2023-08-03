import csv

infile = open('sitka_weather_07-2018_simple.csv', 'r')

csv_file = csv.reader(infile)

header_row = next(csv_file)

for index, col_header in enumerate(header_row):
    print(index, col_header)

highs = []

for row in csv_file:
    highs.append(int(row[5]))

print(highs[:5])
