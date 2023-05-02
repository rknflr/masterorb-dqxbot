# This example requires the 'message_content' intent.

import discord
import orb
import os

from dotenv import load_dotenv

load_dotenv()

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')
        await client.change_presence(activity=discord. Activity(type=discord.ActivityType.watching, name='$jewel [English/Japanese/Romaji Name]'))
        

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith("$jewel"):
            try:
                if(len(message.content) < 7):
                    await message.channel.send("Follow the command: $jewel [English/Japanese/Romaji Name]")
                else:
                    await message.channel.send(embed=orb.orb_result(message.content[7:]))
            except Exception as e:
                print(e)

    client.run(os.getenv("TOKEN"))