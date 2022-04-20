#Hello Guys And Welcome To Another Video! Today I Will Be Showing You How To Make A Custom Help Command With Nextcord.py!

#I Will Upload This Code To Github 👍

#This Code Should Work

import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.remove_command('help')

@bot.command(name='help', description='Returns The Help Command')
async def help(ctx):
    text_help = '```'
    for command in bot.commands:
        text_help+=f"!{command}, Description: {command.description or 'No Description Was Provided'}"
    text_help+='```'
    embed = nextcord.Embed(
        title = '',
        description=text_help
    )
    await ctx.send(embed=embed)

bot.run("")
