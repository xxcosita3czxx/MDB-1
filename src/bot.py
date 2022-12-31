import discord
from discord import app_commands
import os 
from dotenv import load_dotenv

## Config
load_dotenv()
token = os.getenv(token)
status = os.getenv(status)

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
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