from dead_and_injured_module import (gen_pin_or_guess,
                                     generate_computer_pin, generate_computer_guesses,
                                     compare_guesses, narrow_down_guess, message_feedback)

from prettytable import PrettyTable
from arts import game_logo, welcome_image
import time
dead_and_injured_table = PrettyTable()
dead_and_injured_table.field_names = ['User guesses', 'Feedback to user']
def play_game():
    game_icons = [welcome_image, game_logo]
    print(' '.join(game_icons))

    user_pin = gen_pin_or_guess('pin')
    computer_pin = generate_computer_pin()

    winner = 'computer'

    print(f'\n--------PLAYER PIN----------')
    print(f'Your PIN: {user_pin}')
    print(f'computer: {computer_pin}')

    Start_Game = True
    while Start_Game:
        user_guesses = gen_pin_or_guess('guess')
        computer_guesses = generate_computer_guesses()

        print('\n')
        print('-------------------GUESSES----------------------------')
        print(f'user has guessed : {user_guesses}')
        print(f'computer is thinking......🧠🤔')
        time.sleep(1.5)
        print(f'computer has guessed : {computer_guesses}\n')

        print('-----------------------FEEDBACKS------------------------')
        # user tries to guess the computer's pin
        feed_back_to_user = compare_guesses(user_guesses, computer_pin)
        message = message_feedback(feed_back_to_user, "player")

        dead_and_injured_table.add_row([f'{user_guesses}', f'{message}'])
        print(dead_and_injured_table)

        if feed_back_to_user['dead'] == 4 and feed_back_to_user['injured'] == 0:
            Start_Game = False
            winner = 'player'

        computer_bool = narrow_down_guess(computer_guesses, user_pin)
        if computer_bool:
              Start_Game = False

        # computer tries to guess the player's pin as well with a random 4 digit guesses
        # computer compares his current guess with all possible combinations of the guess to
        # get the same feedback and narrow down what the user's pin might be

    print('\nTHE GAME HAS ENDED 🙂')
    print('-----------------------RESULTS----------------------')
    print(f'The winner is......{winner.title()}')
    print(f'Your PIN : {user_pin}')
    print(f'Computer PIN : {computer_pin}')

while input('Do you want to play a game of DEAD and INJURED? 😏: ').lower().strip().startswith('y'):
    play_game()
print('Goodbye 🤗')
