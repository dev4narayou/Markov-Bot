import os
from dotenv import load_dotenv
import discord
from discord import Intents, Message, TextChannel
import markovify

# get the discord token stored in .env (environment variable)
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# intents allow bots to subscribe to specific buckets of events
# i.e. intents specify what a bot is for, and has access to (they specify what events the bot will receive from discord)
intents = Intents.default()
intents.message_content = True

# client represents connection to discord; client handles events, interacts with discord APIs
client = discord.Client(intents=intents)

# store for different markov models
markov_models = {}
channel_messages = {}

# on_ready event handler: called when client is ready 
@client.event
async def on_ready():
    print(f'{client.user} has connected successfully to Discord')
    
@client.event
async def on_message(message):
    # prevents the bot responding to itself!
    if message.author == client.user:
        return
    
    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)
    print(channel, ':', username, user_message)
    
    await send_message(message, user_message)
        
async def send_message(message: Message, user_message: str) -> None:
    if 'hello' in user_message.lower():
        await message.channel.send(f"Hello, {message.author}!")
        
    elif user_message.startswith('!markov'):
        generated_message = await generate_markov_message(message, user_message)
        if generated_message:
            await message.channel.send(generated_message)
        else:
            message.channel.send("I'm not working right now womp womp")
        

# PROOF OF CONCEPT
async def generate_markov_message(message: Message, user_message: str):
    channel_id = message.channel.id

    if channel_id not in markov_models:
        channel_messages[channel_id] = ''
        await update_markov_training(message.channel)
    
    model = markov_models[channel_id]
    return model.make_sentence()

# PROOF OF CONCEPT
async def update_markov_training(channel: TextChannel):
    async for message in channel.history():
        if message.author == client.user:
            continue
        if message.content.startswith('!markov'):
            continue
        channel_messages[channel.id] += message.content + '\n'

    # create new markov model (note .NewlineText not .Text)
    markov_models[channel.id] = markovify.NewlineText(channel_messages[channel.id])
    


# def get_response(user_input: str) -> str:
#     lowered_input = user_input.lower()

if __name__ == "__main__":
    client.run(DISCORD_TOKEN)
