import sys
import discord

CLIENT = discord.Client()

TOKEN = sys.argv[1]

@CLIENT.event
async def on_ready():
    """
    Bot is ready
    """
    print("Ready")

@CLIENT.event
async def on_message(message):
    """
    Adds a gay pride flag as a reaction if a message contains "gay"
    """
    if "gay" in message.content:
        await CLIENT.add_reaction(message, '🏳️‍🌈')
        print("added gay to {}".format(message.content))

CLIENT.run(TOKEN)
