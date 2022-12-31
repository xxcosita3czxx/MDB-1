import discord
from discord import app_commands

## Config

token = "token"
prefix = 'prefix'
status = 'dnd'

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