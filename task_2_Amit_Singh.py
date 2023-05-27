'''
*********************************************************************************
*
*        		===============================================
*           		        CYBORG OPENCV TASK 2
*        		===============================================
*
*
*********************************************************************************
'''

# Author Name:		Amit Singh
# Roll No:			122EI0404
# Filename:			task_2_Amit_Singh.py
# Functions:		detect_arena_parameters,
# 					[ Comma separated list of functions in this file ]


####################### IMPORT MODULES #######################
   ## You are free to make any changes in this section. ##
##############################################################
import cv2 as cv 
import numpy as np
##############################################################

def detect_arena_parameters(maze_image):
    arena_parameters = {}


    # maze_image=cv.imread('maze_0.png')
    # cv.imshow('image',img)

    #----- for detection of traffic lights
    upper_red=np.array([0,0,255],'uint8')
    lower_red=np.array([0,0,200],'uint8')
    mask=cv.inRange(maze_image,lower_red,upper_red)
    # cv.imshow('mask',mask)

    contours1,hierarchy1=cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    dict1={100:'A',200:'B',300:'C',400:'D',500:'E',600:'F',700:'G'}
    dict2={100:'1',200:'2',300:'3',400:'4',500:'5',600:'6',700:'7'}
    s=""
    for c in contours1:
        approx=cv.approxPolyDP(c,0.01*cv.arcLength(c,True),True)
        if len(approx)==4:
            x,y,w,h=cv.boundingRect(c)
            
            s =s+ dict1[x+6]+dict2[y+6]+" "
        
    l=s.split()
    l.sort()



    # -------for detection of start node
    upper_green=np.array([0,255,0],'uint8')
    lower_green=np.array([0,200,0],'uint8')
    mask1=cv.inRange(maze_image,lower_green,upper_green)
    # cv.imshow('mask1',mask1)
    contours1,hierarchy1=cv.findContours(mask1,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
    a=''
    for c in contours1:
        approx=cv.approxPolyDP(c,0.01*cv.arcLength(c,True),True)
        if len(approx)==4 :
            x1,y1,w1,h1=cv.boundingRect(c)
            if w1==13:

                a = a + dict1[x1+6]+dict2[y1+6]+" "
        
    q=a.split()



    #-------for detection of medical shops and medicines

    s1=[0,100,200,300,400,500]
    list = []
    for i in s1:
    # for Shop_1 

    # for i in s1:
        # print(i)
        # Shop_1=img[110+i:190+i,110:190]
        Shop_1=maze_image[110:190,110+i:190+i]
    # cv.imshow('shop',Shop_1)
    # cv.waitKey(2)
        gray=cv.cvtColor(Shop_1,cv.COLOR_BGR2GRAY)
    # cv.imshow('gray',gray)
        adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,5)
    # cv.imshow("adaptivethresholding",adaptive_thresh)

        contours2,hierarchy2=cv.findContours(adaptive_thresh,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    #note




        if len(contours2)==0:
            pass
    
        else:

            for c in contours2:
        

                approx=cv.approxPolyDP(c,0.01*cv.arcLength(c,True),True)
                if len(approx)==4 :

                        x2,y2,w2,h2=cv.boundingRect(c)
                        # print((x2,y2,w2))
                        if w2==21:
                            
                            (b,g,r)=maze_image[y2+120,x2+120+i]
                            l1=(b,g,r)
                            # print(l1)

                            if l1==(255,255,0):
                    
                                    u1=[f'Shop_{(i//100)+1}','Skyblue','Square',[x2+120+i,y2+120]]
                                    # print(u1)
                                    list.append(u1)
                                    # print(list)


                            elif l1==(180,0,255):
                                    u2=[f'Shop_{(i//100)+1}','Pink','Square',[x2+120+i,y2+120]]
                                    list.append(u2)


                            elif l1==(0,127,255):
                                    u3=[f'Shop_{(i//100)+1}','Orange','Square',[x2+120+i,y2+120]]
                                    list.append(u3)
                
                            elif l1==(0,255,0):
                                    u4=[f'Shop_{(i//100)+1}','Green','Square',[x2+120+i,y2+120]]

                                    list.append(u4)


                elif len(approx)==3:
            # print(len(approx))
                            M=cv.moments(c)
                            cX=int(M['m10']/M['m00'])
                            cY=int(M['m01']/M['m00'])
                            (b,g,r)=maze_image[cY+110,cX+110+i]
                            l1=(b,g,r)
                # print(l1)
                
                            if l1==(255,255,0):
                    
                                u5=[f'Shop_{(i//100)+1}','Skyblue','Triangle',[cX+110+i,cY+111]]
                                list.append(u5)

                            elif l1==(180,0,255):
                                u6=[f'Shop_{(i//100)+1}','Pink','Triangle',[cX+110+i,cY+111]]
                                list.append(u6)
                            elif l1==(0,127,255):
                                u7=[f'Shop_{(i//100)+1}','Orange','Triangle',[cX+110+i,cY+111]]
                                list.append(u7)
                
                            elif l1==(0,255,0):
                                u8=[f'Shop_{(i//100)+1}','Green','Triangle',[cX+110+i,cY+111]]
                                list.append(u8)

        
                else:
        # cv.imshow("adaptive_thresh",adaptive_thresh)

                            (x, y), radius = cv.minEnclosingCircle(c)
                            center = (int(x), int(y))
                            radius = int(radius)
        # print((cX+110,cY+110))
                            (b,g,r)=maze_image[int(y)+110,int(x)+110+i]
                            l1=(b,g,r)

        
                            if l1==(255,255,0):

                                u9=[f'Shop_{(i//100)+1}','Skyblue','Circle',[int(x)+110+i,int(y)+110]]
                                list.append(u9)

                            elif l1==(180,0,255):
                                u10=[f'Shop_{(i//100)+1}','Pink','Circle',[int(x)+110+i,int(y)+110]]
                                list.append(u10)


                            elif  l1==(0,127,255):
                                u11=[f'Shop_{(i//100)+1}','Orange','Circle',[int(x)+110+i,int(y)+110]]
                                list.append(u11)


                
                            elif l1==(0,255,0):
                                u12=[f'Shop_{(i//100)+1}','Green','Circle',[int(x)+110+i,int(y)+110]]
                                list.append(u12)
                                    # print(len(contours2))
        



    list.sort()
    arena_parameters={
        'traffic_signals':l,'start_node':q,'medicine_packages_present':list
    }

    return arena_parameters
    # print(arena_parameters)


    # cv.waitKey(0)



	# """
	# Purpose:
	# ---
	# This function takes the image as an argument and returns a dictionary
	# containing the details of the different arena parameters in that image

	# The arena parameters are of four categories:
	# i) traffic_signals : list of nodes having a traffic signal
	# ii) horizontal_roads_under_construction : list of missing horizontal links
	# iii) vertical_roads_under_construction : list of missing vertical links
	# iv) medicine_packages : list containing details of medicine packages
	# v)start_node : list containing the start node

	# These four categories constitute the four keys of the dictionary

	# Input Arguments:
	# ---
	# `maze_image` :	[ numpy array ]
	# 		numpy array of image returned by cv2 library
	# Returns:
	# ---
	# `arena_parameters` : { dictionary }
	# 		dictionary containing details of the arena parameters
	
	# Example call:
	# ---
	# arena_parameters = detect_arena_parameters(maze_image)
	# """    
	# arena_parameters = {}

	##############	ADD YOUR CODE HERE	##############

    

	##################################################
	
	# return arena_parameters

# maze_image = cv.imread('maze_1.png')
# print(detect_arena_parameters(maze_image))

# cv.imshow('i',maze_image)

# cv.waitKey()