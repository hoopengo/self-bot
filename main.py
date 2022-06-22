from pypresence import Presence
from random import choice
from time import time
from config import client_id, gh_url, token
from discord.ext import commands, tasks
from sapper import generate

client = commands.Bot(command_prefix='me.', self_bot=True)

states = ['Он делает это уже давно..', 'Иногда мне кажется что пора прекратить..', 'L-l-let me die', 'so quick to die?', 'Зачееем она берёт..', 'Бог есть! Так алах сказал!']
details = ['Я гуль..', 'Смотрю pornhub..']

@client.event
async def on_ready():
    print('ready')
    
    presence.start()
    
@client.command()
async def rick(ctx: commands.Context):
    await ctx.message.edit(content='https://nextcord.gay/')
    
@client.command()
async def sapper(ctx: commands.Context):
    await ctx.message.edit(content=generate())

btns = [
    {
        "label": "GitHub",
        "url": gh_url,
    }
]

RPC = Presence(client_id=client_id)
RPC.connect()

@tasks.loop(seconds=15)
async def presence():
    RPC.update(
        state=choice(states),
        details=choice(details),
        large_text='Я жигуль..',
        small_text='1000-7',
        large_image="pigs",
        small_image="min",
        start=time()-85000,
        buttons=btns
    )

client.run(token)