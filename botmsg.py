import discord
import requests
from discord.ext import commands

client = discord.Client()



sad_words = ["triste", "depresivo", "infeliz", "enojado", "miserable"]

starter_encouragements = [
  "Arriba amigo!",
  "Chocala!",
  "NO te vas a morir virgen!"
]

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('Hemos iniciado sesion como {0.user}'.format(client))

@client.command(pass_context=True)
async def DM(ctx, user: discord.User, *, message=quota):
    
    await client.send_message(user, message)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if message.content.startswith('inspirame'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('$inspirar'):
        quote = get_quote()
        await message.author.send(quote)
    
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

client.run('ODA5MTUwMTg4MTU3NDAzMTM4.YCQ51g.ktuyTtb7pL5arYwL1xUxL0ybdSA')