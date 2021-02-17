# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:41:48 2021

@author: Traftmine
"""
import time
import pyautogui

START = time.time()
time.sleep(5)
SCRIPT = open("beescript.txt", 'r')
for word in SCRIPT:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
SCRIPT.close()
END = time.time()
print("The spam last for", round(END-START, 2), "secondes")
