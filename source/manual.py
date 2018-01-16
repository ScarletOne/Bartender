def roll_description():
    roll_command = ' > Rzuć - rzucę daną liczbą kostek dziesięciościennych i policzę sukcesy\n'
    return roll_command


def help_description():
    help_command = ' > Pomusz - wyświetlę wszystkie moje komendy\n'
    return help_command


def change_success_description():
    change_success_command = ' > Sukcesy - zmienię od jakiej liczby będę liczył sukcesy następnego rzutu\n'
    return change_success_command


def show_help():
    text_manual = '```To wam mogę zaoferować: \n'
    text_manual += help_description()
    text_manual += roll_description()
    text_manual += change_success_description()
    text_manual += '```'
    return text_manual
