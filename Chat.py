import discord
from discord import utils
from discord import utils, Client
from discord import Member as DiscordMember
from discord.ext.commands import BadArgument, CommandNotFound, MissingRequiredArgument
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from typing import Optional
import time
from asyncio import sleep
import config

client = discord.Client()
client = commands.Bot(command_prefix= '+')

chat_filter =('БЛЯДЬ', 'ЕБАТЬСЯ', 'СОСАТЬ', 'ЕБАТИСЬ', 'ПИДОР', 'ПИДОРИ', 'ХУЯРЮ', 'ПИДОРАСИНА', 'FUCK', 'АХУЕЛ', 'ПИЗДОС', 'ПИЗДУ', 'ДОЛБОЕБ', 'ДОЛБАЁБ', 'ДОЛБАЕБ', 'ЙБАНУТЬСЯ', 'НАЕБ', 'НАЕБАЛ', 'ВЫЕБОН', 'ВЫЕБИВАТЬСЯ', 'ВИЕБУ', 'ЕБ', 'НАХУЙ', 'БЛЯ', 'ЕБУ', 'БЛЯТЬ', 'ХУЙНЮ', 'НИХУЯ', 'ПИДОРАС', 'ПИДАРАС', 'ЕБАТЬ', 'ЕБЛЯ', 'ЁБ', 'ПИЗДА', 'ХУЙ', 'БЛЯДИАДА', 'БЛЯДИНА', 'БЛЯДСКИЙ', 'ВПИЗДЯЧИЛ', 'ВЫЁБЫВАЕТСЯ', 'ДОЕБАЛСЯ', 'ЕБАЛО', 'ЕБАНЁШЬСЯ', 'ЕБАНУЛСЯ', 'ЕБАШИТ', 'ЁБНУЛ', 'ЗАЕБАЛ', 'ЗАЕБИСЬ', 'НАЕБАШИЛСЯ', 'НАЕБНУЛСЯ', 'ПЁЗДЫ', 'ПИЗДАБОЛ', 'ПИЗДЕЦ', 'СПИЗДИЛ', 'УЕБАЛСЯ', 'УЕБАЛАСЯ', 'УЁБИЩЕ', 'ХУЁВО', 'ХУЕВО', 'ХУЙНЯ', 'ЕБАЛ', 'НАХУЙ ПОШЕЛ', 'АХУЕТЬ', 'ПИДР', 'ХУЕПУТАЛО', 'ЧЛЕН', 'ПЕДРИЛО', 'ХЕР', 'ПСИНА', 'ХУЙЛО', 'ДРЯНЬ', 'СУКА', 'СУЧКА', 'ШАЛАВА', 'ЧМО', 'ХУЕГЛОТ', 'ПИДАРЮГА', 'УЕБИЩЕ', 'ЕБЛАН', 'УЕБАН', 'УЕБАНИЩЕ', 'ЕБНУТИЕ', 'БЛ', 'ПЗДЦ', 'СЬЕБАЛ', 'ЕБУ',  'ДОЛБАН', 'ХУИЛО', 'ЕБУШАТНИК', 'ЕБЛАН', 'ХУЙЛОПАН', 'ПИЗДОЛИЗ', 'УСОС', 'ЕБОБО', 'ЕБАЛЬНИК', 'САСАТЬ', 'ХУЙ СОСИ', 'СОСАТЬ', 'СРАКА МОТИКА', 'ЙБАТЬ' 'ДОХУЯ', 'ЙБАНУТЬСЯ', 'ЙБАТЬ')
chat_sleep =('СПОКИ', 'СПОКОЙНОЙ', 'СПОКОНОЙ НОЧИ', 'Я СПАТЬ', 'СПАТЬ', 'НОЧИ', 'Я СПЛЮ')
chat_delete =(', не используй это слово больше!А то я тебя накажу!', 'Желаю сладких снов. Хочешь сказку розкажу?Если да, напиши .сказка')
chat_hi = ('ПРИВЕТ', 'ХЕЛЛО', 'HELLO', 'HI', 'ХАЙ')

@client.event
async def on_message(message):
	contents = message.content.split(" ")
	for word in contents:
		if word.upper() in chat_filter:
			await message.delete()
			await message.channel.send(f"{message.author.mention}, Ееех ты, зачем используешь плохие слова? Это же не культурно... :(")
			await sleep(2.3)
			await message.delete()
		else:
			if word.upper() in chat_sleep:
				await message.channel.send(f"{message.author.mention}, Желаю сладких снов. Хочешь сказку розкажу?Если да, напиши .сказка")
				await sleep(2.3)
				await message.delete()
				return
			else:
				if word.upper() in chat_hi:
					await message.channel.send(f"{message.author.mention}, Приветули :blush:!")
					await sleep(2.3)
					await message.delete()
					return

client.run('NjM1ODY0MDgzOTQ5NjgyNzM1.XfVlRQ.l6UBFjVJLw4Ru82FP2s3tjbTUms')