#Please read it 
#커밋 풀 시 .env파일 추가 --> 토큰 값

# 모듈 가져오기
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# 봇 기본 설정

load_dotenv()
token = os.getenv("TOKEN") #토큰 값 가져오기

intents = discord.Intents.default()  # 기본 인텐트 설정
intents.members = True  # 서버 멤버 목록을 읽을 수 있는 인텐트 설정

client = discord.Client(intents=intents)

#client = commands.Bot(command_prefix='/') #봇 명령어가 / 으로 시작함
#///////////////////////////////////////////////////////////////////#

@client.event #로그인 확인
async def on_ready(): 
    print('im online')

@client.event #봇을 제외한 메시지에 반응하여 그렇군요 출력
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send("네")

#///////////////////////////////////////////////////////////////////#
client.run(token)