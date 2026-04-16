import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

active_timers = set()

@bot.event
async def on_ready():
    print(f"Bot online: {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Slash commands sincronizate: {len(synced)}")
    except Exception as e:
        print(e)

async def start_timer(interaction, total_minutes, name):
    if name in active_timers:
        await interaction.response.send_message(f"❌ Timerul pentru **{name}** este deja activ!", ephemeral=True)
        return
    active_timers.add(name)
    await interaction.response.send_message(f"⏳ Timer pornit pentru **{name}**!")
    try:
        await asyncio.sleep((total_minutes - 15) * 60)
        await interaction.channel.send(f"@everyone ⚠️ {name} poate fi dată în 15 minute!")
        await asyncio.sleep(15 * 60)
        await interaction.channel.send(f"@everyone 💰 {name} poate fi dată ACUM!")
    finally:
        active_timers.remove(name)

@bot.tree.command(name="alta", description="Timer banca Alta")
async def alta(interaction: discord.Interaction):
    await start_timer(interaction, 120, "Banca Alta")

@bot.tree.command(name="vinewood", description="Timer banca Vinewood")
async def vinewood(interaction: discord.Interaction):
    await start_timer(interaction, 120, "Banca Vinewood")

@bot.tree.command(name="highway", description="Timer banca Highway")
async def highway(interaction: discord.Interaction):
    await start_timer(interaction, 120, "Banca Highway")

@bot.tree.command(name="desert", description="Timer banca Desert")
async def desert(interaction: discord.Interaction):
    await start_timer(interaction, 120, "Banca Desert")

@bot.tree.command(name="blaine", description="Timer banca Blaine")
async def blaine(interaction: discord.Interaction):
    await start_timer(interaction, 120, "Banca Blaine")

@bot.tree.command(name="biju", description="Timer banca Biju")
async def biju(interaction: discord.Interaction):
    await start_timer(interaction, 120, "Banca Biju")

@bot.tree.command(name="pacific", description="Timer banca Pacific")
async def pacific(interaction: discord.Interaction):
    await start_timer(interaction, 240, "Banca Pacific")

token = os.environ.get("DISCORD_BOT_TOKEN")
bot.run(token)
