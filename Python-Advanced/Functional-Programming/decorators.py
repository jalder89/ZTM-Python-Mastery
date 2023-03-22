from time import time

# Decorator Exercise - User a decorator to log function performance
def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function took {t2-t1:.20f} seconds')
        return result
    return wrapper

# Wraps the function in printed stars
def star_wrapper(func):
    def wrapper(*args, **kwargs):
        print('****************')
        func(*args, **kwargs)
        print('****************')
    return wrapper


# Decorator Exercise - Create an @authenticated decorator that 
# only allows the function to run if user has 'valid' set to True
def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            fn(*args, **kwargs)
    return wrapper


# Prints a star wrapped greeting and prints time performance
@star_wrapper
@performance
def hello(greeting='Hello', emoji=':(-_-):'):
    print(greeting, emoji)


# Prints a message if user is valid
@authenticated
def message_friends(user):
    print('message has been sent')


user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

message_friends(user1)
hello('Hey you!', '(^_^)/')