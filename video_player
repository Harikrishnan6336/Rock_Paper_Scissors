import cv2 
import numpy as np 
   
# Create a VideoCapture object and read from input file 
cap = cv2.VideoCapture('Cruel Angels Thesis [360p].mp4')
   
# Check if camera opened successfully 
if (cap.isOpened()== False):  
  print("Error opening video  file") 
cv2.namedWindow('Frame', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
# Read until video is completed 
while(cap.isOpened()): 
      
  # Capture frame-by-frame 
  ret, frame = cap.read() 
  if ret == True: 
   
    # Display the resulting frame 
    cv2.imshow('Frame', frame)
    #cv2.resizeWindow('Frame',1000,500) 
   
    # Press Q on keyboard to  exit 
    if cv2.waitKey(25) & 0xFF == ord('q'): 
      break
   
  # Break the loop 
  else:  
    break
   
# When everything done, release  
# the video capture object 
cap.release() 
   
# Closes all the frames 
cv2.destroyAllWindows()
