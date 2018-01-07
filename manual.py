def say_description():
    say_command = ' > Powiedz - powtórzę słowa, które chcesz \n'
    return say_command


def roll_description():
    roll_command = ' > Rzuć - rzucę daną liczbą kostek dziesięciościennych i policzę sukcesy\n'
    return roll_command


def help_description():
    help_command = ' > Pomusz - wyświetlę wszystkie moje komendy\n'
    return help_command


def change_success_description():
    change_success_command = ' > Sukcesy - zmienię od jakiej liczby będę liczył sukcesy następnego rzutu\n'
    return change_success_command

def reactive_drama_description():
    reactive_drama_command = ' > Drama - przerzucę wszystkie dziesiątki i wszystkie kostki, na których nie wypadł sukces z ostatniego rzutu'
    return reactive_drama_command


def show_help():
    text_manual = '```To wam mogę zaoferować: \n'
    text_manual += help_description()
    text_manual += say_description()
    text_manual += roll_description()
    text_manual += change_success_description()
    text_manual += reactive_drama_description()
    text_manual += '```'
    return text_manual
