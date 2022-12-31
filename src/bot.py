import discord
from discord import app_commands
import os 
from dotenv import load_dotenv

## Config

load_dotenv()
token = os.getenv('token')
prefix = os.getenv('prefix')
status = os.getenv('status')

intents = discord.Intents.default()
bot = discord.Client(intents=intents,prefix=prefix)
tree = app_commands.CommandTree(bot)

@bot.event()
async def on_ready():
    print("Ready!")

@tree.command(name="ping", description="Lets play ping pong")
async def ping(interaction):
    await interaction.response.send_message("Pong!")


bot.run(token)