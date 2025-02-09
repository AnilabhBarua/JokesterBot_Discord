
# 🎭 JokesterBot - AI-Powered Discord Bot  

JokesterBot is an interactive Discord bot powered by **Google Gemini AI**, built using `discord.py`. It can generate responses to user messages using AI and is easily customizable with more commands.  

## 🚀 Features  
✅ Uses **Google Gemini AI** for natural language responses  
✅ Slash command `!chat <message>` – The bot responds with AI-generated text  
✅ Secure API key storage with environment variables  
✅ Built with `discord.ext.commands` for better command handling  

## 🛠️ Setup and Usage  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/AnilabhBarua/JokesterBot_Discord.git
cd JokesterBot_Discord
```

### 2️⃣ Create a virtual environment (optional but recommended)  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Create a `.env` file** and add your Discord bot token & Gemini API key:  
```
DISCORD_BOT_TOKEN=your_discord_bot_token
GEMINI_API_KEY=your_gemini_api_key
```

### 5️⃣ Run the bot  
```bash
python bot.py
```

## 🔥 Bot Commands  

| Command         | Description                         |
|----------------|-------------------------------------|
| `!chat <msg>`  | Chat with the AI-powered bot       |

## 🤖 Adding More Features  
Want to add more commands? Just modify `bot.py` and add commands like this:  

```python
@bot.command()
async def joke(ctx):
    await ctx.send("Why did the chicken cross the road? To get to the other side! 🐔")
```

## 📌 Notes  
- Make sure **Message Content Intent** is enabled in Discord Developer Portal.  
- Ensure your `.env` file is correctly set up.  

## 🤝 Contributing  
Feel free to fork the repo, add your own features, and make a pull request!  

