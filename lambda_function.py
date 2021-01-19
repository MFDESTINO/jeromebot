#!/usr/bin/env python3
from random import choice
from datetime import datetime
from jeromebot import JeromeBot
import json
import os

src_dir = 'src'
font_file = os.path.join(src_dir, 'FreeSansBold.otf')
jerome1_file = os.path.join(src_dir, 'jerome1.jpg')
jerome2_file = os.path.join(src_dir, 'jerome2.jpg')
jerome3_file = os.path.join(src_dir, 'jerome3.jpg')
jerome4_file = os.path.join(src_dir, 'jerome4.jpg')
jerome5_file = os.path.join(src_dir, 'jerome5.jpg')

def lambda_handler(event, context):
    jeromebot = JeromeBot()
    dolar = 'me passa ' + jeromebot.get_dolar() + ' real brasileiro'

    jerome = choice(['jerome1', 'jerome2', 'jerome3', 'jerome4', 'jerome5'])
    if jerome == 'jerome1':
        msgs = [{'msg': 'ei carinha que mora logo ali', 'pos': (240, 30), 'color':'yellow'},
                {'msg': dolar, 'pos': (400, 600), 'color': 'yellow'}]
        src_file = jerome1_file

    if jerome == "jerome2":
        msgs = [{'msg': 'ei carinha que mora logo ali', 'pos': (200, 50), 'color': '#e3c520'},
                {'msg': dolar, 'pos': (300, 600), 'color': 'e3c520'}]
        src_file = jerome2_file

    if jerome == "jerome3":
        msgs = [{'msg': 'ei carinha que mora logo ali', 'pos': (150, 50), 'color': '#f5d10c'},
                {'msg': dolar, 'pos': (200, 550), 'color': '#f5d10c'}]
        src_file = jerome3_file

    if jerome == "jerome4":
        msgs = [{'msg': 'ei carinha que mora logo ali', 'pos': (450, 10), 'color': '#fff'},
                {'msg': dolar, 'pos': (150, 650), 'color': '#fff'}]
        src_file = jerome4_file

    if jerome == "jerome5":
        msgs = [{'msg': 'ei carinha que mora logo ali', 'pos': (400, 10), 'color': '#e3c520'},
                {'msg': dolar, 'pos': (300, 600), 'color': '#e3c520'}]
        src_file = jerome5_file
        
    img = jeromebot.make_image(font_file, src_file, msgs)
    current_time = datetime.now().strftime("%d/%m/%y")
    description = ["cotação gerada em " + current_time, '#jeromebot5000']

    postid = jeromebot.post_image(img, description)
    return {
            'statusCode': 200,
            'body': json.dumps(postid)
            }

