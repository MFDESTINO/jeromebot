from io import BytesIO
from facebook import GraphAPI
from PIL import Image, ImageDraw, ImageFont
from jerometoken import token
import requests
import json


class JeromeBot():
    def __init__(self):
        self.graph = GraphAPI(access_token=token)

    def img_to_file(self, img):
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format='PNG')
        return(img_byte_arr.getvalue())

    def post_image(self, img, description):
        img_file = self.img_to_file(img)
        return self.graph.put_photo(image=img_file, message=description)

    def get_dolar(self):
        req = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
        return req.json()['USD']['bid'][:4]

    def make_image(self, font, src_img, msgs):
        FONT = ImageFont.truetype(font, 60)
        base = Image.open(src_img).convert('RGBA')
        txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
        d = ImageDraw.Draw(txt)
        for msg in msgs:
            d.text(msg['pos'], msg['msg'], font=FONT, fill=msg['color'])
        return Image.alpha_composite(base, txt)
