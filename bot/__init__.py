import discord
from .config import Config
import logging
from .numeral_system import *

# Init the Discord bot.
client = discord.Client()

counts = []


@client.event
async def on_ready():
    logging.info(f"{client.user} has connected to Discord!")

    channels = client.get_all_channels()

    # Check the servers for the right channels.
    for channel in channels:
        if channel.name == 'count-decimal':
            counts.append(DecimalCount())
        if channel.name == 'count-binary':
            counts.append(BinaryCount())
        if channel.name == 'count-hex':
            counts.append(HexCount())


@client.event
async def on_message(message):
    logging.info(f"{message.author} said '{message.content}' in channel '{message.channel.name}'.")

    channel_name = message.channel.name

    # Check channel to determine which numeral system to use.
    for count in counts:
        if channel_name == count.channel_name:
            try:
                # Try to convert the number to int. to compare it with the current number
                number = count.convert_to_int(message.content)

                # Compare the given number by the user to the current right answer.
                if number == count.current + 1:
                    # Add an checkmark as reaction to the users answer.
                    await message.add_reaction(Config.Reaction.correct)

                    # Increment the current count by 1
                    count.current += 1
                else:
                    # Add an cross as reaction to the users answer.
                    await message.add_reaction(Config.Reaction.wrong)

                    # Send an message to inform the user the input was wrong.
                    await message.channel.send(Config.Reaction.wrong_message.format(
                        user=message.author.mention,
                        number=count.get_current())
                    )

                    # Reset current count to 0.
                    count.current = 0
            except ValueError:
                # Skip if no value could not be converted, like if it's just regular text.
                pass

# Run the Discord bot
client.run(Config.token)
