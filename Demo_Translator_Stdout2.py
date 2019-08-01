#!/usr/bin/env python

# -*- coding: utf-8 -*-
#!/usr/bin/python3

from BinarySearchTree import BinarySearchTree
from AVLTree import AVLTree
from datetime import datetime
from SpellChecker import SpellChecker
from Result import Result

from random import randint
from Translator import Translator1
from Translator import Translator2
import arabic_reshaper


import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

"""
    Demo program that reroutes stdout and stderr.
    Type something in the input box and click Print
    Whatever you typed is "printed" using a standard print statement
    Use the Output Element in your window layout to reroute stdout
    You will see the output of the print in the Output Element in the center of the window
    
"""


layout = [
            [sg.Text('Type something in input field and click print')],
            [sg.In(size=(50, 1))],
            [sg.Output(size=(50, 5))],
            [sg.Button('Translate')]
         ]

window = sg.Window('English-Arbic-Translator').Layout(layout)

T1 = Translator1()
T2 = Translator2()


while True:     # Event Loop
    event, values = window.Read()
    if event is None:
        break
    word1 = T1.TranslateSentense(values[0])
    word2 = T2.TranslateSentense(values[0])
    reshaped_text1 = arabic_reshaper.reshape(word1)
    reshaped_text2 = arabic_reshaper.reshape(word2)   
    print(reshaped_text1 +"or"+ reshaped_text2)
