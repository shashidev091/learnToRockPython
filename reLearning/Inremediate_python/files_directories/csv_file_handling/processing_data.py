import pandas

park_data = pandas.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

# print(park_data.columns)

new_data = {
    "black_squirrel": len(park_data[park_data["Primary Fur Color"] == "Black"]),
    "gray_squirrel": len(park_data[park_data["Primary Fur Color"] == "Gray"]),
    "red_squirrel": len(park_data[park_data["Primary Fur Color"] == "Cinnamon"]),
}

# data = pandas.DataFrame(new_data)
# print(new_data)

data_dict = {
    "Fur color": ['black_squirrel', 'gray_squirrel', 'red_squirrel'],
    "total_count": [new_data['black_squirrel'], new_data['gray_squirrel'], new_data['red_squirrel']]
}

formatted_data = pandas.DataFrame(data_dict)
print(formatted_data)
