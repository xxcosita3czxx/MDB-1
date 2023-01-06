import discord
from discord import app_commands
import os
import logging
import coloredlogs
from dotenv import load_dotenv

##config
coloredlogs.install()
logging.basicConfig(filename='bot.log', encoding='utf-8',format='%(asctime)s : %(levelname)s >> %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
load_dotenv()
token = os.getenv('token')
status = os.getenv('status')
help_list="""**HELP**
<< UL1T9 >> 
help = /help
ping = /ping
<< T3ST1NG >>
test = /test
"""

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        logging.info("Ready, logged in to Bot account")


bot = aclient()
tree = app_commands.CommandTree(bot)

## Commands

# Ulity

@tree.command(name="ping", description="Lets play ping pong")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('Pong! {0}'.format(round(bot.latency, 1)))

@tree.command(name="help", description="All the commands at one place")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(help_list)

# Test

#@tree.command(name = "test",description="Super ultra giga test")
#async def test(interaction: discord.Interaction, test_text):
#    await interaction.response.send_message(f"Hello! option = {test_text}")

## Run 

bot.run(token, log_handler=None)