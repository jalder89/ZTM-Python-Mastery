# Practice with throwing different types of errors
while True:
    try:
        age = int(input('What is your age? '))
        10/age
    except ValueError as err:
        print(f'Oops! {err} \nPlease enter a number.')
    except ZeroDivisionError as err:
        print(f'Oops {err} \nPlease enter a number higher than 0')
    except:
        print('Something has gone horribly wrong, halting program...')
        break
    else:
        print('Thank you!')
        break
