import math


class Character:
    name = 'Karl Gustaf Gustafsson \"Szkarłatny Lew\"'
    attributes = {
        'Siła': 5,
        'Zwinność': 4,
        'Wytrzymałość': 5,
        'Wola': 6,
        'Intuicja': 5,
        'Mądrość': 4,
        'Charyzma': 5
    }
    advanced_attributes = {
        'Refleks': 5,
        'Potencjał': 0,
        'Mana': 0,
        'Szybkość': 4
    }

    thresholds = {
        'Bólu': 12,
        'Zmęczenia': 25,
        'Masa ekwipunku': 18
    }

    traits = [
        'Naturalny przywódca',
        'Nieustępliwy',
        'Nieustraszony',
        'Niezłomny',
        'Szósty zmysł',
        'Żelazna wola',
        'Jednooki'
    ]

    def display_character(self):
        character = '```' + self.name + '```\n'
        character += self.__display_attributes()
        character += self.__display_adv_attributes()
        return character

    def __display_attributes(self):
        attr = '```ATRYBUTY:\n'
        attr += 'Siła: ' + str(self.attributes['Siła']) + '\n'
        attr += 'Zwinność: ' + str(self.attributes['Zwinność']) + '\n'
        attr += 'Wytrzymałość: ' + str(self.attributes['Wytrzymałość']) + '\n'
        attr += 'Wola: ' + str(self.attributes['Wola']) + '\n'
        attr += 'Intuicja: ' + str(self.attributes['Intuicja']) + '\n'
        attr += 'Mądrość: ' + str(self.attributes['Mądrość']) + '\n'
        attr += 'Charyzma: ' + str(self.attributes['Charyzma']) + '\n'
        attr += '```'
        return attr

    def __display_adv_attributes(self):
        attr = '```DODATKOWE ATRYBUTY:\n'
        attr += 'Refleks: ' + str(self.advanced_attributes['Refleks']) + '\n'
        if self.advanced_attributes['Potencjał'] > 0:
            attr += 'Potencjał: ' + str(self.advanced_attributes['Potencjał']) + '\n'
            attr += 'Mana: ' + str(self.advanced_attributes['Mana']) + '\n'
        attr += 'Szybkość: ' + str(self.advanced_attributes['Szybkość']) + '\n'
        attr += '```'
        return attr
