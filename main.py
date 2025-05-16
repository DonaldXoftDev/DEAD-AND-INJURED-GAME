from dead_and_injured_module import (generate_user_pin,
                                     generate_computer_pin, get_user_guesses, generate_computer_guesses,
                                     compare_guesses, narrow_down_guess, message_feedback)

user_pin = generate_user_pin()
computer_pin = generate_computer_pin()



print('\n')
print(f'User pin : {user_pin}')
print(f'Computer pin : {computer_pin}')

Start_Game = True
while Start_Game:
    user_guesses = get_user_guesses()
    computer_is_guessing_again = True
    computer_guesses = generate_computer_guesses()

    print(f'\nuser guessed : {user_guesses}')
    print(f'computer guessed : {computer_guesses}')
    print('\n')

    # user tries to guess the computer's pin
    feed_back_to_user = compare_guesses(user_guesses, computer_pin)
    Start_Game = message_feedback(feed_back_to_user,"player")

    # computer tries to guess the player's pin as well with a random 4 digit guesses
    # computer compares his current guess with all possible combinations of the guess to
    # get the same feedback and narrow down what the user's pin might be
    narrow_down_guess(computer_guesses, user_pin,)
    # the second guess of the computer will be taken from one of the possibilities list







