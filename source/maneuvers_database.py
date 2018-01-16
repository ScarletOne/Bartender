import gspread
from oauth2client.service_account import ServiceAccountCredentials
import maneuver

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('google_api_secret.json', scope)
client = gspread.authorize(credentials)

spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1gPD1QgHUE2mw0XSVdk7B_ZF5I-B66zYbnpdWiaNNpTA/edit#gid=0')
worksheet = spreadsheet.sheet1

maneuvers = []


def get_all_basic_offensive_maneuvers():
    basic_offensive = []
    list_of_basic_offensive_cells = worksheet.findall("Ofensywne podstawowe")
    for member in list_of_basic_offensive_cells:
        row = member.row
        row_value = worksheet.row_values(row)[:4]
        basic_offensive.append(maneuver.Maneuver(row_value[:4]))
    return basic_offensive


basic_offensive_maneuvers = get_all_basic_offensive_maneuvers()


def display_all_basic_offensive():
    global basic_offensive_maneuvers
    out = 'OFENSYWNE PODSTAWOWE\n'
    for member in basic_offensive_maneuvers[:10]:
        out += member.display_maneuver() + '\n'
    return out


def display_maneuvers():
    maneuvers_data = '```MANEWRY\n'
    maneuvers_data += display_all_basic_offensive()
    maneuvers_data += '```'
    return maneuvers_data
