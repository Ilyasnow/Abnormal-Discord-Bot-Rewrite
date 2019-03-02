import discord

client = discord.Client()
TOKEN = input('Enter your token\n')

print('Starting...')
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id != 477269419765006345:
        return
    
    await message.channel.send(message.contents)

client.run(TOKEN)
