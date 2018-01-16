def roll_description():
    roll_command = ' > Rzuć - rzucę daną liczbą kostek dziesięciościennych i policzę sukcesy\n'
    return roll_command


def drama_description():
    drama_command = ' > Drama - przerzucę ostatni rzut według zasad Dramy w systemie Ostrza\n'
    return drama_command


def help_description():
    help_command = ' > Podręcznik - wyświetlę wszystkie moje komendy\n'
    return help_command


def change_success_description():
    change_success_command = ' > Sukcesy - zmienię od jakiej liczby będę liczył sukcesy następnego rzutu\n'
    return change_success_command


def maneuvers_database():
    maneuvers_command = ' > Manewry - wyświetla listę manewrów z kosztami\n'
    return maneuvers_command


def show_help():
    text_manual = '```To wam mogę zaoferować: \n'
    text_manual += help_description()
    text_manual += change_success_description()
    text_manual += roll_description()
    text_manual += drama_description()
    text_manual += maneuvers_database()
    text_manual += '```'
    return text_manual
