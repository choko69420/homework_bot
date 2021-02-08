import discord
import os
from replit import db
from keepalive import keep_alive
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler


client = discord.Client()
client = commands.Bot(command_prefix = '.')

days = [
["qartuli 5 0-10","fizika 5 40-50","matematika 6 25-35","matematika 7 10-20","istoria 9 25-35","inglisuri 10 10-20"],
["qartuli 5 0-5","fizika 5 40-45","fizika 6 25-35","matematika 7 10-20", "samoqalaqo 8 40-50", "biologia 9 30-40", "musika 11 40-50"],
["matematika 5 0-5","matematika 5 40-45","qartuli 6 25-35","fizika 7 10-20","istoria 8 40-50","inglisuri 9 25-35"],
["qartuli 5 0-5","fizika 5 40-45","matematika 6 25-35","matematika 7 10-20","rusuli 8 40-50","geografia 9 25-35","inglisuri 10 10-20"],
["fizika 5 0-5","matematika 5 40-45","matematika 6 25-35","qartuli 7 10-20","xelovneba 9 25-35","qimia 10 10-20"]
]
weekendd = ["mon","tue","wed","thu","fri"]
links = ["https://us04web.zoom.us/j/3782012234?pwd=aTA0SzlrTjB0eC9VN2JNbmRuemIrZz09","https://us04web.zoom.us/j/7396383539?pwd=WEE3QllEemF1VElDaC9Sc0t0U0Z2dz09","https://us04web.zoom.us/j/4388107807?pwd=dlg3WEYxVEVNZWN2WVl4VjY5bHo0QT09","https://us04web.zoom.us/j/4735191542?pwd=bUJHWWd5U2d2ZWlaMDd1M3BNb0prZz09&fbclid=IwAR3mBQppRuW-o-B4grsljfnekfmeB3E_WHnalFotstSpus94KZA72bUg4hY","https://us04web.zoom.us/j/7478275475?pwd=WVR2QUJ2VVZabEFieVJUcGNFNnFsUT09","https://us04web.zoom.us/j/75351830846?pwd=YWlKcnJYMDA1RTFBb3FtdCtFaU1wUT09",
"https://us04web.zoom.us/j/71930596311?pwd=emZwdkVGN1BwSUlhVjFKK0hPWlZtQT09"]
#tanmimdebrobit linkebi gakvesi dabla
gakve = ["qartuli","fizika","matematika","istoria","inglisuri","xelovneba","qimia" ]



channel = client.get_channel(796664227468148759)
sched = AsyncIOScheduler()
def sachiro():
	global pp
	for i in range(len(days)):
		for j in range(len(days[i])):
			dd = days[i][j].split(" ")
			for g in range(len(gakve)):
				if gakve[g] == dd[0]:
					pp = g
			sched.add_job(sendchokosmessage,"cron" ,[pp], day_of_week = weekendd[i], hour = dd[1] , minute=dd[2])




def Add_db(message,sagani):
        db[sagani] = message  


async def sendchokosmessage(gakve):
	channel = client.get_channel(796664227468148759)
	await client.wait_until_ready()
	await channel.send(links[gakve])



@client.event
async def on_ready():
	print("ready")


@client.command()
async def showhw(ctx,sagani):
	await ctx.send(db[sagani])


@client.command()
async def addhw(ctx,sagani,message):
	Add_db(message,sagani)
	await ctx.send("Davaleba damatebulia!" + message)


@client.command()
async def removehw(ctx,sagani):
	del db [sagani]
	await ctx.send("davaleba waishala!")


@client.command()
async def helpchoko(ctx):
	await ctx.send(".showhw [matematika/qartuli/fizika] \n .addhw [matematika/qartuli/fizika] [davalebis shinaarsi brchyalebshi \' an \" \n .removehw [matematika/qartuli/fizika] ")


keep_alive()
sachiro()
sched.start()
client.run(os.getenv('TOKEN'))
