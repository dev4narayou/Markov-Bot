import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

client = commands.Bot(command_prefix = "?" ,intents=discord.Intents.all())

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

client.run('enter token here')
