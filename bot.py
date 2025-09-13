import os
import discord
from discord.ext import commands

# Lấy token từ biến môi trường
TOKEN = os.getenv("DISCORD_TOKEN")

# Khai báo intents
intents = discord.Intents.default()
intents.message_content = True  # Bật quyền đọc nội dung tin nhắn

# Tạo bot với intents
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập thành {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello 👋! Bot đang hoạt động trên Render 🚀")

bot.run(TOKEN)

