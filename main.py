from dead_and_injured_module import (gen_pin_or_guess,
                                     generate_computer_pin, generate_computer_guesses,
                                     compare_guesses, computer_guessing_strategy, message_feedback)

from prettytable import PrettyTable
from arts import game_logo, welcome_image
import time
import itertools

dead_and_injured_table = PrettyTable()
computer_guess_table = PrettyTable()

dead_and_injured_table.field_names = ['User guesses', 'Feedback to user']
computer_guess_table.field_names = ['Computer guesses','Feedback to computer']


def play_game():
    """this allows you to play the game. """
    game_icons = [welcome_image, game_logo]
    print(' '.join(game_icons))

    new_possible_pins = [list(p) for p in itertools.permutations(range(10), 4)]

    user_pin = gen_pin_or_guess('pin')
    computer_pin = generate_computer_pin(new_possible_pins)

    winner = 'computer'

    print(f'\n--------PLAYER PIN----------')
    print(f'Your PIN: {user_pin}')


    is_guessing = True
    while is_guessing:
        user_guesses = gen_pin_or_guess('guess')
        computer_guesses = generate_computer_guesses(new_possible_pins)

        print('\n')
        print('-------------------GUESSES----------------------------')
        print(f'user has guessed : {user_guesses}')
        print(f'computer is thinking......🧠🤔')
        time.sleep(1.5)
        print(f'computer has guessed : {computer_guesses}\n')

        print('-----------------------FEEDBACKS------------------------')
        # user tries to guess the computer's pin
        feed_back_to_user = compare_guesses(user_guesses, computer_pin)
        user_message = message_feedback(feed_back_to_user)

        dead_and_injured_table.add_row([f'{user_guesses}', f'{user_message}'])
        print(dead_and_injured_table)

        if feed_back_to_user['dead'] == 4 and feed_back_to_user['injured'] == 0:
            is_guessing = False
            winner = 'player'

        feed_back_to_computer, comp_message = computer_guessing_strategy(computer_guesses, user_pin, new_possible_pins)

        computer_guess_table.add_row([f'{computer_guesses}', f'{comp_message}'])
        print(computer_guess_table)

        if feed_back_to_computer['dead'] == 4 and feed_back_to_computer['injured'] == 0:
            is_guessing = False

        # computer tries to guess the player's pin as well with a random 4 digit guesses
        # computer compares his current guess with all possible combinations of the guess to
        # get the same feedback and narrow down what the user's pin might be

    dead_and_injured_table.clear_rows()
    computer_guess_table.clear_rows()

    print('\nTHE GAME HAS ENDED 🙂')
    print('-----------------------RESULTS----------------------')
    print(f'The winner is......{winner.title()}')
    print(f'Your PIN : {user_pin}')
    print(f'Computer PIN : {computer_pin}')

while input('Do you want to play a game of DEAD and INJURED? 😏: ').lower().strip().startswith('y'):
    play_game()
print('Goodbye 🤗')
