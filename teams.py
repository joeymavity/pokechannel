import discord
import asyncio
import re

client = discord.Client()

badwords = {'shit', 'fuck', 'cunt', 'retarded', 'gay', 'fag'}

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_member_join(member):
    if member.name=="Sfelman":
        server = member.server
        for i in server.roles:
            if i.name == 'Sun':
                await client.add_roles(member, i)

@client.event
async def on_message(message):
    if message.channel.name == 'bot-spam':
        if message.content.startswith('!moon') or message.content.startswith('!Moon'):
            server = message.author.server
            for i in message.author.roles:
                if i.name == 'Sun':
                    await client.send_message(message.author, "You're already on team Sun!")
                    return
                elif i.name == 'Moon':
                    await client.send_message(message.author, "You're already on team Moon!")
                    return
            for i in server.roles:
                if i.name == 'Moon':
                    await client.add_roles(message.author, i)
            
        elif message.content.startswith('!sun') or message.content.startswith('!Sun'):
            server = message.author.server
            for i in message.author.roles:
                if i.name == 'Sun':
                    await client.send_message(message.author, "You're already on team Sun!")
                    return
                elif i.name == 'Moon':
                    await client.send_message(message.author, "You're already on team Moon!")
                    return
            for i in server.roles:
                if i.name == 'Sun':
                    await client.add_roles(message.author, i)
    if (message.content.find("!sun") >-1 or message.content.find("!Sun") >-1) and message.author.name=="Sfelman":
        await client.delete_message(message)
    for i in badwords:
        if i in message.content:
            await client.send_message(message.author, "Chill with the language")
            await client.delete_message(message)
        

client.run('Mjc5ODQ0MzYzMjY4NTIxOTg0.C4FXFQ.Egg9ktpljx8FrR6O5lMMBbJkTxs')
