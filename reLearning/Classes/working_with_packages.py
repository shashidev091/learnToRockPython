from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Names", ["Shashi", "Bhushan", "Bhagat"])
table.add_column("age", [27, 29, 28])
table.align = 'l'
print(table)
