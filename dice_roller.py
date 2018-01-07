import random
import gif_database


class DiceRoller:

    def __init__(self, given_success_threshold):
        self.success_threshold = given_success_threshold
        self.results = [0]

        self.dice_number = 0

        self.successes = 0
        self.failures = 0

        self.tens = 0
        self.critical_failures = 0

        self.glitch = False

    # Dice Rolling
    def roll_dice(self, message):
        self.__prepare_dice(message)
        self.__roll_multiple_times(self.dice_number)
        self.__evaluate_roll_output()
        self.__check_glitch()
        return self.__output_roll_result()

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