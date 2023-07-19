# 모듈 가져오기
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# 봇 기본 설정

load_dotenv()

token = os.getenv("TOKEN") #토큰 값 가져오기

bot = commands.Bot(command_prefix='/') #봇 명령어가 / 으로 시작함
bot.run(token)