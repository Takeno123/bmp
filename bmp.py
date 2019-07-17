# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 13:34:38 2019

@author: 15t50
"""

from PIL import Image
import json
            
def test(pixels,paint_data):
    reverse = paint_data.pop("reverse")
    for paint in paint_data:
        for i in range(paint_data[paint]["line"]):
            for j in range(paint_data[paint]["column"]):
                for k in range(paint_data[paint]["width"]):
                    for l in range(paint_data[paint]["height"]):
                        target_x = paint_data[paint]["coordinate"][0]+j*(paint_data[paint]["horizontal_spacing"]+paint_data[paint]["width"])+k
                        target_y = paint_data[paint]["coordinate"][1]+i*(paint_data[paint]["vertical_spacing"]+paint_data[paint]["height"])+l
                        pixels[target_x,target_y] = paint_data[paint]["brightness"],paint_data[paint]["brightness"],paint_data[paint]["brightness"]
    
    if reverse == 1:
        for k in range(1024):
            for l in range(768):
                relay = 255 - (pixels[k,l][0])
                pixels[k,l] = relay,relay,relay
                
    return pixels
                    

img = Image.new('RGB',(1024,768),"black")
pixels = img.load()

with open('jsonFile.json', 'r') as f:
    paint_data = json.load(f) 
    print(paint_data)

pixels=test(pixels,paint_data)

print(paint_data)

img.save("gomi.bmp")