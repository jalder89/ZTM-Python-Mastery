# Practice with file I/O
try:
    my_file = open('../../requirements.txt', mode='r')
    print(my_file.readlines()[0])
    my_file.close()

    with open('./text.txt', mode='w') as text:
        text.write("Hello, you!")
        text.close()

    with open('./text.txt', mode='r') as text:
        print(text.read())
        text.close()

    with open('./text.txt', mode='r+') as text:
        text.seek(text.read().find('you!'))
        text.write("Jess!")
        text.close()

    with open('./text.txt', mode='a') as text:
        text.write(" I hope you are well!")
        text.close()

    with open('./text2.txt', mode='w') as text:
        text.write("Mode w creates a new file if one doesn't exist!")
        text.close()

    with open('./text.txt', mode='r') as text:
        print(text.read())
        text.close()

    with open('./text2.txt', mode='r') as text:
        print(text.read())
        text.close()

except FileNotFoundError as error:
    print(f"{error} \nTry running from the script's parent directory.")
    