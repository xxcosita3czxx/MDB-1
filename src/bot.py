import discord
from discord import app_commands
import os
import logging
import coloredlogs
from dotenv import load_dotenv

## Config
coloredlogs.install()
logging.basicConfig(filename='bot.log', encoding='utf-8',format='%(asctime)s : %(levelname)s >> %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
load_dotenv()
token = os.getenv('token')
status = os.getenv('status')

# Text

help_list="""**HELP**
<< UL1T9 >> 
help = /help
ping = /ping
<< T3ST1NG >>
test = /test
"""

hello_list=["Hey","Hello","Hi"]
bhai_list=["bhai","Goodbye","bye"]
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
        logging.info("Ready, logged in to Bot account")


bot = aclient()
tree = app_commands.CommandTree(bot)
## Events

@bot.event
async def on_message(message):
  # This checks if the message is not from the bot itself. If it is, it'll ignore the message.
  if message.author == client.user:
    return

  # From here, you can add all the rules and the behaviour of the bot.
  # In this case, the bot checks if the content of the message is "Hello!" and send a message if it's true.
  if message.content == hello_list:
    await message.channel.send("Hello! I'm happy to see you around here.")
    return

  if message.content == bhai_list:
    await message.channel.send("Hope to see you soon!")
    return


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