import discord
from discord.ext import commands

#Coded by navy
bot = Bot.commands(prefix_bot="!")

@bot.event()
async def on_ready(ctx):
  print("I'm alive")

@bot.command(name="ping")
async def ping():
  print(f"My ping's {bot.latency} !")

bot.token("")
