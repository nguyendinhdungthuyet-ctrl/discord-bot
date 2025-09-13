import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True  # cần cho discord.py 2.0+
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập với tên: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

# lấy token từ biến môi trường
bot.run(os.getenv("DISCORD_TOKEN"))
