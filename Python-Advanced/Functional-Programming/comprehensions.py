# List Comprehensions
my_list = [char for char in "some text"]
my_list2 = [char for char in "some text without spaces" if char.isalnum()]
my_list3 = [num for num in range(1, 101)]
my_list4 = [num**2 for num in range(1, 101) if num**2 % 2 == 0]

print(my_list)

# Set Comprehension
my_set = {char for char in "some text without duplicates"}
my_set2 = {char for char in "some text without spaces or duplicates" if char.isalnum()}

print(my_set2)

# Dict Comprehensions
my_primer = list(zip(my_set2, my_list4))
my_dict = {key:value for key, value in my_primer}
my_dict2 = {num:num**2 for num in range(1, 101)}
my_dict3 = {key:int(value/2) for key, value in my_primer}
my_dict4 = {key:value for key, value in my_primer if (value / 3.0).is_integer()}

print(my_dict4)

# Duplicate Exercise - Return the duplcates
tester = 'some text with duplicate characters'
my_list = list(set([char for char in tester if tester.count(char) > 1 and char.isalnum()]))
my_set = {char for char in tester if tester.count(char) > 1 and char.isalnum()}
my_dict = {char:tester.count(char) for char in tester if tester.count(char) > 1 and char.isalnum()}

print(my_dict)