from vkwave.bots import SimpleLongPollBot
from json import load

with open('data/cfg.json', 'r', encoding='utf-8')
    data = load(f)

bot = SimpleLongPollBot(tokens=data['token'], group_id=data['idgr'])
