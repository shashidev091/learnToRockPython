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
data_to_dict = datas.to_dict()

temp_list = datas["temp"].to_list()
print(sum(temp_list) / len(temp_list))

print(datas["temp"].mean())

print(datas["temp"].max())

print(datas.temp.max())

print(datas[datas.day == "Monday"])

print(datas[datas.temp == datas.temp.max()])
