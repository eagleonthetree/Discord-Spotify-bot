import discord
from discord.ext import commands

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('Dan is ready')


@client.command()
async def noob(ctx):
    await ctx.send(f'Danny is noob!')

@client.command()
async def p(ctx):
    await ctx.send(f'Talking with girlfriend ar diu')



client.run('ODI3MDM4NjE1NDk0MTk3MzE5.YGVNuw.7Pompd-gBlg2OF_tfLloM-vUuN0')

