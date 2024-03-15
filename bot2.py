import discord
import random 
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import flip_coin


with open("token.txt", "r") as f:
    token = f.read()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def passwd(ctx):
    await ctx.send(gen_pass(5))

@bot.command()
async def flipone(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


bot.run(token)
