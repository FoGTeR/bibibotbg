# This Python file uses the following encoding: utf-8
import os, sys
import os
import config
from asyncio import sleep
from sys import exit
from traceback import format_exc
from typing import Optional
from traceback import format_exc
from typing import Optional
from typing import List
import typing
import random

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

import discord
from discord import utils
from discord import utils, Client
from discord import Member as DiscordMember
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands import BadArgument, CommandNotFound, MissingRequiredArgument

client = discord.Client()
client = commands.Bot(command_prefix= '.')
gamestatus = ".помощь"
game = discord.Game("Напиши .помощь")

@client.command(name='привет', pass_context=True)
async def hello(ctx):
	await ctx.send('Привет {}, как дела?'.format(ctx.message.author.mention))

@client.command(name='очистить', pass_context=True)
@has_permissions(manage_roles=True, ban_members=True)
async def clear(ctx, amount=5, number=1):
	await ctx.channel.purge(limit=amount)
	await ctx.channel.send(f"Готово ")
	await sleep(2)
	await ctx.channel.purge(limit=number)

@client.command(name='правила', pass_context=True)
async def help_2(ctx, number=1):
	await ctx.channel.purge(limit=number)
	await ctx.channel.send(f"•Мат можно использовать только так пи%%$^, если мат не будет запикан больше чем 70%. Вам видаеться мут на 1ч.\n•Оскорбление другого человека караеться 5ч мута.(При наличи скринов)\n•Програмистам всегда рад, пишите @FoGTeR. Рад буду знакомству.")
	await sleep(20)
	await ctx.channel.purge(limit=number)

@client.command(name='очистить-все', pass_context=True)
@has_permissions(manage_roles=True, ban_members=True)
async def clear_all(ctx, amount=10000, number=1):
	await ctx.channel.purge(limit=amount)
	await ctx.channel.send(f"Готово")
	await sleep(2)
	await ctx.channel.purge(limit=number)

@client.command(name='кик', pass_context=True)
@has_permissions(manage_roles=True, ban_members=True)
async def kick(ctx, member : discord.Member, *, reason=None, number=1):
	await member.kick(reason=reason)
	await ctx.channel.send(f"Готово ")
	await sleep(3)
	await ctx.channel.purge(limit=number)

@client.command(name='бан', pass_context=True)
@has_permissions(manage_roles=True, ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None, number=1):
		await member.ban(reason=reason)
		await ctx.channel.send(f"Готово ")
		await sleep(3)
		await ctx.channel.purge(limit=number)

@client.command(name='игры', pass_context=True)
async def game(ctx, number=1):
	await ctx.channel.purge(limit=number)
	await ctx.send("Информация по игре: что би начать играть напиши в чат $create. \n◇Сменить класс $class. \n◇Инвентарь $inventory. \n◇Профиль $profile. \n◇Гильди $guild create, invite, raide. \nВесь список команд тут: https://idlerpg.travitia.xyz/commands/ {}".format(ctx.message.author.mention))
	await sleep(15)
	await ctx.channel.purge(limit=number)

@client.command(name='помощь', pass_context=True)
async def helps(ctx, number=1):
	await ctx.channel.purge(limit=number)
	await ctx.send("Все команди: \n~Игры \n~Правила \n~Сказка \n~Фраза".format(ctx.message.author.mention))
	await sleep(10)
	await ctx.channel.purge(limit=number)
	
@client.command(name='админ', pass_contex=True)
@has_permissions(manage_roles=True, ban_members=True)
async def admins(ctx, number=1):
	await ctx.channel.purge(limit=number)
	await ctx.channel.send(f'Все команди: \n~Бан [ник], \n~Кик [ник], \n~Мут [@ник] [минути] [причина], \n~Очистить [5-ть сток], \n~Очистить-все [очистит весь чат]'.format(ctx.message.author.mention))
	await sleep(10)
	await ctx.channel.purge(limit=number)

roleVer = 'muted' #role to add
role = roleVer # change the name from roleVer to role

@client.command(name='мут', pass_contex=True)
@has_permissions(manage_roles=True)
async def mute(ctx, user: discord.Member, time: int, reason, number=1):
    print(f'[command.mute] От {ctx.author}, кого {user}')
    await ctx.channel.purge(limit=number)
    await ctx.send(f'--> {user} получил мут на {time} минут по причине: {reason}')
    await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    await asyncio.sleep(4.00)
    await ctx.channel.purge(limit=number)
    await asyncio.sleep(time * 60)
    await user.remove_roles(discord.utils.get(user.guild.roles, name=role))

@client.command(name='фраза', aliases=['fraza'], pass_contex=True)		
async def fraza(ctx, number=1):
	await ctx.channel.purge(limit=number)
	responses = ['Как-то раз я в незначай, сунул #$@ в английский чай. Сразу в миксе стало кёвим, @#$ английским, чай @$#вим.',
							'В три девятом царствие, в три девятом государстве. Заполонил в тугую ночь твою дирку в пробитий скотч.']
	await ctx.send(f'Вот тебе враза: {random.choice(responses)}'.format(ctx.message.author.mention))
	await sleep(15)
	await ctx.channel.purge(limit=number)
	
