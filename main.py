#!/usr/bin/env python3
from random import choice
from datetime import datetime
from jeromebot import JeromeBot
import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))
src_dir = os.path.join(os.path.dirname(sys.argv[0]), 'src')
font_file = os.path.join(src_dir, 'FreeSansBold.otf')
jerome1_file = os.path.join(src_dir, 'jerome1.jpg')
jerome2_file = os.path.join(src_dir, 'jerome2.jpg')
jerome3_file = os.path.join(src_dir, 'jerome3.jpg')
out_file = os.path.join(os.getcwd(), 'output.png')

jeromebot = JeromeBot(headless=True)

frase1 = "ei carinha que mora logo ali"
frase2 = "me passa " + jeromebot.get_dolar().lower()


jerome = choice(['jerome1', 'jerome2', 'jerome3'])
if jerome == 'jerome1':
    jeromebot.make_image(font_file, jerome1_file, frase1,
                         frase2, (240, 30), (400, 600), 'yellow', out_file)
if jerome == "jerome2":
    jeromebot.make_image(font_file, jerome2_file, frase1,
                         frase2, (200, 50), (300, 600), '#e3c520', out_file)
if jerome == "jerome3":
    jeromebot.make_image(font_file, jerome3_file, frase1,
                         frase2, (150, 50), (200, 550), '#f5d10c', out_file)

now = datetime.now()
current_time = now.strftime("%d/%m/%y %H:%M")
description = ["cotação gerada em " + current_time, '#jeromebot5000']

jeromebot.post_image(out_file, description)
print('sucess')
