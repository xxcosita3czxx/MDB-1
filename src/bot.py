import discord
from discord import app_commands
import os 
from dotenv import load_dotenv

## Config
load_dotenv()
token = "token"
prefix = 'prefix'
status = 'dnd'

intents = discord.Intents.default()
bot = discord.Client(intents=intents,prefix=prefix)
tree = app_commands.CommandTree(bot)

## Main code

# Events

@bot.event()
async def on_ready():
    print("Ready!")

# Commands

@tree.command(name="ping", description="Lets play ping pong")
async def ping(interaction):
    await interaction.response.send_message("Pong!")

## Run 

bot.run(token)