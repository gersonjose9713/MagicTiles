from mss import mss
import cv2
import numpy as np
import win32gui
from keys import PressKey,ReleaseKey

def focusWindow(title):
    handle = win32gui.FindWindow(None, title)
    if handle != 0:
        win32gui.SetForegroundWindow(handle)

def teclado(img):
  loc1,loc2,loc3,loc4 = 50,175,290,415
  y = 100
  pixel1,pixel2,pixel3,pixel4 = img[y,loc1],img[y,loc2],img[y,loc3],img[y,loc4]
  A = 0x1E
  S = 0x1F
  D = 0x20
  F = 0x21

  
  #print(pixel1)
  #img2 = cv2.rectangle(img,(loc3,90),(loc4,110),(0,0,255),2)
  #cv2.imshow('Vision', img2)
  
  if pixel1 < 50 or pixel1 == 0:
    PressKey(A)
    ReleaseKey(A)

  if pixel2 < 50 or pixel2 == 0:
    PressKey(S)
    ReleaseKey(S)

  if pixel3 < 50 or pixel3 == 0:
    PressKey(D)
    ReleaseKey(D)

  if pixel4 < 50 or pixel4 == 0:
    PressKey(F)
    ReleaseKey(F)
  





def tela():
  #start_time = time.time() 
  sct_img = sct.grab(monitor)
  img = np.array(sct_img)
  img_gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
  teclado(img_gray)
  #cv2.imshow('Vision', img_gray)
  #print("FPS: ", 1.0 / (time.time() - start_time))
  

monitor = {'top': 540, 'left':490, 'width':460, 'height':200}
sct = mss()
print('Starting')
focusWindow("LDPlayer")

while True:
  tela()
  if cv2.waitKey(25) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
    break
