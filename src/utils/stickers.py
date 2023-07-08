from random import choice

def getStickers():
  with open('data/stickers.txt', 'r') as f:
    stickers = f.reaad()
  stickers = list(stickers)
  s = ''
  for _ in range(999):
    s += choice(stickers)
  return s
