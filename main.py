import discord
from secret import token
from nltk.chat.util import Chat, reflections
from inosuke_chatbot import pairs


client = discord.Client()
inosuke_chatbot = Chat(pairs, reflections)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$b '):
        msg = message.content[3:len(message.content)]
        res = inosuke_chatbot.respond(msg)
        await message.channel.send(message.author.mention + " " + res)

if __name__ == "__main__":
    client.run(token)
