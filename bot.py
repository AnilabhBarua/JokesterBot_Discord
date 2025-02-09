import discord
import google.generativeai as genai
import os
from discord.ext import commands
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Google Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True  # Required for receiving messages
bot = commands.Bot(command_prefix="!", intents=intents)

# Get AI response
def get_gemini_response(user_input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_input)
    return response.text if response.text else "I couldn't generate a response."

# Bot event
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!chat"):
        user_message = message.content[len("!chat "):]
        await message.channel.send("💬 Thinking...")
        response = get_gemini_response(user_message)
        await message.channel.send(response)

# Run the bot
bot.run(DISCORD_BOT_TOKEN)
