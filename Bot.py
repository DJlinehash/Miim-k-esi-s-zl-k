import discord
import asyncio
import random

# İntentleri belirleyelim
intents = discord.Intents.default()
intents.message_content = True

# Client oluşturuyoruz
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

    while True:
        activity1 = discord.Game(name="Shadow_387 Yapımcım ")
        await client.change_presence(activity=activity1)
        await asyncio.sleep(3)  # 10 saniye bekle

        activity2 = discord.Game(name="ad:shadow387ayaz")
        await client.change_presence(activity=activity2)
        await asyncio.sleep(3)  # 10 saniye bekle

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('S$Merhaba'):
        await message.channel.send("Selam!")
    
    elif message.content.startswith('S$Baybay'):
        await message.channel.send("Bay bay")


    elif message.content.startswith('S$Yardım'):
        await message.channel.send("Komutlar: S$Baybay S$Merhaba S$Hakkımda S$Sunucu-Sahibi-Shadow387 S$Çalıştırma S$Paranıçaldım S$Domati S$Şaşır S$Zamanlayıcı30 S$Çekiliş S$RastgeleKullanıcı S$Kick S$Oylama S$TaşKağıtMakas S$AdamAsmaca S$Tahmin S$Motivasyon    BAZI KOMUTLAR ÇALIŞMIYOR.")
        

    elif message.content.startswith('S$Hakkımda'):
        await message.channel.send("Ben shadow387ayaz Tarafından yapıldım. Yapımcımın Kankası Yusuf Barandır.")

    elif message.content.startswith('S$Sunucu-Sahibi-Shadow387'):
        await message.channel.send("shadow387ayaz ve Katılmak İçin: https://discord.gg/3pmnmRpqyE")

    elif message.content.startswith('S$Çalıştırma'):
        await message.channel.send("https://www.youtube.com/shorts/6naK5GW0XVA Lan çalıştırma dedim İfşa oldum şimdi :/") 

    elif message.content.startswith('S$Paranıçaldım'):
        await message.channel.send("NEE")

    elif message.content.startswith('S$Domati'):
        await message.channel.send("DOMATİ AŞİRETİNİN BAŞLAMA TARİHİ 2022 NASIL BAŞLADI? SERVİSTE -Shadow387-") 

    elif message.content.startswith('S$Şaşır'):
        await message.channel.send("Şaşırmicam XD")

  client.run("TOKEN")
