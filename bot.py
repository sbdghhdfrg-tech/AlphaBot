
import os
import discord
from discord import app_commands

class AlphaBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

bot = AlphaBot()

@bot.event
async def on_ready():
    print(f"AlphaBot est connecté : {bot.user}")

@bot.tree.command(name="bonjour", description="AlphaBot te dit bonjour")
async def bonjour(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Salut {interaction.user.mention} ! 🤖"
    )

bot.run(os.environ["DISCORD_TOKEN"])
