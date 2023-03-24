# Practice with generator functions
def generator_function(num):
    for i in range(num):
        yield i + i

gen = generator_function(5)
print(next(gen))
print(next(gen))