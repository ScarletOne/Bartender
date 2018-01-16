import random
import gif_database
import roll_parameters


class DiceRoller:

    def __init__(self):
        self.success_threshold = roll_parameters.roll_parameters['success_threshold']
        self.successes = 0
        self.failures = 0
        self.tens = 0
        self.results = [(0, [0])]

    def reset_dice_roller(self):
        self.successes = 0
        self.failures = 0
        self.tens = 0
        self.results = [(0, [0])]
        self.__export_roll_parameters()

    # Dice Rolling
    def roll_dice(self, requested_number_of_dice):
        dice_number = self.__prepare_dice(requested_number_of_dice)
        results = self.__roll_multiple_times(dice_number)
        self.__evaluate_roll_output(results)
        self.__glitch_exists(dice_number, results)

        self.results = [(dice_number, results)]
        self.__export_roll_parameters()
        return self.__output_roll_result(dice_number, results)

    def roll_drama(self):
        dice_number = roll_parameters.roll_parameters['tens'] + roll_parameters.roll_parameters['failures']
        successes = roll_parameters.roll_parameters['successes']
        self.results = roll_parameters.roll_parameters['results']
        self.reset_dice_roller()
        while dice_number > 0:
            results = self.__roll_multiple_times(dice_number)
            self.__evaluate_roll_output(results)
            self.results.append((dice_number, results))
            successes += self.successes
            dice_number = self.tens
            self.__export_roll_parameters()
            self.tens = 0
            self.successes = 0
        return self.__output_drama_result(successes)

    def __output_drama_result(self, successes):
        result = '```'
        result += 'Użyto dramy na poprzednim rzucie!\n'
        result += 'Rzucono ' + str(len(self.results)-1) + ' razy!\n'
        result += 'Oto wyniki rzutów: \n'
        result += self.__display_drama_results()
        result += 'Sumaryczna liczba sukcesów wszystkich rzutów: ' + str(successes) + '\n'
        result += '```'
        return result

    def __display_drama_results(self):
        self.results.pop(0)
        output = ''
        roll_count = 1
        for roll in self.results:
            output += 'Rzut ' + str(roll_count) + ' dramy:\n'
            output += '\tRzucono ' + str(roll[0]) + ' kości\n'
            output += '\tOto wyniki rzutów: \n\t' + str(roll[1][0:]) + '\n'
        return output

    @staticmethod
    def __prepare_dice(requested_number_of_dice):
        dice_number = 0
        if len(requested_number_of_dice) > 1 and requested_number_of_dice[1].isdigit():
            dice_number = int(requested_number_of_dice[1])
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
                critical_failures += 1
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
        roll_parameters.roll_parameters['results'] = self.results
