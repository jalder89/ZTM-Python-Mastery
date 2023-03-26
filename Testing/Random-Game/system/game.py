if __name__ == 'system.game':
    import random

    def get_random(num1, num2):
        try:
            return random.randint(int(num1), int(num2))
        except ValueError as error:
            print(f'Oops, please enter a whole number.\n{error}')
            return error
    
    def get_input():
        while True:
            try:
                return int(input("\nGuess a number between 1 and 10: "))
            except ValueError as error:
                print(f'Oops, please enter a whole number.\n{error}')
                continue

    def check_guess(guess, number):
        try:
            if int(guess) == int(number):
                return True
            else:
                return False
        except ValueError as error:
            print(f'Oops, please enter a whole number.\n{error}')
            return error

        
    def play_again():
        return str(input('Would you like to play again? (y/n): ')) == 'y'

    def start():
        is_playing = True
        number = get_random(1, 10)
        guesses = 0

        while is_playing:
            guess = get_input()
            is_num_higher = guess < number
            guesses += 1

            if check_guess(guess, number):
                print(f'You win! The number was {number} and you made {guesses} guesses!\n\n')
                is_playing = play_again()

                if is_playing:
                    number = get_random(1, 10)
                    guesses = 0
                    continue
                else:
                    break

            else:
                if guesses < 3:
                    print("I'm sorry, that isn't correct.\n")
                    continue
                else:
                    if is_num_higher:
                        print("i'm sorry, that isn't correct. The number is higher than your guess.\n")
                    else:
                        print("i'm sorry, that isn't correct. The number is lower than your guess.\n")
                continue



else:
    print("Do not run game system files directly, run randomgame.py instead...")