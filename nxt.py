
# Import nextcord libary 
import nextcord
from nextcord import commands

bot = commands.Bot(command_prefix="!")
@bot.event
async def on_ready():
  print("Im Ready")

@bot.event
async def on_message(message):
  if message.author.bot:
    return 
  if message.content
