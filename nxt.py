
# Import nextcord libary 
from nextcord import Interaction
from nextcord.ext import commands

bot = commands.Bot(command_prefix="!")
@bot.event
async def on_ready():
  print("Im Ready")

@bot.event
async def on_message(message):
  if message.author.bot:
    return 
  if message.content.startswith("!github"):
    await message.channel.send("https://github.com/YarinTheDev")
# make an slash command named hello
@bot.slash_command(name="hello")
async def hello(interaction: Interaction):
  # responding with "whats up?"
  await interaction.send("WHATS UP?")
  
  
#Running the bot
bot.run("YOUR_TOKEN_GOES_HERE")
