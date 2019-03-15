import discord
import dyn_import

cogs = dyn_import.cogs
cog_events = dyn_import.cog_events
if 'logger' in cogs:
    cogs['logger'].init()

if 'config' in cogs:
    config = cogs['config'].ConfigFileIO('abnormal_config.cfg')
    config.init_setup()
    
    TOKEN = config.read('CONFIG','token')
    if not TOKEN:
        print("Couldn't get token from config file")
        TOKEN = input('Enter your token\n')
        
    BOT = config.read('CONFIG','bot')
    if not BOT:
        BOT = True
    else:
        BOT = bool(BOT)

#print('Token: '+str(TOKEN))
#print('Bot: '+str(BOT))


client = discord.Client()


print('Starting...')

@client.event
async def on_ready():
    if "on_ready" in cog_events:
        cog_events["on_ready"].on_ready(client)
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "on_message" in cog_events:
        cog_events["on_message"].on_message(client)

    if message.channel.id != 477269419765006345:
        return
    
    await message.channel.send(message.content)

client.run(TOKEN, bot=BOT)
