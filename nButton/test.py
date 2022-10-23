import discord
from discord.ext import commands
import discord.ui
from discord.ui import Button
import random
def button_n(label: str, style: str):
    a = discord.ui.Button(label=f"{label}", style=style)
    print(a)
    return a


def button_e(label: str,
    style: str, 
    emoji: str):
    a = discord.ui.Button(label=label, style=style, emoji=emoji)
    print(a)
    return a