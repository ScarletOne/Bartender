def say_description():
    say_command = ' > Powiedz - powtórzę słowa, które chcesz \n'
    return say_command


def roll_description():
    roll_command = ' > Rzuć - rzucę daną liczbą kostek dziesięciościennych i policzę sukcesy\n'
    return roll_command


def help_description():
    help_command = ' > Pomusz - wyświetlę wszystkie moje komendy\n'
    return help_command


def show_help():
    text_manual = '```To wam mogę zaoferować: \n'
    text_manual += help_description()
    text_manual += say_description()
    text_manual += roll_description()
    text_manual += '```'
    return text_manual
