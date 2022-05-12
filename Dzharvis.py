import discord
from Dzharvis_config import *
import random
import asyncio
import aiocron
#########
import datetime

#Предустановка
intents = discord.Intents.all()
bot = discord.Client(intents=intents)

#Проверка успешного запуска бота
@bot.event
async def on_ready():
  print('Джарвис запущен как {0.user}'.format(bot))
  user = await bot.fetch_user(My_ID)
  await user.send('Джарвис запущен :thumbsup:')

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  else:
    if message.guild.id == TEST_ID:
      if message.author.id == My_ID and message.content == "1qq":
        await message.reply('Всё ок)', mention_author=True)
####################################################################################
      if message.channel.id == 972798046997979166:
        if message.author.id == My_ID and message.content == "Create":
          channel = bot.get_channel(972798046997979166)
          embed = discord.Embed(title='Золотые цитаты нашей гильдии', color=0xCC0000)
          await channel.send(embed=embed)
          if message.author.id == My_ID and message.content == "111":
            message = channel.fetch_message(973302543235055686)
            load = discord.Embed(title='Золотые цитаты нашей гильдии', description = 'message', color=0xCC0000)
            await message.edit(embed=load)
####################################################################################
@aiocron.crontab('26 11 * * *')
async def Dobroe_utro():
  Today = datetime.datetime.today() - datetime.datetime.today()
  channel = bot.get_channel(Chat)
  History = await channel.history(limit=None, after=Today).flatten()
  for message in History:
    if message.author.id == My_ID and 'SIR' in message.content:
      await channel.send(message)
####################################################################################

####################################################################################
#ЗАВЕРШЕНИЕ
bot.run(TOKEN)

