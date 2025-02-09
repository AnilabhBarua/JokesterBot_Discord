import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Setting up the bot with required intents
intents = discord.Intents.default()
intents.message_content = True  # Needed for message-based commands

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')
    try:
        await bot.tree.sync()  # Syncing slash commands
        print('✅ Slash commands synced!')
    except Exception as e:
        print(f'❌ Error syncing commands: {e}')

# Basic slash command
@bot.tree.command(name="hello", description="Say hello to the bot!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello! 👋")


bot.run(TOKEN)
