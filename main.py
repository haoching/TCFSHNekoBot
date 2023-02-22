import nextcord
from nextcord.ext import commands
from os import environ
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import json
#import requests

load_dotenv()

token = environ["TOKEN"]

total = 0

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="My first slash command", guild_ids=None)
async def nyan(interaction: nextcord.Interaction):
    embedVar = nextcord.Embed(title="貓貓", description="貓貓基本資料", color=0x7FFFD4 )
    embedVar.add_field(name="test", value=123, inline=False)
    await interaction.send(embed=embedVar)

async def feed(interaction: nextcord.Interaction,NumOfCan : str):
    await interaction.send("成功為了貓{NumOfCan}次,今天被餵了{total}")
                              
bot.run(token)