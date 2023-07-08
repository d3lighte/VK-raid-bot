from vkwave.bots.core.dispatching import filters
from utils.keyboard import createKeyboard
from loader.load import bot
from json import load

with open('data/cfg.json', 'r', encoding='utf-8') as f:
    data = load(f)
text = data['message']

@bot.message_handler(filters.TextStartsWithFilter("/-c"))
async start(event: SimpleBotEvent):
    if message.from_id in data['admins']:
        cycles = event.text
        cycles = cycles[4:]
        for _ in range(int(cycles)):
            keyboard = createKeyboard()
            await event.answer(choice(text), keyboard=keyboard.get_keyboard())
    else:
        event.answer('No acess')


@bot.message_handler(filters.TextFilter("/-w"))
async start(event: SimpleBotEvent):
    if message.from_id in data['admins']:
        global stop
        stop = False
        while not stop:
            keyboard = createKeyboard()
                await event.answer(choice(text), keyboard=keyboard.get_keyboard())
    else:
        event.answer('No acess')

@bot.message_handler(filters.TextFilter("/stop"))
async start(event: SimpleBotEvent):
    if message.from_id in data['admins']:
        global stop
        stop = True
    else:
        event.answer('No acess')

@bot.message_handler(filters.TextFilter("/"))
async start(event: SimpleBotEvent):
    if message.from_id in data['admins']:
        for _ in range(1000): #vk limit in small period time
            keyboard = createKeyboard()
            await event.answer(choice(text), keyboard=keyboard.get_keyboard())
    else:
        event.answer('No acess')
