import pyautogui
import cv2
import numpy as np

resolution = (720,1080)                                           #resolution

codec = cv2.VideoWriter_fourcc(*'XVID')                           #codec

filename = 'screencapp.avi'                                        #name

fps = 60                                                           #specify the fps

out = cv2.VideoWriter(filename,codec,fps,resolution)       #object

cv2.namedWindow('Live',cv2.WINDOW_NORMAL)                         #EMT window
 
cv2.resizeWindow('Live',500,500)                                  #window size

while True:
    img=pyautogui.screeshot()                                     #screen shot using pygui

    frame= np.array(img)                                           #convet into np arry

    frame =cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2RGB )            # CONVERTING RGB

    out.write(frame)                                             #OUTPUT

    cv2.imshow('Live',frame)                                      #farme diapaly

    if cv2.waitKey(1000) == ord('q'):                                #end 
    
     break

out.release()
cv2.destroyAllWindows
