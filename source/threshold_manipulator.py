import roll_parameters


class ThresholdManipulator:
    def __init__(self):
        self.new_threshold = 7

    def reset_threshold(self):
        self.new_threshold = 7
        self.__export_threshold()

    def change_success_threshold(self, threshold):
        previous_threshold = self.new_threshold
        self.__prepare_threshold(threshold)
        if self.new_threshold < 1 or self.new_threshold > 10:
            self.new_threshold = previous_threshold
            return self.__throw_invalid_threshold()
        self.__export_threshold()
        return self.__threshold_changed()

    def __prepare_threshold(self, new_threshold):
        self.new_threshold = int(new_threshold[1])

    def __export_threshold(self):
        roll_parameters.roll_parameters['success_threshold'] = self.new_threshold

    @staticmethod
    def __throw_invalid_threshold():
        return '```Porżnęło Cię? Nic nie zmieniam Ty chory pojebie ```'

    def __threshold_changed(self):
        return '```Próg sukcesu został zmieniony na ' + str(self.new_threshold) + '```'
