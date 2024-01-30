import discord
from discord.ext import commands
import datetime
import asyncio
from colorama import Fore

CHANNEL_ID = 1026413161575874580

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

restricted_channels = ["bot-commands"]

# Create a bot instance with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def dm_channel_members(ctx, *, message):
    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        print("Channel not found.")
        return

    if not isinstance(channel, discord.TextChannel):
        print("This is not a text channel.")
        return

    counter = 0

    for member in channel.members:
        if member.bot:
            continue

        if counter >= 3:
            counter = 0
            await asyncio.sleep(1)
        try:
            embed = discord.Embed(
            title="ANNOUNCE TUNG SHOP",
            url="https://discord.gg/P5gpDJXVKU",
            description=message
)
            
            #set thumbnail
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1190933106853695609/1190940664565862400/logo4.png?ex=65a3a0ed&is=65912bed&hm=c5a6eae8564b5c8e51f7e4684614e85897589532e0c19f554b61623e00f9db08&=&format=webp&quality=lossless&width=671&height=671")
            #set image
            embed.set_image(url="https://media.discordapp.net/attachments/1026794280309751868/1189492078351228928/0.png?ex=659e5bd3&is=658be6d3&hm=901ae283ac1c9bb0f91689569e4c04b8e0570de6ea042d379f9a5caa92d59d82&=&format=webp&quality=lossless&width=895&height=671")
            embed.timestamp = datetime.datetime.utcnow()
            await member.send(embed=embed)
            print(Fore.LIGHTGREEN_EX + f"Sent message to: {member.name}")
        except discord.errors.Forbidden:
            print(Fore.LIGHTRED_EX + f"Could not send message to: {member.name}")

bot.run('MTE5MTc1MTM4NTkwNjE1OTY3Nw.GceNgi.9_LY4xPtbcNz6tsqi2TbCnhRc1e1BgDXnYRWy0')