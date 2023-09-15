#Please read it 
#커밋 풀 시 .env파일 추가 --> 토큰 값

# 모듈 가져오기
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# 봇 기본 설정

load_dotenv()
token = os.getenv("TOKEN") # .env 파일에서 토큰 값 가져오기

intents = discord.Intents.all()  # 기본 인텐트 설정
intents.members = True  # 서버 멤버 목록을 읽을 수 있는 인텐트 설정

bot = commands.Bot(command_prefix='!', intents=intents)

#///////////////////////////////////////////////////////////////////#

@bot.event #로그인 확인
async def on_ready(): 
    print('im online')

@bot.event 
async def on_message(message):
    if message.content == "안녕":
        await message.channel.send("안녕하쇼")
    await bot.process_commands(message)
        
@bot.command() # !hello 입력 시 hello 출력
async def hello(ctx):
    await ctx.send("Hello")

@bot.command() # !image + 사진파일 입력 시 이미지 링크 반환
async def image(ctx):
    print(ctx.message.attachments[0].url)
    await ctx.send("확인")
    return(ctx.message.attachments[0].url)



#///////////////////////////////////////////////////////////////////#
bot.run(token)