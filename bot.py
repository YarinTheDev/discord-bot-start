# Import the discord.py library
import discord

# Create a new Discord client
client = discord.Client()

# Define an event for when the bot is ready to connect to Discord
@client.event
async def on_ready():
    # Print a message to the console to confirm that the bot has connected
    print('We have logged in as {0.user}'.format(client))

# Define an event for when the bot receives a message
@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # make an !github command
    if message.content.startswith('!github'):
        await message.channel.send('Here is a link to my GitHub page: https://github.com/YarinTheDev')

    

# Run the bot with your bot token
client.run('YOUR_BOT_TOKEN_HERE')
