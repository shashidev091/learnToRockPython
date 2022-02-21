import csv
import pandas

# with open('./weather_data.csv') as weather_data:
#     data = weather_data.readlines()
#     rows = []
#     for row in data:
#         rows.append(row.strip())
#     print(rows)

with open('./weather_data.csv') as data:
    weather_data = csv.reader(data)
    temperatures = []
    for row in weather_data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)

datas = pandas.read_csv('./weather_data.csv')
print(datas['temp'])
