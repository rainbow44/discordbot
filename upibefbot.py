import discord
import random
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix = '.')

@client.event 
async def on_ready():
	print(f"{client.user.name} is Online")
	game = discord.Game("test")
	await client.change_presence(status=discord.Status.online, activity=game)	

@client.command(aliases=['hi', 'privet', 'darova'])
async def hello(ctx):
	await ctx.send(f'hello, {ctx.author.nick}')

@client.command()
async def love(ctx, member : discord.Member):
	await ctx.send(f'love between {ctx.author.name} and {member.name} is {random.randint(1,101)} % ')

@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)}ms')

@client.command()
async def close(ctx):
	await ctx.send('vsem bb')
	await client.close()

@client.command(aliases=['8ball'])
async def ball8(ctx, *, question):
	resp = ['Бесспорно',
	 'Предрешено', 
	 'Никаких сомнений',
	 'Определённо да', 
	 'Можешь быть уверен в этом',
	 'Мне кажется — «да»', 
	 'Вероятнее всего',
	 'Хорошие перспективы', 
	 'Знаки говорят — «да»',
	 'Да',
	 'Пока не ясно, попробуй снова',
	 'Спроси позже',
	 'Сейчас нельзя предсказать',
	 'Лучше не рассказывать',
	 'Сконцентрируйся и спроси опять',
	 'Даже не думай',
	 'Мой ответ — «нет»',
	 'По моим данным — «нет»',
	 'Перспективы не очень хорошие',
	 'Весьма сомнительно']
	await ctx.send(f'Вопрос: {question}\nОтвет: {random.choice(resp)}')

@client.command()
async def clear(ctx, amount=5):
	def check(m):
		return ctx.author == m.author
	amount += 1
	await ctx.channel.purge(limit=amount,check=check)

@client.command()
async def test(ctx, arg):
	await ctx.send(arg)



@client.command(aliases=['membercount'])
async def mc(ctx):
		online = 0
		idle = 0 
		offline = 0
		upibef_guild = client.get_guild(331177508844077057)
		for i in upibef_guild.members:
			if str(i.status) == "online":
				online += 1
			if str(i.status) == "offline":
				offline += 1
			else:
				idle += 1
		overallonline = online + idle
		await ctx.send(f"```Online: {overallonline}\nOffline: {offline} ```")

@client.command()
async def botclear(ctx, amount=5):
	def isme(i):
		return i.author == client.user
	await ctx.channel.purge(limit=amount, check=isme)

#@client.command()
#async def kick(ctx, member, *, reason=None):
	#def checc(a):
		#return ctx.author == 
	#await member.kick(reason=reason)


client.run("NjAwOTcyNzcyNTE2Mjk4Nzgz.XS9odw.OFBTok2bjwivaTm691nO76WDX_k")

