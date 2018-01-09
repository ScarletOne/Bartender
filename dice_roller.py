import random
import gif_database
import roll_parameters


class DiceRoller:

    def __init__(self):
        self.success_threshold = roll_parameters.roll_parameters['success_threshold']
        self.successes = 0
        self.failures = 0
        self.tens = 0

    # Dice Rolling
    def roll_dice(self, message):
        dice_number = self.__prepare_dice(message)
        results = self.__roll_multiple_times(dice_number)
        self.__evaluate_roll_output(results)
        self.__glitch_exists(dice_number, results)
        self.__export_roll_parameters()
        return self.__output_roll_result(dice_number, results)

    @staticmethod
    def __prepare_dice(message):
        args = message.content.split(" ")
        dice_number = 0
        if len(args) > 1 and args[1].isdigit():
            dice_number = int(args[1])
        return dice_number

    @staticmethod
    def __roll_10s():
        return random.randrange(1, 11)

    def __roll_multiple_times(self, dice_number):
        results = [0] * dice_number
        for i in range(dice_number):
            results[i] = self.__roll_10s()
        return results

    def __evaluate_roll_output(self, results):
        for i in range(len(results)):
            if results[i] >= self.success_threshold:
                self.successes += 1
                if results[i] is 10:
                    self.tens += 1
            else:
                self.failures += 1

    @staticmethod
    def __count_critical_failures(results):
        critical_failures = 0
        for i in range(len(results)):
            if results[i] is 1:
                critical_failures +=1
        return critical_failures

    def __glitch_exists(self, dice_number, results):
        return self.__count_critical_failures(results) >= dice_number / 2

    def __output_roll_result(self, dice_number, results):
        result = '```'
        result += 'Rzuciłem ' + str(dice_number) + ' kośćmi\n'
        result += 'Sukcesy rzutu liczyłem od ' + str(self.success_threshold) + '\n'
        result += 'Wyniki rzutu:\n' + str(results[0:]) + '\n'
        result += 'Liczba sukcesów: ' + str(self.successes) + '\n'
        if self.__glitch_exists(dice_number, results):
            result += 'Zgrzyt! ```\n'
            result += gif_database.random_fail()
        else:
            result += '```'
        return result

    def __export_roll_parameters(self):
        roll_parameters.roll_parameters['successes'] = self.successes
        roll_parameters.roll_parameters['failures'] = self.failures
        roll_parameters.roll_parameters['tens'] = self.tens
