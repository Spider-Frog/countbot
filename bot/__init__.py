import discord
from .config import Config
import logging

client = discord.Client()

current_count = 0


@client.event
async def on_ready():
    logging.info(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    global current_count

    logging.debug(f"{message=}")
    logging.debug(f"{message.channel=}")

    channel_name = message.channel.name

    # Check if the channel is count-decimal channel.
    if channel_name == 'count-decimal':
        try:
            if int(message.content) == current_count + 1:
                await message.add_reaction('✅')
                current_count += 1
            else:
                await message.add_reaction('❌')
                await message.channel.send("Wrong numba bitch!")
                current_count = 0
        except ValueError:
            pass

client.run(Config.token)
