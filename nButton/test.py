import discord
from discord.ext import commands
import discord.ui
from discord.ui import Button
import random
def button_n(label: str, style: str):
    a = discord.ui.button(label=f"{label}", style=style)
    print(a)
    return a


def button_e(label: str,
    style: str, 
    emoji: str):
    a = discord.ui.button(label=label, style=style, emoji=emoji)
    print(a)
    return a

def send_msg(content):
    a = await interaction.send_message(content)
    return a

def para_btn()
    a = self, interaction: discord.Interaction, button: discord.Button
    return a         
