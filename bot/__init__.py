import discord
from .config import Config
import logging
from .numeral_system import *

client = discord.Client()

counts = []


@client.event
async def on_ready():
    logging.info(f"{client.user} has connected to Discord!")

    channels = client.get_all_channels()

    for channel in channels:
        if 'count-decimal' == channel.name:
            counts.append(DecimalCount())
        if 'count-binary' == channel.name:
            counts.append(BinaryCount())
        if 'count-hex' == channel.name:
            counts.append(HexCount())


@client.event
async def on_message(message):
    logging.info(f"{message.author} said '{message.content}' in channel '{message.channel.name}'.")

    channel_name = message.channel.name

    # Check if the channel is numeral_system-decimal channel.
    for count in counts:
        if channel_name == count.channel_name:
            try:
                number = count.convert_to_int(message.content)

                if number == count.current + 1:
                    await message.add_reaction(Config.Reaction.correct)
                    count.current += 1
                else:
                    await message.add_reaction(Config.Reaction.wrong)
                    await message.channel.send(Config.Reaction.wrong_message.format(user=message.author.mention, number=count.get_current()))
                    count.current = 0
            except ValueError:
                pass

client.run(Config.token)
