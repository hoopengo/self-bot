import time
import discord
from random import choice
from discord.ext import commands, tasks
from pypresence import Presence
from sapper import generate_minesweeper_board

# Constants
STATES = ['Он делает это уже давно!', 'Играем до победного!']
DETAILS = ["Разрабатывает интересное", "Изучает что-то новое"]
BTNS = [
    {
        "label": "GitHub",
        "url": "https://github.com/{nickname}",
    }
]
BOT_PREFIX = ".me"

# Bot initialization
bot = commands.Bot(
    command_prefix=BOT_PREFIX,
    self_bot=True,
    intents=discord.Intents.all()
)

# Command definitions
@bot.command()
async def sapper(ctx: commands.Context):
    await ctx.message.edit(content=generate_minesweeper_board())

# Presence loop
@tasks.loop(seconds=15)
def update_presence_loop():
    presence = Presence(client_id=client_id)
    presence.connect()
    presence.update(
        state=choice(STATES),
        details=choice(DETAILS),
        large_text='Python/Go',
        small_text='Программист',
        large_image="pigs",
        small_image="min",
        start=time(),
        buttons=BTNS
    )

# Event handlers
@bot.event
async def on_ready():
    print('ready')

# Main function
def main():
    bot.run(token)
    update_presence_loop.start()

if __name__ == '__main__':
    main()
