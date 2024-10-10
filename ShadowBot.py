import discord
from discord.ext import commands
import json

intents = discord.Intents.default()
intents.message_content = True # can read messages
bot = commands.Bot(command_prefix ='!', intents = intents) # prefix is !

# parse through json file
def load_registered_users():
    with open('registered_users.json','r') as file:
        return json.load(file)
    
registered_users = load_registered_users() # dictionary to map emails to team numbers
