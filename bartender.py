import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import dice_roller
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
    if message_starts_with(message, 'sukcesy'):
        await client.send_message(message.channel, '```' + dice_roller.change_success_threshold(message))
    if message_starts_with(message, 'rzuc') or message_starts_with(message, 'rzuć'):
        print('Stół do rzucania kośćmi gotowy!')
        result = roller.roll_dice(message)
        await client.send_message(message.channel, result)
    if message_starts_with(message, 'powiedz'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
    if message_starts_with(message, 'pomusz'):
        await client.send_message(message.channel, manual.show_help())
    if message_starts_with(message, 'drama') or message_starts_with(message, 'drama!'):
        await client.send_message(message.channel, '```' + dice_roller.perform_drama_roll())
    if message_starts_with(message, 's!'):
        print('Nowy próg sukcesu')
        result = roller.change_success_threshold(message)
        await client.send_message(message.channel, result)


client.run("Mzg5NzYyMDM5MTc1OTcwODI2.DRARvQ.rYou-m3OjU5c6zvXd4_seyb5GUw")
