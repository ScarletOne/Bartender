'''import math'''


class Character:
    nickname = 'Lew'
    name = 'Karl Gustav Gustavsson \"Szkarłatny Lew\"'
    race = 'Człowiek'
    social_status = 'Dowódca najemników'
    drama = 2
    motivations = {
        'Moi ludzie, moja rodzina, moja kompania to jest wszystko co cenię i kocham i chcę tego bronić. Aż po grób': 3,
        'Przeszedłem tak dużo, nie ważne co zostanie rzucone przeciwko mnie, stawię temu czoła': 2,
        'Nawet w najgorszych sytuacjach można dostrzec światło, nawet najgorszych zbirów można nawrócić, trzeba im tylko pokazać jakim przykładem się jest': 2
    }
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

    '''Skill name: (ranks: threshold)'''
    skills = {
        'Miecze': 11,
        'Broń drzewcowa': 10,
        'Obuchy': 10,
        'Kusze': 7,
        'Walka wręcz': 11,
        'Hart': 12,
        'Blef': 4,
        'Perswazja': 6,
        'Zastraszanie': 7,
        'Przeczucie': 9,
        'Zbieranie informacji': 4,
        'Bieganie': 6,
        'Jeździectwo': 4,
        'Percepcja': 8,
        'Pływanie': 5,
        'Równowaga': 6,
        'Skakanie': 5,
        'Wspinaczka': 5,
        'Dowodzenie': 12,
        'Nawigacja': 2,
        'Pierwsza pomoc': 7,
        'Podnoszenie': 6,
        'Zwierzęca empatia': 4,
        'Sztuka przetrwania': 3,
        'Odnajdywanie ścieżek': 4
    }

    languages = {
        'Thuleański': 6,
        'Cymryjski': 3,
        'Conariański': 4,
        'Giganci': 2,
        'Ośmiogrodzki': 5,
        'Lamarski': 5,
        'Orczy': 3
    }

    knowledge = {
        'Legendy': 4,
        'Potwory': 2,
        'Półświatek': 2,
        'Wojenna': 6,
        'Etykieta': 5
    }

    @staticmethod
    def __display_dict(dict_to_be_displayed):
        display_friendly_dict = ''
        for member in dict_to_be_displayed:
            display_friendly_dict += member + ": " + str(dict_to_be_displayed[member]) + '\n'
        return display_friendly_dict

    @staticmethod
    def __display_array(array_to_be_displayed):
        display_friendly_array = ''
        for member in array_to_be_displayed:
            display_friendly_array += member + '\n'
        return display_friendly_array

    def display_character(self):
        character = '```' + self.name + '```\n'
        character += '```Rasa: ' + self.race + '\nStatus społeczny: ' + self.social_status + '\n```'
        character += self.__display_motivations()
        character += self.__display_attributes()
        character += self.__display_adv_attributes()
        character += self.__display_thresholds()
        character += self.__display_traits()
        character += self.__display_skills()
        character += self.__display_languages()
        character += self.__display_knowledge()
        return character

    def __display_attributes(self):
        attr = '```ATRYBUTY:\n'
        attr += self.__display_dict(self.attributes)
        attr += '```'
        return attr

    def __display_adv_attributes(self):
        attr = '```DODATKOWE ATRYBUTY:\n'
        attr += self.__display_dict(self.advanced_attributes)
        attr += '```'
        return attr

    def __display_thresholds(self):
        attr = '```PROGI:\n'
        attr += self.__display_dict(self.thresholds)
        attr += '```'
        return attr

    def __display_traits(self):
        attr = '```CECHY:\n'
        attr += self.__display_array(self.traits)
        attr += '```'
        return attr

    def __display_skills(self):
        attr = '```UMIEJĘTNOŚCI:\n'
        attr += self.__display_dict(self.skills)
        attr += '```'
        return attr

    def __display_languages(self):
        attr = '```JĘZYKI:\n'
        attr += self.__display_dict(self.languages)
        attr += '```'
        return attr

    def __display_knowledge(self):
        attr = '```WIEDZA:\n'
        attr += self.__display_dict(self.knowledge)
        attr += '```'
        return attr

    def __display_motivations(self):
        attr = '```MOTYWACJE:\n'
        attr += self.__display_dict(self.motivations)
        attr += '```'
        return attr

