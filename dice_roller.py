import random
import gif_database

success_threshold = 7


def set_success_threshold_to(new_success_threshold):
    global success_threshold
    success_threshold = new_success_threshold


def reset_success_threshold():
    set_success_threshold_to(7)


def change_success_threshold(message):
    args = message.content.split(" ")
    new_threshold = int(args[1])
    if new_threshold < 1 or new_threshold > 10:
        return '``` Porżnęło Cię? Nic nie zmieniam Ty chory pojebie ```'
    set_success_threshold_to(new_threshold)
    return '```W następnym rzucie będę miał sukcesy od ' + str(success_threshold) + '```'


def roll_dice():
    return random.randrange(1, 10)


def roll_given_number_of_times(number_of_times):
    args = [0] * int(number_of_times)
    for i in range(int(number_of_times)):
        args[i] = roll_dice()
    return args


def count_successes(roll_output):
    number_of_successes = 0
    for i in range(len(roll_output)):
        if roll_output[i] >= success_threshold:
            number_of_successes += 1
    return number_of_successes


def count_failures(roll_output):
    number_of_failures = 0
    for i in range(len(roll_output)):
        if roll_output[i] == 1:
            number_of_failures += 1
    return number_of_failures


def check_if_glitch_occurred(number_of_failures, number_of_dice_rolled):
    return number_of_failures >= (number_of_dice_rolled/2)


def perform_roll(message):
    args = message.content.split(" ")
    rolled = roll_given_number_of_times(args[1])
    successes = count_successes(rolled)
    failures = count_failures(rolled)
    glitch = check_if_glitch_occurred(failures, len(rolled))

    message_array = 'Rzucam ' + str(len(rolled)) + ' kostkami z sukcesami od ' + str(success_threshold) +  '\noto wyniki rzutu: \n' + str(rolled[0:]) + '\n liczba sukcesów: ' + str(successes)
    if glitch:
        glitch_message = '\nliczba jedynek: ' + str(failures) + '\nZgrzyt!'
        message_array += glitch_message
    if successes == 0:
        message_array += '``` ' + gif_database.random_fail() + ' ``` Coś nie wyszło...'
    if successes == len(rolled):
        message_array += '``` ' + gif_database.random_win() + ' ``` Wow!'
    return_message = '```' + message_array + '```'
    reset_success_threshold()
    return return_message
