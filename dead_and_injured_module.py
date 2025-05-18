import random
import itertools
from prettytable import PrettyTable

computer_guess_table = PrettyTable()
computer_guess_table.field_names = ['Computer guesses','Feedback to computer']

new_possible_pins = [list(p) for p in itertools.permutations(range(10), 4)]
def gen_pin_or_guess(response):
    print('\n')
    pin_or_guess = []
    for i in range(4):
        while True:
            try:
                user_choice = int(input(f'Enter the {response} number{i + 1} from (0 - 9): '))
                if user_choice not in pin_or_guess and user_choice in range(0, 10):
                    pin_or_guess.append(user_choice)
                    break
                else:
                    print(f'That number has either already been entered! or may not be within the range of 0 - 9!')
            except ValueError:
                print('That is not a number')
    return pin_or_guess


def generate_computer_pin():
    comp_pin = random.choice(new_possible_pins)
    return comp_pin


def generate_computer_guesses():
    if random.random() < 0.3:
        comp_guesses = random.sample(range(10), k=4)
    else:
        comp_guesses = random.choice(new_possible_pins)
    return comp_guesses


# User tries to guess the computer pin with his 4 guesses
# loop through all the user's guess and loop through the computer's pin
# when a number in the user's guess is in the same position as a number in the computer's pin, it counts as a dead
# when a number in the user's guess is in the computer's pin but at the correct index , it counts as an injured

def compare_guesses(guesses, pin):
    dead = 0
    inj = 0

    for i in range(len(guesses)):
        for j in range(len(pin)):
            if guesses[i] == pin[j] and i == j:
                dead += 1
            elif guesses[i] in pin and i != pin.index(guesses[i]):
                inj += 1
                break
    return {"dead": dead, 'injured': inj}

def message_feedback(game_feed_back,current_player):

    if game_feed_back['dead'] == 4 and game_feed_back['injured'] == 0:
        return f' All dead'

    elif game_feed_back['dead'] == 0 and game_feed_back['injured'] == 0:
        return f'None is dead'
    else:
        return f"{game_feed_back['dead']}dead and {game_feed_back['injured']}injured."




# computer's strategy for guessing the user's pin
# the computer will generate all the possible combinations from a list of allowed guess range 0 - 9
# the computer will check his guess against the user's pin and compare the feedback with all the
# possible combinations in the list of possibilities to try and narrow down what the combinations
# that will produce the same result
# the computer will then move those combinations to a new list and then replace the old combination
# -list with a copy of the new possibilities list and clear the new list
# When you generate the list of all possible combination, then you compare each combination with the computer's
# current guess to try to reproduce the output it got as feedback from the user.


def narrow_down_guess(comp_curr_guess, user_pin):
    guess_logically = False
    feedback_to_computer = compare_guesses(comp_curr_guess, user_pin)
    message = message_feedback(feedback_to_computer, 'computer')
    if not guess_logically:

        global new_possible_pins
        new_possibilities = []

        for pin in new_possible_pins:
            pin_feed_back = compare_guesses(comp_curr_guess, pin)
            if pin_feed_back['dead'] == feedback_to_computer['dead'] and pin_feed_back["injured"] == feedback_to_computer['injured']:
                new_possibilities.append(pin)

        new_possible_pins[:] = new_possibilities

    computer_guess_table.add_row([f'{comp_curr_guess}', f'{message}'])
    print(computer_guess_table)

    if feedback_to_computer['dead'] == 4 and feedback_to_computer['injured'] == 0:
        return True
    return False


