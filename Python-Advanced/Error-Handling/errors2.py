# More practice with error handling
def get_nums(func):
    def wrapper():
        num_number = input('How many numbers would you like to sum? ')
    
        try:
            num_numbers = int(num_number)
        except ValueError as error:
            print(f'Oops, please enter a number! \n{error}')
        else:
            number_list = []
            counter = 0

            while num_numbers > 0:
                counter += 1
                while True:
                    try:
                        number_list.append(int(input(f'Please enter num{counter}: ')))
                    except ValueError as error:
                        print(f'Oops, please enter a number! \n{error}')
                    else:
                        num_numbers -= 1
                        break
            return func(number_list)
    return wrapper


@get_nums
def mysum(*args, **kwargs):
    total = 0

    for number in args[0]:
        try:
            total += number
        except TypeError as error:
            print(f'Oops! {error}')   
    return total   

print(f'Your total is {mysum()}')
