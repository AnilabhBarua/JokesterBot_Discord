import discord
import groq
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Configure the Asynchronous Groq Client
client = groq.AsyncGroq(api_key=GROQ_API_KEY)

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# ------------------ Groq API call ------------------
async def get_groq_response(user_input):
    try:
        response = await client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred with Groq API: {e}")
        return "Sorry, I couldn't get a response. There might be an issue with the API."

# ------------------ Events ------------------
@bot.event
async def on_ready():
    try:
        # Sync slash commands
        await bot.tree.sync()
        print("✅ Slash commands synced.")
    except Exception as e:
        print(f"Slash sync failed: {e}")
    print(f"✅ Logged in as {bot.user}")

# ------------------ Slash Command ------------------
@bot.tree.command(name="chat", description="Chat with the AI assistant")
async def slash_chat(interaction: discord.Interaction, message: str):
    await interaction.response.defer()  # show "thinking..." indicator

    full_response = await get_groq_response(message)

    # Send API response
    await interaction.followup.send(full_response)

    # Wait 6 seconds, then send your hardcoded line
    await asyncio.sleep(6)
    await interaction.followup.send("aur yaad rakhna Error69 dalla tha,, dalla hei, aur dalla hi rhega!")

# ------------------ Legacy !chat command (optional) ------------------
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!chat"):
        user_message = message.content[len("!chat "):].strip()
        if not user_message:
            await message.channel.send("Please provide a message after `!chat`.")
            return

        async with message.channel.typing():
            full_response = await get_groq_response(user_message)
            await message.channel.send(full_response)

        await asyncio.sleep(6)
        await message.channel.send("aur yaad rakhna Error69 dalla tha,, dalla hei, aur dalla hi rhega!")

# ------------------ Run bot ------------------
bot.run(DISCORD_BOT_TOKEN)
