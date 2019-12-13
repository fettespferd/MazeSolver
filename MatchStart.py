from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from Graph import Graph

img_maze = cv2.imread('C:\\Users\\faube\\Desktop\\Python\\Data\\demo.png')
    
    #Detect Start and Finish

def findstart():
    global startpoint

    hsv_image = cv2.cvtColor(img_maze, cv2.COLOR_BGR2HSV)
  
   # define range of red color in HSV
    lower_red = np.array([0,100,100])
    upper_red = np.array([50,255,255])
   
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv_image, lower_red, upper_red)
    
    #cv2.imshow('Mask',mask)
    #cv2.waitKey(0)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(hsv_image,hsv_image, mask= mask)
    cimg=res
    res=cv2.cvtColor(res, cv2.COLOR_RGB2GRAY)


    circles = cv2.HoughCircles(res,cv2.HOUGH_GRADIENT,1,1,param1=50,param2=10,minRadius=0,maxRadius=0)
    #circles = np.uint16(np.around(circles))

    for i in circles[0,:]:
    # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(255,0,0),2)
     # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
        startpoint = (i[0],i[1])
    #print(startpoint)
    #cv2.imshow('Detected Start circles',cimg)
    #cv2.waitKey(0)
    return startpoint

def findend():
    global endpoint

    hsv_image = cv2.cvtColor(img_maze, cv2.COLOR_BGR2HSV)
  
   # define range of red color in HSV
    lower_green = np.array([60,100,100])
    upper_green = np.array([135,255,255])
   
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv_image, lower_green, upper_green)
    

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(hsv_image,hsv_image, mask= mask)
    cimg=res
    res=cv2.cvtColor(res, cv2.COLOR_RGB2GRAY)

    circles = cv2.HoughCircles(res,cv2.HOUGH_GRADIENT,1,30,param1=50,param2=10,minRadius=0,maxRadius=0)
    #circles = np.uint16(np.around(circles))

    for i in circles[0,:]:
    # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(255,0,0),2)
     # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
        endpoint = (i[0],i[1])
    #print(endpoint)
    #cv2.imshow('Detected End circles',cimg)
    #cv2.waitKey(0)
    return endpoint
