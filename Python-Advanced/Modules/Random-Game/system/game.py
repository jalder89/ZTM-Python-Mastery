if __name__ == 'system.game':
    import random

    def get_random(num1, num2):
        return random.randint(num1, num2)


    def start():
        number = get_random(1, 10)
        guesses = 0

        while True:
            try: 
                guess = int(input("\nGuess a number between 1 and 10: "))
                is_num_higher = guess < number
                guesses += 1
            except ValueError as error:
                print('Oops, please enter a whole number.')
            else:
                if guess == number:
                    print(f'You win! The number was {number} and you made {guesses} guesses!\n\n')
                    if str(input('Would you like to play again? (y/n): ')) == 'y':
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