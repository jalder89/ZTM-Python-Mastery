# Exercise: Checlk for duplicates in a list
some_list = [1, 2, 3, 4, 3, 5, 6, 6, 7, 2]
duplicates = []

for element in some_list:
    count = some_list.count(element)
    if count > 1 and element not in duplicates:
            duplicates.append(element)
print(duplicates)