import discord
import groq
import os
import asyncio # Still needed for the 0.5s delay
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

# This function to get the response from Groq remains the same
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

# Bot event
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!chat"):
        user_message = message.content[len("!chat "):].strip()
        if not user_message:
            await message.channel.send("Please provide a message after `!chat`.")
            return

        # --- MODIFIED LOGIC STARTS HERE ---
        
        # 1. Show a "typing..." status while waiting for the API
        async with message.channel.typing():
            # Get the full response from the API
            full_response = await get_groq_response(user_message)
            # Send the entire response in one message
            await message.channel.send(full_response)
        
        # 2. Wait for exactly 0.5 seconds
        await asyncio.sleep(6)
        
        # 3. Send your hardcoded sentence
        await message.channel.send("aur yaad rakhna Error69 dalla tha,, dalla hei, aur dalla hi rhega!")

# Run the bot
bot.run(DISCORD_BOT_TOKEN)