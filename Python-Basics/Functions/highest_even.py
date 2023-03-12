def highest_even(li):
    even_list = []
    for item in li:
        is_even = item % 2 == 0
        if is_even:
            even_list.append(item)
    return max(even_list)


print(highest_even([10, 7, 4, 6, 10, 11, 3, 12, 2, 8]))
print('Hello'[0])