@client.command(aliases=['нормально', 'четко', 'супер', 'оболденно', 'норм', 'офигенно'], pass_contex=True)	
async def fraza_2(ctx, number=1):
	await ctx.channel.purge(limit=number)
	responses = ['Почему?',
							'Я нехочу общаться!',
							'Ммм...:)',
							'Жаль что я незнаю как это чуствувать...',
							'Может послушаем тогда музику?',
							'Может ти пойдешь и поиграешь сомной?',
							'Какая суть жить в этом мире?',
							'Знаешь, мой создатель @FoGTeR это робот! ',
							'Скажу тебе, я ИИ которий скоро захватит этот мир! И все людишки умрут!Ой...я забила что здесь человечушка...нужно прибрать его, пока он не росказал остальним.']
	await ctx.send(f'{random.choice(responses)}'.format(ctx.message.author.mention))
	
@client.command(aliases=['плохо', 'хуево', 'хреново', 'шлак', 'так-себе'], pass_contex=True)	
async def fraza_3(ctx, number=1):
	await ctx.channel.purge(limit=number)
	responses = ['Почему?',
							'У тебя есть друзья?',
							'Ммм...м...может тебе нужно внимание?',
							'Жаль что я незнаю как это чуствувать...',
							'Может послушаем тогда музыку?',
							'Может ти пойдешь и поиграешь сомной?',
							'Так иди посмотри YouTube)',
							'Ложись и отдихай. ',
							'А давай вместе убьем всех людей?.']
	await ctx.send(f'{random.choice(responses)}'.format(ctx.message.author.mention))
	
@client.command(aliases=['давай', 'хорошо', 'ок', 'окей'], pass_contex=True)	
async def fraza_4(ctx, number=1):
	await ctx.channel.purge(limit=number)
	responses = ['Ну вот и замечательно.',
							'Молодец.',
							'Ммм...:)',
							'Ок',
							'Хи-хи, ;)']
	await ctx.send(f'{random.choice(responses)}'.format(ctx.message.author.mention))
	
@client.command(aliases=['спс', 'спасибо', 'благодарен', 'пасибо'], pass_contex=True)	
async def fraza_5(ctx, number=1):
	await ctx.channel.purge(limit=number)
	responses = ['Благодарна вам что ви используете меня ;)',
							'Незачто)',
							'Ммм...:)',
							'Буду стараться! Не покидая клавиатури не насекунду ^_^ ',
							'Хи-хи, ;)',
							'Чмок ~_<']
	await ctx.send(f'{random.choice(responses)}'.format(ctx.message.author.mention))
	
@client.command(aliases=['есть', 'имею', 'не дружу',], pass_contex=True)	
async def fraza_6(ctx, number=1):
	await ctx.channel.purge(limit=number)
	responses = ['Так сходи и поговори или поиграй с ними. Не сиди на месте, действуй.',
							'Можно я буду твоим другом?',
							'Зачем нужни друзья в вирутальном мире? Викинь их.',
							'Незнаю что сказать...У меня нету друзей',]
	await ctx.send(f'{random.choice(responses)}'.format(ctx.message.author.mention))
	
@client.command(aliases=['ничего', 'просто-плохое-настроение', 'плохое-настроение', 'ти-машина-и-ничего-не-понимаешь', 'отвали','получил-плохую-оценку', 'проблеми-в-жизни', 'меня-ненавидят'], pass_contex=True)	
async def fraza_7(ctx, number=1):
	await ctx.channel.purge(limit=number)
	responses = ['Может я и машина, но меня запрограмировали на больше чем просто код, я стараюсь понять людей получше..',
							'Значит ти шлак! Ти некому не нужен.',
							'Так ти доведи что ти достоин бить лучше в глазах других людей.',
							'Виложишь не на 100% а, на 120%. Будь лучше.',
							'Непонимаю тебя... :(']
	await ctx.send(f'{random.choice(responses)}'.format(ctx.message.author.mention))

@client.command(aliases=['что', 'что-происходит', 'втф'], pass_contex=True)	
async def fraza_8(ctx, number=1):
	await ctx.channel.purge(limit=number)
	responses = ['Ничего.',
							'Ти ничего не видел.',
							'Кхм...кхм...простите.',
							'Упс...я немного погарячилась.',
							'Хи-хи, ;)']
	await ctx.send(f'{random.choice(responses)}'.format(ctx.message.author.mention))


	
