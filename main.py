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



client.run('incert client token here')

