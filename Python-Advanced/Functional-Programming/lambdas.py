# Square the list with lambda
my_list = [5, 4, 3]

print(list(map(lambda item: item*item, my_list)))

# Sort list
tuple_list = [(0, 2), (4, 3), (9, 9), (10, -1)]

tuple_list.sort(key=lambda element: element[1])
print(tuple_list)