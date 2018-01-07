import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import dice_roller
import threshold_manipulator
import manual

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


@client.event
async def on_message(message):
    roller = dice_roller.DiceRoller()
    manipulator = threshold_manipulator.ThresholdManipulator()

    if message_starts_with(message, 'sukcesy'):
        print('Nowy próg sukcesu')
        result = manipulator.change_success_threshold(message)
        await client.send_message(message.channel, result)
    if message_starts_with(message, 'rzuc') or message_starts_with(message, 'rzuć'):
        print('Stół do rzucania kośćmi gotowy!')
        result = roller.roll_dice(message)
        await client.send_message(message.channel, result)
    if message_starts_with(message, 'powiedz'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
    if message_starts_with(message, 'pomusz'):
        await client.send_message(message.channel, manual.show_help())

