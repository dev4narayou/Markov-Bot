import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio, TextChannel, Message
import markovify

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = "?" ,intents=discord.Intents.all())

markov_models = {}
channel_messages = {}

@client.event
async def on_ready():
    print("bot is ready")
    print("------------------")

@client.command()
async def hello(ctx):
    await ctx.send("hello")


@client.command()
async def backshots(ctx):
    await ctx.send("https://tenor.com/view/anime-gif-7279870884587886608")


@client.command()
async def hollowpurple(ctx):
    await ctx.send("https://tenor.com/view/jujutsu-kaisen-second-season-satoru-gojo-purple-hollow-purple-gif-15126148765882407056")


@client.event
async def on_member_join(member):
    channel = client.get_channel(1195337419227144255)
    await channel.send("a smelly individual has arrived")


@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channelgit 
        voice = await channel.connect()
        source = FFmpegPCMAudio('1x1lego.mp3')
        player = voice.play(source)
        await ctx.send("you're in for a treat")

    else:
        await ctx.send("Your bomboclat not in voice channel dawg")


@client.command(pass_context = True)
async def leave(ctx): 
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("bye bye")
    else:
        await ctx.send("Im not in")


@client.command(pass_context=True)
async def markov(ctx):
    generated_message = await generate_markov_message(ctx)
    if generated_message:
        await ctx.send(generated_message)
    else:
        await ctx.send("I couldn't generate a message right now. Please try again later.")

async def generate_markov_message(ctx):
    channel_id = ctx.channel.id

    if channel_id not in markov_models:
        channel_messages[channel_id] = ''
        await update_markov_training(ctx.channel)
    
    model = markov_models[channel_id]
    return model.make_sentence()

async def update_markov_training(channel: TextChannel):
    async for message in channel.history():
        if message.author == client.user:
            continue
        if message.content.startswith('?markov'):
            continue
        channel_messages[channel.id] += message.content + '\n'

    # create new markov model (note .NewlineText not .Text)
    markov_models[channel.id] = markovify.NewlineText(channel_messages[channel.id])

if __name__ == "__main__":
    print('testing')
    client.run(DISCORD_TOKEN)
