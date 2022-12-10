
# Import nextcord libary 
from nextcord import Interaction
from nextcord.ext import commands

# Create a new Discord client
bot = commands.Bot(command_prefix="!")

# Define an event for when the bot is ready to connect to Discord
@bot.event
async def on_ready():
  # Print a message to the console to confirm that the bot has connected
  print("Im Ready")

# Define an event for when the bot receives a message
@bot.event
async def on_message(message):
  # Ignore messages sent by the bot itself
  if message.author.bot:
    return 
  #make !github command
  if message.content.startswith("!github"):
    #respond my github profile link
    await message.channel.send("https://github.com/YarinTheDev")
    
    
# make an slash command named hello
@bot.slash_command(name="hello")
async def hello(interaction: Interaction):
  # responding with "whats up?"
  await interaction.send("WHATS UP?")
  
  
#Running the bot
bot.run("YOUR_TOKEN_GOES_HERE")
