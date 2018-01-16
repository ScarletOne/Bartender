import discord
from discord.ext import commands
import client_id
import dice_roller
import manual
import threshold_manipulator
import character

Client = discord.Client()
client = commands.Bot(command_prefix="?")


@client.event
async def on_ready():
    print("Karczma otwarta!")


def unify_message(message):
    return message.content.lower()


def message_starts_with(message, starting_word):
    return unify_message(message).startswith(starting_word)


def validate_command(message):
    word_count = message.content.split(' ')
    if len(word_count) > 1:
        return True
    return False


def extract_content(message):
    args = message.content.split(" ")
    return args


def reset_roll_parameters(dice_roller_to_be_reset, threshold_manipulator_to_be_reset):
    dice_roller_to_be_reset.reset_dice_roller()
    threshold_manipulator_to_be_reset.reset_threshold()
    return '```Parametry rzutów zostały ustawione na domyślne```'


@client.event
async def on_message(message):
    roller = dice_roller.DiceRoller()
    manipulator = threshold_manipulator.ThresholdManipulator()
    char = character.Character()

    if message_starts_with(message, 'pomusz'):
        await client.send_message(message.channel, manual.show_help())
    if message_starts_with(message, 'reset'):
        await client.send_message(message.channel, reset_roll_parameters(roller, manipulator))
    if message_starts_with(message, 'sukcesy'):
        print('Nowy próg sukcesu')
        result = manipulator.change_success_threshold(extract_content(message))
        await client.send_message(message.channel, result)
    if message_starts_with(message, 'rzuc') or message_starts_with(message, 'rzuć'):
        print('Stół do rzucania kośćmi gotowy!')
        result = roller.roll_dice(extract_content(message))
        await client.send_message(message.channel, result)
    if message_starts_with(message, 'drama'):
        print('Używamy dramy!')
        result = roller.roll_drama()
        await client.send_message(message.channel, result)
    if message_starts_with(message, 'inicjatywa'):
        await client.send_message(message.channel, 'still under work')
    if message_starts_with(message, 'postac'):
        print('tymczasowo wyświetlam Lwa')
        await client.send_message(message.channel, char.display_character())

client.run(client_id.address)
