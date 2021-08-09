from pyautogui import *
import pyautogui
import time
import threading
import random
import win32api, win32con
import keyboard

pointx = 0
pointy = 0
fx = 0
fy = 0
#pyinstaller --hidden-import "pynput.keyboard._win32" --hidden-import "pynput.mouse._win32" maplestory.py
#MAKE SURE NO WINDOWS ARE OPEN IN MAPLE (NO EQUIP TAB, NO INVENTORY)
#******MAKE SURE ITEM YOU ARE STARFORCING IS IN THE FIRST SLOT OF YOUR INVENTORY)
#MAKE SURE FREDERICK, STARFORCE UI, SWORDIE WINDOW NAME, ONSCREEN KB IS *NOT* BLOCKED
#Q TO EXIT


def sequenceligma():
        frederick()
        global pointx
        global pointy
        
        pyautogui.moveTo(pointx, pointy)
        pyautogui.mouseDown()
        time.sleep(0.02) 
        pyautogui.mouseUp()
        time.sleep(1)
    
        pyautogui.moveTo(fx,fy)
        pyautogui.mouseDown()
        time.sleep(0.02) 
        pyautogui.mouseUp()
        time.sleep(1)

        pyautogui.moveTo('restoretraced.png')
        pyautogui.mouseDown()
        time.sleep(0.02) 
        pyautogui.mouseUp()
        time.sleep(1)

        pyautogui.moveTo(pointx, pointy)
        pyautogui.mouseDown()
        time.sleep(0.02) 
        pyautogui.mouseUp()
        time.sleep(1)

        pyautogui.moveTo(pointx, pointy)
        pyautogui.mouseDown()
        time.sleep(0.02) 
        pyautogui.mouseUp()
        time.sleep(1)

        pyautogui.moveTo('starforcetab.png')
        pyautogui.mouseDown()
        time.sleep(0.02) 
        pyautogui.mouseUp()
        time.sleep(1)

        pyautogui.moveTo(fx,fy)
        pyautogui.mouseDown()
        time.sleep(0.02) 
        pyautogui.mouseUp()
        time.sleep(1)

        pyautogui.moveTo('enhance.png')
        pyautogui.mouseDown()
        time.sleep(0.02) 
        pyautogui.mouseUp()
        time.sleep(1)
        
        pyautogui.moveTo(pointx, pointy)
        pyautogui.mouseDown()
        time.sleep(0.02) 
        pyautogui.mouseUp()
        time.sleep(1)
        
        pyautogui.moveTo(pointx, pointy)
        pyautogui.mouseDown()
        time.sleep(0.02) 
        pyautogui.mouseUp()    

a = input("Enter to start: ")

def findy():
    global pointx
    global pointy
    ylocation = pyautogui.locateOnScreen('yfind.png')
    pointx = ylocation.left + ylocation.width + 5
    pointy = ylocation.top + ylocation.height + 5
    sw = pyautogui.locateOnScreen('swordiewindow.png')
    pyautogui.moveTo(sw.left+ 20, sw.top + 40)
    pyautogui.mouseDown()
    time.sleep(0.02) 
    pyautogui.mouseUp()

def frederick():
    global fx
    global fy
    tempvar = pyautogui.locateOnScreen('frederick.png')
    fx = tempvar.left + 15
    fy = tempvar.top - 10


findy()
#focus window lol

while True:
    #stop chainy
    if keyboard.is_pressed("q"):
        break
    
    if pyautogui.locateOnScreen('boomed.png', confidence = 0.9) != None:
        sequenceligma()
    else:
        #click 'y' (position y on screen button over auto click)
        if pyautogui.locateOnScreen('22star.png') != None:
            print("can see")
            sys.exit()
        else:
            print('cannot see')

        pyautogui.moveTo(pointx, pointy)
        pyautogui.mouseDown()
        time.sleep(0.02) 
        pyautogui.mouseUp()
        time.sleep(0.2)
        print("starforcing")
    
k = input("Enter to exit: ")



    

