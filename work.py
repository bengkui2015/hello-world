import csv
from matplotlib import pyplot as plt

filename = '20190328.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates = []
    max_vols = []
    min_vols = []
    max_temps = []
    min_temps = []

    for row in reader:
        date = int(row[0])
        dates.append(date)

        max_vol = float(row[7]) * 10
        max_vols.append(max_vol)

        min_vol = float(row[9]) * 10
        min_vols.append(min_vol)


        max_temp = float(row[18])
        max_temps.append(max_temp)

        min_temp = float(row[20])
        min_temps.append(min_temp)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, max_vols, c='red')
plt.plot(dates, min_vols, c='blue')
plt.plot(dates, max_temps, c='green')
plt.plot(dates, min_temps, c='black')

plt.title("Max cell voltage/temperture", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("V/C", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()


