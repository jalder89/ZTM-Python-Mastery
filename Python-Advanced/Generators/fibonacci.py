def fib(num):
    a = 0
    b = 1

    for i in range(num):
            yield a
            temp = a
            a = b
            b = temp + a


def fibolist(num):
    a = 0
    b = 1
    result = []

    for i in range(num):
        result.append(a)
        temp = a
        a = b
        b = temp + a    
    return result  


for num in fib(21):
    print(num)

print(fibolist(21))