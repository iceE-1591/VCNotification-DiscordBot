from discord.ext import commands
import discord

import settings

intents = discord.Intents.all()
TOKEN = settings.TOKEN
prefix = "/"

bot = commands.Bot(command_prefix=prefix, help_command=None, intents=intents)

bot.load_extension("main")

bot.run(TOKEN)
