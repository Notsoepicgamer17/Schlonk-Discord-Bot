import os
bot_token = os.environ['TOKEN']

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=['S!', 's!'], description='Schlonk', intents=intents, help_command=None, case_insensitive=True)

@bot.event
async def on_ready():
	print("Schlonk")
	await bot.change_presence(activity=discord.Game('Schlonk'))
	channel = bot.get_channel(926278759445844080)
	await channel.send("Schlonk <:schlonk:1003615664235364394>")

@bot.command()
async def schlonk(ctx):
	await ctx.send("<:schlonk:1003615664235364394>")

@bot.command()
async def schlonk2(ctx):
	await ctx.send("<:Schlonk2:1014970236216287312>")

@bot.command()
async def whatis(ctx, arg):
	if arg in ("schlerd", "Schlerd"):
		await ctx.send('''schlerd
——————
noun

A flock of schlonk.
*"owen ran when he saw the schlerd of schlonks running towards him"*''')
	
	elif arg in ("schlonkulous", "Schlonkulous"):
		await ctx.send('''schlonkulous
———————-
adjective

describing a person who is schlonk.
*“owen is very schlonkulous when it comes to schlonkology”*''')
	
	elif arg in ("schlonkist", "Schlonkist"):
		await ctx.send('''schlonkist
——————
adjective

A form of bigotry towards schlonks.
*“samuel is very schlonkist towards straight schlonks because he himself is not straight.”*''')
	
	elif arg in ("schlonkular", "Schlonkular"):
		await ctx.send('''Schlonkular
——————— 
adjective 

A way of describing something or something in a way relating to schlonk.
*“Trace’s dick is very schlonkular in appearance, being long and skinny at the base but curving back towards the tip.”*''')
	
	else:
		await ctx.send("That's not a schlonkular term")

@bot.command()
async def schlonktionary(ctx):
	await ctx.send('''This is the current state of the schlonktionary:
 ```
 Schlerd
 Schlonkulous
 Schlonkist
 Schlonkular```''')

@bot.command()
async def help(ctx):
	await ctx.send('''```This is a list of every command that you can use with the official Schlonk Bot
 schlonk- When you need to schlonk
 schlonk2- The first schlonk is better, just don't use this one
 whatis <insert schlonkular term>- Get the definition of a schlonkular term
 schlonktionary- See every word that is currently in the schlonktionary```''')

bot.run(bot_token)
