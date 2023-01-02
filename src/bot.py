import discord
from discord import app_commands
import os 
import config

## vars
token = config("token")
status = config("status")

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id="YOUR GUILD ID"))
            self.synced = True

bot = aclient()
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

#test

@tree.command(name = "test",description="Super ultra giga test")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")


## Run 

bot.run(token)