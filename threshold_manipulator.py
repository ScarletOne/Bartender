import roll_parameters


class ThresholdManipulator:
    def __init__(self):
        self.new_threshold = 7

    def change_success_threshold(self, message):
        self.__prepare_threshold(message)
        if self.new_threshold < 1 or self.new_threshold > 10:
            return self.__throw_invalid_threshold()
        roll_parameters.roll_parameters['success_threshold'] = self.new_threshold
        return self.__threshold_changed()

    def __prepare_threshold(self, message):
        args = message.content.split(" ")
        self.new_threshold = int(args[1])

    @staticmethod
    def __throw_invalid_threshold():
        return '```Porżnęło Cię? Nic nie zmieniam Ty chory pojebie ```'

    def __threshold_changed(self):
        return '```Próg sukcesu został zmieniony na ' + str(self.new_threshold) + '```'
