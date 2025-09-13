import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập thành {bot.user}")

bot.run(TOKEN)
