import datetime as dt

now = dt.datetime.now()
print(now.year)
year = now.year

if year == 2022:
    print("Still wear mask")

with open('quotes.txt', 'r') as data_file:
    data = data_file.readlines()
    print(data)
