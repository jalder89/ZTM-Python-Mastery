def do_stuff(num):
    try:
        return int(num) + 5
    except ValueError as error:
        return error
    except TypeError as error:
        print("Please enter a number")
        return error
    