#-------------------------------------------------------------------------------
# Name:        Video_Cropper
# Purpose:      A OpenCV python program for cropping a fixed width window of a video,
#               The center location of the window has to be inputted through mouse click
# Author:      Saikat
#
# Created:     23-08-2018
# Copyright:   (c) Saikat 2018
# Licence:     MIT
#-------------------------------------------------------------------------------
import cv2
import numpy as np

#global variables
ix=-1
iy=-1

#mouse callback
def select_point(event, x, y, flags, param):
    global ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        ix=x
        iy=y

video = raw_input('Enter the video file name : ') #'F:\\1.mp4'
cap = cv2.VideoCapture(video)
# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")

cv2.namedWindow('image')
cv2.setMouseCallback('image', select_point)
roi_range=100 #size of the cropped window will be roi_range*2 x roi_range*2

first_frame=True;
flag=False;
# Read until video is completed, press q to quit
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  #cropped=frame[0:100,0:100]
  if first_frame & ret:
    while (ix==-1):
        cv2.imshow('image',frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
          flag=True
          break
    first_frame=False
  else:
    if ret == True:
        cropped=frame[iy-roi_range:iy+roi_range, ix-roi_range:ix+roi_range]        
        # Display the cropped frame
        cv2.imshow('image',cropped)
        # Press Q on keyboard to  exit
        if cv2.waitKey(100) & 0xFF == ord('q'):
          flag=True
      # Break the loop
    else:
        flag=True
  if flag:
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()