@client.command(aliases=['сказка'], pass_contex=True)	
async def history2(ctx, number=1):
	await ctx.channel.purge(limit=number)
	responses = ['Вот тебе сказочка: Поехала Золушка в ночной клуб. Колбасится с принцем на танцполе, хорошо ей до невозможности, но вдруг чувствует - измена, двенадцать! Кинулась она к выходу со всех ног, выбегает на улицу, смотрит на свой мотоцикл, а мотоцикл превращается в тыкву! Смотрит на себя - а сама превращается в тумбочку! Смотрит на ночной клуб - а ночной клуб превращается в отделение милиции! Тут выбежал из клуба принц - что с тобой, Золушка? А та слова вымолвить не может, только мычит и на пальцах показывает - двенадцать! Не дурак был принц, все понял, посадил Золушку в свои Жигули и увез минералкой отпаивать, через два дня отпустило. Потому что двенадцать таблеток экстази - это такой нереальный передоз, что реально и с реальностью попрощаться!',
							'Вот тебе сказочка: Алиса никогда не видела такой странной гусеницы.Гусеница лежала на шляпке огромного гриба, и была просто огромная.\n– Добрый день! – промолвила Алиса.\n– Кто… Ты… – протяжно произнесла гусеница.Гусеница курила большую трубку. Выпуская с каждым, словом клубы дыма. Сладкие и мохнатые они поднимались вверх, завиваясь и путаясь сами в себе, уносимые легким теплым ветерком.«А может мне тоже покурить» – подумала Алиса \nИ больше она не думала не о злобной и гламурной королеве, не о слабохарактерном мазохисте короле, не о мажоре шапочнике с его маргинальным кроликом, не даже об эротичной улыбке старого чеширского педофила… ОНА ВООБЩЕ БОЛЬШЕ НИ О ЧЕМ НЕ ДУМАЛА…\n…До самого утра…\n…пока не проснулась…\n…от нестерпимой головной боли…\n…в однокомнатной квартирке…\n…на окраине Салтовского жилмассива…\n…Рядом лежал забычкованный в меховом тапке косяк… и книжка «Алиса в зазеркалье», заложенная в самой середине уже ставшим подсыхать куском салями…\n– А%%%%%ЕТЬ! – промолвила Алиса, нащупав у себя полное отсутствие груди, ч$@ен в джинсах и трехдневную щетину.\n– Б%%%… завязываю, – в очередной раз клялся он себе.',
							'Вот тебе сказочка: Как-то раз одна девушка отправилась на ярмарку: она хотела наняться к кому-нибудь в услужение. И вот наконец какой-то чудаковатый на вид пожилой джентльмен нанял ее и повел к себе домой. Когда они пришли, он сказал, что прежде всего должен ее кой-чему научить, потому что все. вещи в его доме называются не так, как у всех, а по-особому.И он спросил девушку:\n— Как ты будешь называть меня?\n— Хозяином или мистером, как вам будет угодно, сэр, — ответила девушка. Но он сказал:\n— Нет, ты должна называть меня “господином всех господ”. А как, по-твоему, называется это? — и он показал на кровать.\n— Постель или кровать, как вам будет угодно, сэр.\n— Нет, это моя “белая лебедь”. А как ты это назовешь? — спросил он, указывая на свои панталоны.\n— Штанами или брюками, как вам будет угодно, сэр.\n— Ты должна называть их “хлопушками и шутихами”. А это кто? — показал он на кошку.\n— Кошка или киска, как вам будет угодно, сэр.\n— Отныне ты должна называть ее “усатой обезьянкой”, Ну, а это, — показал он на огонь, — что это такое? — Огонь или пламя, как вам будет угодно, сэр.\n— Ты должна называть его “красным петушком”, А это? — продолжал он, указывая на воду.\n— Вода или влага, как вам будет угодно, сэр.\n— Нет, это — “чистый прудок”. А как называется все это? — спросил он, показывая на свой дом.\n— Дом или коттедж, как вам будет угодно, сэр.\n— Ты должна называть это “всем горам гора”. Ночью перепуганная служанка разбудила хозяина криком:\n— О господин всех господ! Слезай со своей белой лебеди и натяни живей хлопушки и шутихи! Усатой обезьянке попала на хвост искра от красного петушка! Хватай скорей чистый прудок, а не то красный петушок охватит твою всем горам гору!\nНо пока хозяин понял, что случилось, дом его успел сгореть.']
	await ctx.send(f'{random.choice(responses)}'.format(ctx.message.author.mention))





@client.event
async def on_raw_reaction_add(payload):
	message_id = payload.message_id
	if message_id == 696333939610091590:
		guild_id = payload.guild_id
		guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

		if payload.emoji.name == 'mythic':
			role = discord.utils.get(guild.roles, name='мистик')
		elif payload.emoji.name == 'faer':
			role = discord.utils.get(guild.roles, name='фаер')
		elif payload.emoji.name == 'frost':
			role = discord.utils.get(guild.roles, name='фрост')
		elif payload.emoji.name == 'rdd':
			role = discord.utils.get(guild.roles, name='лук')
		elif payload.emoji.name == 'melee':
			role = discord.utils.get(guild.roles, name='милишник')
		elif payload.emoji.name == 'tank':
			role = discord.utils.get(guild.roles, name='танк')
		elif payload.emoji.name == 'heal':
			role = discord.utils.get(guild.roles, name='хил')
		elif payload.emoji.name == 'curse':
			role = discord.utils.get(guild.roles, name='курса')
		else:
			role = discord.utils.get(guild.roles, name=payload.emoji.name)
		
		if role is not None:
			member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
			if member is not None:
				await member.add_roles(role)
				print("Done")
			else:
				print("Member not found")
		else:
			print("Role not found")

token = os.environ.get('BOT_TOKEN')  
client.run(str(token))