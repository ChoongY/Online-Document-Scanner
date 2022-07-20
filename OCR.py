import easyocr
import numpy as np

def textScanner(Image):
    reader = easyocr.Reader(['en'],gpu=False)
    result = reader.readtext(Image)
    text =''
    for results in result:
        text+=results[1] + ' '
    return text

    
##a = textScanner(r"D:\python file VSC\fyp\myImage0.jpg")
##print (a)