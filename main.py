import discord
from secret import token

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$b '):
        await message.channel.send(message.author.mention + " Hi. I recieved you message")


if __name__ == "__main__":
    client.run(token)
