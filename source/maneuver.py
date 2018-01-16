class Maneuver:
    maneuver_type = 'Typ manewru'
    name = 'Nazwa manewru'
    cost = 'Koszt manewru'
    description = 'Opis manewru'

    def __init__(self, sheet_value):
        self.maneuver_type = str(sheet_value[0])
        self.name = str(sheet_value[1])
        self.cost = str(sheet_value[2])
        self.description = str(sheet_value[3])

    def display_maneuver(self):
        print('displaying ' + self.name)
        info = '\t>' + self.name + '(' + self.cost + ')'
        return info

    def display_detailed_info(self):
        info = self.display_maneuver()
        info += ' - ' + self.description
        return info