import discord
from discord import app_commands
import os
import logging
import coloredlogs
from dotenv import load_dotenv
import platform
coloredlogs.install()
## Pre start
if platform.system() == "Windows":
    os.system("cls")
elif platform.system() == "Linux":
    os.system("clear")
logging.info("Clearing")
## Config
logging.basicConfig(filename='bot.log', encoding='utf-8',format='%(asctime)s : %(levelname)s >> %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
load_dotenv()
token = os.getenv('token')
status = os.getenv('status')
#activity = os.getenv('activity')
logging.info("Config loaded successfully")
# Text

help_list="""**HELP**
<< UL1T9 >> 
help = /help
ping = /ping
<< T3ST1NG >>
test = /test
"""

hello_list=["Hey","Hello","Hi","helo","hey"]
bhai_list=["bhai","Goodbye","bye","bye bye"]

logging.info("Text for commands loaded successfully")
## Client 
class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        await bot.change_presence(status=status)
        logging.info("Ready, logged in to Bot account")


bot = aclient()
tree = app_commands.CommandTree(bot)
## Events
logging.info("Loading events")
@bot.event
async def on_message(message):
  if message.author == bot.user:
    return


  if message.content in hello_list:
    await message.channel.send("Hello! I'm happy to see you around here.")
    return

  if message.content in bhai_list:
    await message.channel.send("Hope to see you soon!")
    return
logging.info("Loading commands")
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
logging.info("All things loaded!")
bot.run(token, log_handler=None)