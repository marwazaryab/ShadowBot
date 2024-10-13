import discord
from discord.ext import commands
import json
from dotenv import load_dotenv
import os


load_dotenv() # load environment variables

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True # can read messages
bot = commands.Bot(command_prefix ='!', intents = intents) # prefix is !

# parse through json file
def load_registered_users():
    with open('registered_users.json','r') as file:
        return json.load(file)
    
registered_users = load_registered_users() # dictionary to map emails to team numbers

# verify user based on email address
@bot.command()
async def verify_user(ctx,username:str):
    if username not in registered_users:
        await ctx.send("Email not valid")
    else:
        await ctx.send("Welcome to GiSO! You are in team {registered_users[username]}") # notify based on team

bot.run(DISCORD_TOKEN)