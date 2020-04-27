from PIL import Image, ImageFont, ImageDraw
from requests_html import HTMLSession
from random import choice
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%d/%m/%y %H:%M")
print("cotação gerada em ", current_time)

MAX_WIDTH = 1280  # px
FONT_HEIGHT = 60
FONT = ImageFont.truetype("src/FreeSansBold.otf",FONT_HEIGHT)

def make_image(img_path, msg1, msg2, output_path, pos1, pos2, color):
    base = Image.open(img_path).convert('RGBA')
    txt = Image.new('RGBA', base.size, (255,255,255,0))
    d = ImageDraw.Draw(txt)

    d.text(pos1, msg1, font=FONT, fill=color)
    d.text(pos2, msg2, font=FONT, fill=color)

    out = Image.alpha_composite(base, txt)
    out.save(output_path)

def get_dolar():
    s = HTMLSession()
    r = s.get('https://www.google.com/search?q=dolar')
    raw = r.html.find("#knowledge-currency__updatable-data-column", first=True)
    cotacao = raw.text.split('\n')[1]
    return cotacao

print(get_dolar())

p2 = "ei carinha que mora logo ali"
phrase = "me passa " + get_dolar().lower()

jerome = choice(['jerome1', 'jerome2', 'jerome3'])
if jerome == 'jerome1':
    make_image("src/jerome1.jpg", phrase, p2, "teste.png", (400, 600), (240, 30), 'yellow')
if jerome == "jerome2":
    make_image("src/jerome2.jpg", phrase, p2, "teste.png", (300, 600), (200, 50), '#e3c520')
if jerome == "jerome3":
    make_image("src/jerome3.jpg", phrase, p2, "teste.png", (200, 550), (150, 50), '#f5d10c')
