import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import aiohttp
import string
import random
import datetime
import command
import openpyxl

const token = 

client = discord.Client()


@client.event
async def on_ready():
    print("[호동 BOT]의 동작 준비 중..")
    print("[호동 BOT]의 동작을 시작합니다.")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    game = discord.Game("hodong.py on client 3.5.4")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("호동"):
        await message.channel.send("[호동 BOT] 호동이 불러쪄?")
        await message.channel.send(file = '호동.png')

    if message.content.startswith("!discord creative mode"):
        await message.channel.send("[호동 BOT] 'Discord' 서버에 연결 중 입니다.")
        await message.channel.send("[호동 BOT] 'Discord' 서버에 연결 완료됨.")
        await message.channel.send("모듈 실행 완료:: Creative Mode::")
        await message.channel.send("[호동 BOT] 개발자 모드가 활성화되었습니다.")

    if message.content.startswith("!screen"):
        await message.channel.send("[호동 BOT] 'Discord' 서버와 연결 중 입니다.")
        await message.channel.send("[호동 BOT] 'Discord' 서버에 연결 완료됨.")
        await message.channel.send("https://discordapp.com/channels/421646618140606474/600308081813094400")

    if message.content.startswith("!server"):
        await message.channel.send("[호동 BOT] Finding..")
        await message.channel.send("[호동 BOT] Finding..")
        await message.channel.send("[호동 BOT] Finding..")
        await message.channel.send("[호동 BOT] SERVER LIST:")
        file = open("serverlist.txt")
        await message.channel.send(file.read())
        file.close()

    if message.content.startswith("!show error"):
        await message.channel.send("[호동 BOT] error code will show Thus On")

    if message.content.startswith("!check module all hodong/.py"):
        await message.channel.send("[호동 BOT] 'hodong/.py' 파일을 찾을 수 없습니다.")
        await message.channel.send("[호동 BOT] 사유: .py 의 확장명이 아니거나 파일이 존재하지 않습니다.")

    if message.content.startswith("!check module all hodong.py"):
        await message.channel.send("[호동 BOT] CHANGE - hodong ONLINE")
        await message.channel.send("모듈 점검 런처 한글화 파일 저작권은 벌판#4442 에게 있습니다. 2차 수정 및 무단배포를 금합니다.")
        await message.channel.send("모듈을 리로드 중.. 위치 - hodong.py")
        await message.channel.send("모듈 점검 런처를 시작하는 중..")
        await message.channel.send("[INFO] file found: 호동.png")
        await message.channel.send("[경고] 이미지를 불러 올 수 없음: 파일이 손상되거나 위치에 존재하지 않습니다.")
        await message.channel.send("[INFO] file registered: serverlist.txt")
        await message.channel.send("[INFO] module list: discord / discord.ext : commands / discord.ext.commands : Bot / asyncio / aiohttp / string / random / openpyx1 / datetime / command")
        await message.channel.send("[경고] 명령어 : !시간 - 5개의 함수가 발견 됨: a / b / c / d /e - str(d) GMT+9")
        await message.channel.send("[INFO] 명령어: screen - 'discord' 서버와 연결 값 : hodong5")
        await message.channel.send("Launcher Based on Python client 3.5.4")
        await message.channel.send("[INFO] 모듈 점검 런처 종료 중...")
        await message.channel.send("모듈 점검 런처 종료 메시지 확인 후 봇 배치파일을 껏다 켜주세요.")
        await message.channel.send("모듈 점검 런처 종료:: 발견에러: 116(s)")

    if message.content.startswith("!check log output"):
        await message.channel.send("[호동 BOT] CHANGE - hodong ONLINE")
        await message.channel.send("모듈 점검 런처 한글화 파일 저작권은 벌판#4442 에게 있습니다. 2차 수정 및 무단배포를 금합니다.")
        await message.channel.send("[호동 BOT] CHANGE - hodong ONLINE")
        await message.channel.send("[호동 BOT] Log Finding....")
        await message.channel.send("[호동 BOT] LOG saved Successfully./ C:Users$joon1$Desktop$Python / ")

    if message.content.startswith("!ignore permission reload"):
        await message.channel.send("[호동 BOT] 관리자 권한 확인 중..")
        await message.channel.send("[호동 BOT] RELOADING...")

    if message.content.startswith("!시간"):
        a = datetime.datetime.today().month
        b = datetime.datetime.today().day
        c = datetime.datetime.today().hour
        d = datetime.datetime.today().minute
        e = datetime.datetime.today().second
        await message.channel.send(str(a) + "월 " + str(b) + "일의 현재시간은 " + str(c) + "시 " + str(d) + "분 " + str(e) + "초 입니다. (Seoul, GMT +9) ")
        file = open("d-day.txt")
        await message.channel.send(file.read())
        file.close()

    if message.content.startswith("!sector2 시간"):
        a = datetime.datetime.today().month
        b = datetime.datetime.today().day
        c = datetime.datetime.today().hour
        d = datetime.datetime.today().minute
        e = datetime.datetime.today().second
        await message.channel.send(str(a) + "월 " + str(b) + "일의 현재시간은 " + str(c) + "시 " + str(d) + "분 " + str(e) + "초 입니다. (Seoul, GMT +9) ")
        file = open("d-day.txt")
        await message.channel.send(file.read())
        file.close()

    if message.content.startswith("!log delete"):
        await ctx.message.delete()
        await ctx.message.delete()
        await ctx.message.delete()
        await ctx.message.delete()
        await ctx.message.delete()

    if message.content.startswith("!remove all !d-list in- any - no"):
        await message.channel.send("[호동 BOT] 관리자 권한 확인 중..")
        await message.channel.send("[호동 BOT] 'd-list' 파일 작성 값 삭제 완료:: 1(s)")

    if message.content.startswith("!ad essential Member check"):
        file = open("file.txt")
        await message.channel.send(file.read())
        file.close()

    if message.content.startswith("!backup-all"):
        await message.channel.send("[호동 BOT] 관리자 권한 확인 중..")
        await message.channel.send("[호동 BOT] 관리자 권한이 없습니다. 필요권한: load failed..1000100101000101010111010")


    if message.content.startswith("!채금"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="채팅 금지")
        roles = discord.utils.get(message.guild.roles, name="Member")
        await author.add_roles(role)
        await author.remove_roles(roles)
        await message.channel.send("[호동 BOT] 해당 플레이어의 채팅이 비활성화 되었습니다.")

    if message.content.startswith("!멤버"):
        await message.channel.send("[호동 BOT] 관리자 권한 확인 중..")
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="채팅 금지")
        roles = discord.utils.get(message.guild.roles, name="Member")
        await author.add_roles(roles)
        await author.remove_roles(role)

    if message.content.startswith("!경고"):
        author = message.guild.get_member(int(message.content[4:22]))
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        i = 1
        while True:
            if sheet ["A" + str(i)].value == str(author.id):
                sheet ["B" + str(i)].value = int(sheet ["B" + str(i)].value) + 1
                file.save("경고.xlsx")
                if sheet ["B" + str(i)].value == 3:
                    await message.guild.ban(author)
                    await message.channel.send("경고 3회 누적, 해당 플레이어가 추방되었습니다.")
                else:
                    await message.channel.send("경고 1회 누적됨.")
                break
            if sheet ["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(author.id)
                sheet["B" + str(i)].value = 1
                file.save("경고.xlsx")
                await message.channel.send("경고 1회 누적됨.")
                break
            i += 1



client.run('NTUxNDAwMjMzOTk3Njk3MDI2.XvbM5g.3D4cuseUIPuyXZJdskVKpaJbNyo')
