import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True # can read messages
bot = commands.Bot(command_prefix ='!', intents = intents) # prefix is !
