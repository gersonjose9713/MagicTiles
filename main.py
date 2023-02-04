import mss
import cv2
import numpy as np
import win32gui
from keys import PressKey,ReleaseKey
import keyboard
import time

loc1,loc2,loc3,loc4 = 55,170,285,400
y = 95
A = 0x1E
S = 0x1F
D = 0x20
F = 0x21

with mss.mss() as sct:
  monitor = {'top': 540, 'left':490, 'width':460, 'height':200}

def focusWindow(title):
    handle = win32gui.FindWindow(None, title)
    if handle != 0:
        win32gui.SetForegroundWindow(handle)

def teclado(img):
  pixel1,pixel2,pixel3,pixel4 = img[y,loc1],img[y,loc2],img[y,loc3],img[y,loc4]

  if pixel1[0] < 50 or pixel1[0] == 0:
    PressKey(A)
    ReleaseKey(A)

  if pixel2[0] < 50 or pixel2[0] == 0:
    PressKey(S)
    ReleaseKey(S)

  if pixel3[0] < 50 or pixel3[0] == 0:
    PressKey(D)
    ReleaseKey(D)

  if pixel4[0] < 50 or pixel4[0] == 0:
    PressKey(F)
    ReleaseKey(F)
  
def tela():
  #start_time = time.time() 
  img = np.array(sct.grab(monitor))
  teclado(img)
  #cv2.imshow('Vision', img)
  #print("FPS: ", 1.0 / (time.time() - start_time))
  
print('Starting')
focusWindow("LDPlayer")

while True:
  tela()
  if cv2.waitKey(1) & keyboard.is_pressed('q'):
    cv2.destroyAllWindows()
    break
