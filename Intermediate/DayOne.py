myList = ["banana", "cherry", "apple"]
print(myList)

item = myList[0]
print(item)

for items in myList:
    print(items)

print(list(filter(lambda fruit: fruit == "banana", myList)))

print(sorted(myList))

myComplexList = [("name", "Shashi")]
