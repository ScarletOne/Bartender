import random
import gif_database


class DiceRoller:
    results = [0]
    success_threshold = 7

    dice_number = 0

    successes = 0
    failures = 0

    tens = 0
    critical_failures = 0

    glitch = False

    def roll_dice(self, message):
        self.__init__()
        self.__prepare_dice(message)
        self.__roll_multiple_times(self.dice_number)
        self.__evaluate_roll_output()
        self.__check_glitch()
        return self.__output_roll_result()

#Dice Rolling
    def __prepare_dice(self, message):
        args = message.content.split(" ")
        if len(args) > 1 and args[1].isdigit():
            self.dice_number = int(args[1])

    @staticmethod
    def __roll_10s():
        return random.randrange(1, 11)

    def __roll_multiple_times(self, number_of_times):
        self.results = [0] * number_of_times
        for i in range(number_of_times):
            self.results[i] = self.__roll_10s()

    def __evaluate_roll_output(self):
        for i in range(len(self.results)):
            if self.results[i] >= self.success_threshold:
                self.successes += 1
                if self.results[i] is 10:
                    self.tens += 1
            else:
                self.failures += 1
                if self.results[i] is 1:
                    self.critical_failures += 1

    def __check_glitch(self):
        self.glitch = self.critical_failures >= self.dice_number / 2

    def __output_roll_result(self):
        result = '```'
        result += 'Rzuciłem ' + str(self.dice_number) + ' kośćmi\n'
        result += 'Sukcesy rzutu liczyłem od ' + str(self.success_threshold) + '\n'
        result += 'Wyniki rzutu:\n' + str(self.results[0:]) + '\n'
        result += 'Liczba sukcesów: ' + str(self.successes) + '\n'
        if self.glitch:
            result += 'Zgrzyt!\n'
        result += '```'
        if self.glitch:
            result += gif_database.random_fail()
        return result







success_threshold = 7
number_of_potential_rerolls = 0


def set_success_threshold_to(new_success_threshold):
    global success_threshold
    success_threshold = new_success_threshold


def reset_success_threshold():
    set_success_threshold_to(7)


def change_success_threshold(message):
    args = message.content.split(" ")
    new_threshold = int(args[1])
    if new_threshold < 1 or new_threshold > 10:
        return 'Porżnęło Cię? Nic nie zmieniam Ty chory pojebie ```'
    set_success_threshold_to(new_threshold)
    return 'W następnym rzucie będę miał sukcesy od ' + str(success_threshold) + '```'


def roll_dice():
    return random.randrange(1, 11)


def roll_given_number_of_times(number_of_times):
    args = [0] * number_of_times
    for i in range(number_of_times):
        args[i] = roll_dice()
    return args


def count_successes(roll_output):
    global number_of_potential_rerolls
    number_of_successes = 0
    for i in range(len(roll_output)):
        if roll_output[i] >= success_threshold:
            number_of_successes += 1
            if roll_output[i] == 10:
                number_of_potential_rerolls += 1
    return number_of_successes


def count_failures(roll_output):
    number_of_failures = 0
    for i in range(len(roll_output)):
        if roll_output[i] == 1:
            number_of_failures += 1
    return number_of_failures


def check_if_glitch_occurred(number_of_failures, number_of_dice_rolled):
    return number_of_failures >= (number_of_dice_rolled/2)


def perform_roll(number_of_dice):
    if number_of_dice <= 0:
        return 'To ile kostek mam rzucić? ```'

    rolled = roll_given_number_of_times(number_of_dice)
    successes = count_successes(rolled)
    failures = count_failures(rolled)
    glitch = check_if_glitch_occurred(failures, len(rolled))

    message_array = 'Rzucam ' + str(len(rolled)) + ' kostkami z sukcesami od ' + str(
        success_threshold) + '\noto wyniki rzutu: \n' + str(rolled[0:]) + '\n liczba sukcesów: ' + str(successes)
    if glitch:
        glitch_message = '\nliczba jedynek: ' + str(failures) + '\nZgrzyt!'
        message_array += glitch_message
    if successes == 0:
        message_array += '``` ' + gif_database.random_fail() + ' ``` Coś nie wyszło...'
    if successes == len(rolled):
        message_array += '``` ' + gif_database.random_win() + ' ``` Wow!'
    return_message = message_array + '```'
    reset_success_threshold()
    return return_message


def perform_standard_roll(message):
    args = message.content.split(" ")
    if len(args) > 1 and args[1].isdigit():
        number_of_dice = int(args[1])
        return perform_roll(number_of_dice)
    return 'Czekaj, ile tych kostek mam rzucić?```'


def perform_drama_roll():
    global number_of_potential_rerolls
    rerolls = number_of_potential_rerolls
    number_of_potential_rerolls = 0
    return "Drama! Przerzucam dziesiątki! \n" + perform_roll(rerolls)
