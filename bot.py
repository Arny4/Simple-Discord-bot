import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.bot(command_prefix = '!')

token = "you bot token"

@bot.event
async def on_ready():
    print('Bot is ONLINE!')
   
   
#A simple discord bot command
@bot.command(pass_context= True)
async def ping(ctx):
    await bot.say("Pong!")
    
#Simple discord bot command with embed box
@bot.command(pass_context= True)
async def embed(ctx):
    emb=Discord.Embed(title = "You title", description = "You description", colour = 5296861)
    emb.set_author(name = "Author", icon_url = "https://cdn.discordapp.com/embed/avatars/3.png")
    emb.set_footer(text = "Footer text", icon_url = "https://cdn.discordapp.com/embed/avatars/3.png")
    await bot.say(embed= emb)
    
    
bot.run(token)
