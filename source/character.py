class Character:
    name = ''
    attributes = {
        'Siła': 0,
        'Zwinność': 0,
        'Wytrzymałość': 0,
        'Wola': 0,
        'Intuicja': 0,
        'Mądrość': 0,
        'Charyzma': 0
    }

    def display_character(self):
        character = self.name + '\n'
        character += self.display_attributes()
        return character

    def display_attributes(self):
        attr = '```'
        attr += 'Siła: ' + str(self.attributes['Siła']) + '\n'
        attr += 'Zwinność: ' + str(self.attributes['Zwinność']) + '\n'
        attr += 'Wytrzymałość: ' + str(self.attributes['Wytrzymałość']) + '\n'
        attr += 'Wola: ' + str(self.attributes['Wola']) + '\n'
        attr += 'Intuicja: ' + str(self.attributes['Intuicja']) + '\n'
        attr += 'Mądrość: ' + str(self.attributes['Mądrość']) + '\n'
        attr += 'Charyzma: ' + str(self.attributes['Charyzma']) + '\n'
        attr += '```'
        return attr
