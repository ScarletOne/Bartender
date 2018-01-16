'''https://github.com/burnash/gspread'''

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import maneuver

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('google_api_secret.json', scope)
client = gspread.authorize(credentials)

spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1gPD1QgHUE2mw0XSVdk7B_ZF5I-B66zYbnpdWiaNNpTA/edit#gid=0')
worksheet = spreadsheet.sheet1


def get_group_of_mnvrs(group_name):
    manvr_group = []
    list_of_found_cells = worksheet.findall(group_name)
    for member in list_of_found_cells:
        row = member.row
        row_value = worksheet.row_values(row)[:3]
        manvr_group.append(maneuver.Maneuver(row_value[:3]))
    return manvr_group


mnvrs = {
    "Ofensywne podstawowe": get_group_of_mnvrs("Ofensywne podstawowe"),
    "Defensywne podstawowe": get_group_of_mnvrs("Defensywne podstawowe"),
    "Ofensywne zwarcia": get_group_of_mnvrs("Ofensywne zwarcia")
}


def display_mnvr_group(group_name):
    global basic_offensive_mnvrs
    out = group_name.upper() + '\n'
    for member in mnvrs[group_name]:
        out += member.display_maneuver() + '\n'
    return out


def display_maneuvers():
    maneuvers_data = '```MANEWRY\n'
    maneuvers_data += display_mnvr_group("Ofensywne podstawowe")
    maneuvers_data += display_mnvr_group("Defensywne podstawowe")
    maneuvers_data += display_mnvr_group("Ofensywne zwarcia")
    maneuvers_data += '\n\n\n By dowiedzieć się więcej o manewrach, zapraszam pod link:```\n'
    maneuvers_data += 'https://docs.google.com/document/d/1sR8H4HYvnnyZBR62bA01LUCrgI2Nzu0aaYwck834xlA/edit?usp=sharing'
    return maneuvers_data
