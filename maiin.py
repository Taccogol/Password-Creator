import discord
import asyncio
from discord.ext import commands

botsito = commands.Bot(command_prefix="¡", intents=discord.Intents.all())
 
@botsito.command()
async def ping(ctx):
    await ctx.send("pong")

@botsito.command()
async def comandos(ctx):
    await ctx.send("")

@botsito.after_invoke


botsito.run("MTExMzQ1MTY3OTAwMjY1NjgyOA.GbiNVm.Pg27-vyQPbrbhfWfcXxTbMo-UbV4bQI5SmbnAk")