#This code emulates in VMWare what the drawing machine
#would do if it had worked

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

edges_template = cv2.Canny(gray,40,45,apertureSize=3,L2gradient=False)
drawing = np.zeros_like(edges_template)

white_pix_count = np.count_nonzero(edges_template)

cv2.imshow('edges_template',edges_template)

#starting position
pos_x = 0
pos_y = 0

#pencil state: 0: pencil raised, 1: pencil lowered
pencil_state = 0

#white_pix_count = np.count_nonzero(edges_template)

while np.count_nonzero(edges_template) > 0:
        #while position is on upper left corner
        while pos_x == 0 and pos_y == 0:
                if edges_template[pos_y,pos_x] == 255 and pencil_state == 0:
                        #if white pix while pencil is raised, lower pencil
                        pencil_state = 1
                if edges_template[pos_y,pos_x] == 255:
                        drawing[pos_y,pos_x] = 255
                #check off pixel as examined
                edges_template[pos_y,pos_x] = 0
                #check for next white pix
                if edges_template[pos_y,pos_x + 1] == 255:
                        #white pix E
                        pos_x = pos_x + 1
                elif edges_template[pos_y + 1,pos_x + 1] == 255:
                       #white pix SE
                        pos_y = pos_y + 1
                        pos_x = pos_x + 1
                elif edges_template[pos_y + 1,pos_x] == 255:
                        #white pix S
                        pos_y = pos_y + 1
                else:
                        #no nearby white pix
                        #check if pencil is raised
                        if pencil_state == 1:
                                #if pencil is lowered, raise pencil
                                pencil_state = 0
                        if np.count_nonzero(edges_template[0,0:639]) != 0:
                                pos_y = 0
                                pos_x = 1
                        elif np.count_nonzero(edges_template[0:479,0]) != 0:
                                pos_y = 1
                                pos_x = 0
                        else:
                                #go to edges_template[1,1]
                                pos_y = 1
                                pos_x = 1
                white_pix_count = np.count_nonzero(edges_template)
                print "white_pix_count: ",white_pix_count
                print "pos_y: ",pos_y
                print "pos_x: ",pos_x
                cv2.imshow('drawing',drawing)
                cv2.waitKey(1)


        #while position is at upper right corner
        while pos_x == 639 and pos_y == 0:
                if edges_template[pos_y,pos_x] == 255 and pencil_state == 0:
                        #if white pix while pencil is raised, lower pencil
                        pencil_state = 1
                if edges_template[pos_y,pos_x] == 255:
                        drawing[pos_y,pos_x] = 255
                #check off pixel as examined
                edges_template[pos_y,pos_x] = 0
                #check for next white pix
                if edges_template[pos_y + 1,pos_x] == 255:
                        #white pix S
                        pos_y = pos_y + 1
                elif edges_template[pos_y + 1,pos_x - 1] == 255:
                        #white pix SW
                        pos_y = pos_y + 1
                        pos_x = pos_x - 1
                elif edges_template[pos_y,pos_x - 1] == 255:
                        #white pix W
                        pos_x = pos_x - 1
                else:
                        #no nearby white pix
                        #check if pencil is raised
                        if pencil_state == 1:
                                #if pencil is lowered, raise pencil
                                pencil_state = 0
                        if np.count_nonzero(edges_template[0,0:639]) != 0:
                                pos_y = 0
                                pos_x = 638
                        elif np.count_nonzero(edges_template[0:479,639]) != 0:
                                pos_y = 1
                                pos_x = 639
                        else:
                                #go to edges_template[1,638]
                                pos_y = 1
                                pos_x = 638
                white_pix_count = np.count_nonzero(edges_template)
                print "white_pix_count: ",white_pix_count
                print "pos_y: ",pos_y
                print "pos_x: ",pos_x
                cv2.imshow('drawing',drawing)
                cv2.waitKey(1)

        #while position is at lower right corner
        while pos_x == 639 and pos_y == 479:
                if edges_template[pos_y,pos_x] == 255 and pencil_state == 0:
                        #if white pix while pencil is raised, lower pencil
                        pencil_state = 1
                if edges_template[pos_y,pos_x] == 255:
                        drawing[pos_y,pos_x] = 255
               #check off pixel as examined
                edges_template[pos_y,pos_x] = 0
                #check for next white pix        
                if edges_template[pos_y,pos_x - 1] == 255:
                        #white pix W
                        pos_x = pos_x - 1
                elif edges_template[pos_y - 1,pos_x - 1] == 255:
                        #white pix NW
                        pos_y = pos_y - 1
                        pos_x = pos_x - 1
                elif edges_template[pos_y - 1,pos_x] == 255:
                        #white pix N
                        pos_y = pos_y - 1
                else:
                        #no nearby white pix
                        #check if pencil is raised
                        if pencil_state == 1:
                                #if pencil is lowered, raise pencil
                                pencil_state = 0
                        if np.count_nonzero(edges_template[479,0:639]) != 0:
                                pos_y = 479
                                pos_x = 638
                        elif np.count_nonzero(edges_template[0:479,639]) != 0:
                                pos_y = 478
                                pos_x = 639
                        else:
                                #go to edges_template[478,638]
                                pos_y = 0
                                pos_x = 0
                white_pix_count = np.count_nonzero(edges_template)
                print "white_pix_count: ",white_pix_count
                print "pos_y: ",pos_y
                print "pos_x: ",pos_x
                cv2.imshow('drawing',drawing)
                cv2.waitKey(1)

        #while position is at lower left corner
        while pos_x == 0 and pos_y == 479:
                if edges_template[pos_y,pos_x] == 255 and pencil_state == 0:
                        #if white pix while pencil is raised, lower pencil
                        pencil_state = 1
                if edges_template[pos_y,pos_x] == 255:
                        drawing[pos_y,pos_x] = 255
                #check off pixel as examined
                edges_template[pos_y,pos_x] = 0
                #check for next white pix
                if edges_template[pos_y,pos_x + 1] == 255:
                        #white pix E
                        pos_x = pos_x + 1
                elif edges_template[pos_y - 1,pos_x] == 255:
                        #white pix N
                        pos_y = pos_y - 1
                elif edges_template[pos_y - 1,pos_x + 1] == 255:
                        #white pix NE
                        pos_y = pos_y - 1
                        pos_x = pos_x + 1
                else:
                        #no nearby white pix
                        #check if pencil is raised
                        if pencil_state == 1:
                               #if pencil is lowered, raise pencil
                                pencil_state = 0
                        if np.count_nonzero(edges_template[479,0:639]) != 0:
                                pos_y = 479
                                pos_x = 1
                        elif np.count_nonzero(edges_template[0:479,0]) != 0:
                                pos_y = 478
                                pos_x = 0
                        else:
                                #go to edges_template[479,1]
                                pos_y = 0
                                pos_x = 0
                white_pix_count = np.count_nonzero(edges_template)
                print "white_pix_count: ",white_pix_count
                print "pos_y: ",pos_y
                print "pos_x: ",pos_x
                cv2.imshow('drawing',drawing)
                cv2.waitKey(1)

        #while position is along left boundary
        while pos_x == 0 and pos_y < 479 and pos_y > 0:
                if edges_template[pos_y,pos_x] == 255 and pencil_state == 0:
                        #if white pix while pencil is raised, lower pencil
                        pencil_state = 1
                if edges_template[pos_y,pos_x] == 255:
                        drawing[pos_y,pos_x] = 255
                #check off pixel as examined
                edges_template[pos_y,pos_x] = 0
                #check for next white pix
                if edges_template[pos_y,pos_x + 1] == 255:
                       #white pix E
                        pos_x = pos_x + 1
                elif edges_template[pos_y + 1,pos_x + 1] == 255:
                        #white pix SE
                        pos_y = pos_y + 1
                        pos_x = pos_x + 1
                elif edges_template[pos_y + 1,pos_x] == 255:
                        #white pix S
                        pos_y = pos_y + 1
                elif edges_template[pos_y - 1,pos_x] == 255:
                        #white pix N
                                pos_y = pos_y - 1
                elif edges_template[pos_y - 1,pos_x + 1] == 255:
                        #white pix NE
                        pos_y = pos_y - 1
                        pos_x = pos_x + 1
                else:
                        #no nearby white pix
                        #check if pencil is raised
                        if pencil_state == 1:
                                #if pencil is lowered, raise pencil
                                pencil_state = 0
                        if np.count_nonzero(edges_template[pos_y,0:639]) != 0:
                                pos_x = 1
                        elif np.count_nonzero(edges_template[0:pos_y,0]) != 0:
                                pos_y = pos_y - 1
                        elif np.count_nonzero(edges_template[pos_y:479,0]) != 0:
                                pos_y = pos_y + 1
                        else:
                                #go to edges_template[pos_y,1]
                                pos_y = pos_y + 1
                                pos_x = 1
                white_pix_count = np.count_nonzero(edges_template)
                print "white_pix_count: ",white_pix_count
                print "pos_y: ",pos_y
                print "pos_x: ",pos_x
                cv2.imshow('drawing',drawing)
                cv2.waitKey(1)

        #while position is along top boundary
        while pos_x < 639 and pos_x > 0 and pos_y == 0:
                if edges_template[pos_y,pos_x] == 255 and pencil_state == 0:
                        #if white pix while pencil is raised, lower pencil
                        pencil_state = 1
                if edges_template[pos_y,pos_x] == 255:
                        drawing[pos_y,pos_x] = 255
                #check off pixel as examined
                edges_template[pos_y,pos_x] = 0
                #check for next white pix
                if edges_template[pos_y,pos_x + 1] == 255:
                       #white pix E
                        pos_x = pos_x + 1
                elif edges_template[pos_y + 1,pos_x + 1] == 255:
                        #white pix SE
                        pos_y = pos_y + 1
                        pos_x = pos_x + 1
                elif edges_template[pos_y + 1,pos_x] == 255:
                        #white pix S
                        pos_y = pos_y + 1
                elif edges_template[pos_y + 1,pos_x - 1] == 255:
                        #white pix SW
                        pos_y = pos_y + 1
                        pos_x = pos_x - 1
                elif edges_template[pos_y,pos_x - 1] == 255:
                        #white pix W
                        pos_x = pos_x - 1
                else:
                        #no nearby white pix
                        #check if pencil is raised
                        if pencil_state == 1:
                                #if pencil is lowered, raise pencil
                                pencil_state = 0
                        if np.count_nonzero(edges_template[0:479,pos_x]) != 0:
                                pos_y = 1
                        elif np.count_nonzero(edges_template[0,0:pos_x]) != 0:
                                pos_x = pos_x - 1
                        elif np.count_nonzero(edges_template[0,pos_x:639]) != 0:
                                pos_x = pos_x + 1
                        else:
                                #go to edges_template[0,pos_x + 1]
                                pos_y = 1
                                pos_x = pos_x + 1
                white_pix_count = np.count_nonzero(edges_template)
                print "white_pix_count: ",white_pix_count
                print "pos_y: ",pos_y
                print "pos_x: ",pos_x
                cv2.imshow('drawing',drawing)
                cv2.waitKey(1)

        #while position is along right boundary
        while pos_x == 639 and pos_y < 479 and pos_y > 0:
                if edges_template[pos_y,pos_x] == 255 and pencil_state == 0:
                        #if white pix while pencil is raised, lower pencil
                        pencil_state = 1
                if edges_template[pos_y,pos_x] == 255:
                        drawing[pos_y,pos_x] = 255
                #check off pixel as examined
                edges_template[pos_y,pos_x] = 0
                #check for next white pix
                if edges_template[pos_y + 1,pos_x] == 255:
                        #white pix S
                        pos_y = pos_y + 1
                elif edges_template[pos_y + 1,pos_x - 1] == 255:
                        #white pix SW
                        pos_y = pos_y + 1
                        pos_x = pos_x - 1
                elif edges_template[pos_y,pos_x - 1] == 255:
                        #white pix W
                        pos_x = pos_x - 1
                elif edges_template[pos_y - 1,pos_x - 1] == 255:
                        #white pix NW
                        pos_y = pos_y - 1
                        pos_x = pos_x - 1
                elif edges_template[pos_y - 1,pos_x] == 255:
                        #white pix N
                        pos_y = pos_y - 1
                else:
                        #no nearby white pix
                        #check if pencil is raised
                        if pencil_state == 1:
                                #if pencil is lowered, raise pencil
                                pencil_state = 0
                        if np.count_nonzero(edges_template[pos_y,0:639]) != 0:
                                pos_x = 638
                        elif np.count_nonzero(edges_template[0:pos_y,639]) != 0:
                                pos_y = pos_y - 1
                        elif np.count_nonzero(edges_template[pos_y:479,639]) != 0:
                                pos_y = pos_y + 1
                        else:
                                #go to edges_template[pos_y + 1,0]
                                pos_y = pos_y + 1
                                pos_x = 638
                white_pix_count = np.count_nonzero(edges_template)
                print "white_pix_count: ",white_pix_count
                print "pos_y: ",pos_y
                print "pos_x: ",pos_x
                cv2.imshow('drawing',drawing)
                cv2.waitKey(1)

        #while position is along bottom boundary
        while pos_x < 639 and pos_x > 0 and pos_y == 479:
                if edges_template[pos_y,pos_x] == 255 and pencil_state == 0:
                        #if white pix while pencil is raised, lower pencil
                        pencil_state = 1
                if edges_template[pos_y,pos_x] == 255:
                        drawing[pos_y,pos_x] = 255
                #check off pixel as examined
                edges_template[pos_y,pos_x] = 0
                #check for next white pix
                if edges_template[pos_y,pos_x + 1] == 255:
                        #white pix E
                        pos_x = pos_x + 1
                elif edges_template[pos_y,pos_x - 1] == 255:
                        #white pix W
                        pos_x = pos_x - 1
                elif edges_template[pos_y - 1,pos_x - 1] == 255:
                        #white pix NW
                        pos_y = pos_y - 1
                        pos_x = pos_x - 1
                elif edges_template[pos_y - 1,pos_x] == 255:
                       #white pix N
                        pos_y = pos_y - 1
                elif edges_template[pos_y - 1,pos_x + 1] == 255:
                        #white pix NE
                        pos_y = pos_y - 1
                        pos_x = pos_x + 1
                else:
                        #no nearby white pix
                        #check if pencil is raised
                        if pencil_state == 1:
                                #if pencil is lowered, raise pencil
                                pencil_state = 0
                        if np.count_nonzero(edges_template[0:479,pos_x]) != 0:
                                pos_y = 478
                        elif np.count_nonzero(edges_template[479,0:pos_x]) != 0:
                                pos_x = pos_x - 1
                        elif np.count_nonzero(edges_template[479,pos_x:639]) != 0:
                                pos_x = pos_x + 1
                        else:
                                #go to edges_template[479,pos_x + 1]
                                pos_y = 478
                                pos_x = pos_x + 1
                white_pix_count = np.count_nonzero(edges_template)
                print "white_pix_count: ",white_pix_count
                print "pos_y: ",pos_y
                print "pos_x: ",pos_x
                cv2.imshow('drawing',drawing)
                cv2.waitKey(1)

        #while position is not on the corners or boundaries
        while pos_x < 639 and pos_x > 0 and pos_y < 479 and pos_y > 0:
                if edges_template[pos_y,pos_x] == 255 and pencil_state == 0:
                        #if white pix while pencil is raised, lower pencil
                        pencil_state = 1
                if edges_template[pos_y,pos_x] == 255:
                        drawing[pos_y,pos_x] = 255
                #check off pixel as examined
                edges_template[pos_y,pos_x] = 0
                #check for next white pix
                if edges_template[pos_y,pos_x + 1] == 255:
                        #white pix E
                        pos_x = pos_x + 1
                elif edges_template[pos_y + 1,pos_x + 1] == 255:
                        #white pix SE
                        pos_y = pos_y + 1
                        pos_x = pos_x + 1
                elif edges_template[pos_y + 1,pos_x] == 255:
                        #white pix S
                        pos_y = pos_y + 1
                elif edges_template[pos_y + 1,pos_x - 1] == 255:
                        #white pix SW
                        pos_y = pos_y + 1
                        pos_x = pos_x - 1
                elif edges_template[pos_y,pos_x - 1] == 255:
                        #white pix W
                        pos_x = pos_x - 1
                elif edges_template[pos_y - 1,pos_x - 1] == 255:
                        #white pix NW
                        pos_y = pos_y - 1
                        pos_x = pos_x - 1
                elif edges_template[pos_y - 1,pos_x] == 255:
                        #white pix N
                        pos_y = pos_y - 1
                elif edges_template[pos_y - 1,pos_x + 1] == 255:
                        #white pix NE
                        pos_y = pos_y - 1
                        pos_x = pos_x + 1
                else:
                        #no nearby white pix
                        #check if pencil is raised
                        if pencil_state == 1:
                                #if pencil is lowered, raise pencil
                                pencil_state = 0
                        if np.count_nonzero(edges_template[pos_y,0:pos_x]) != 0:
                                pos_x = pos_x - 1
                        elif np.count_nonzero(edges_template[pos_y,pos_x:639]) != 0:
                                pos_x = pos_x + 1
                        elif np.count_nonzero(edges_template[0:pos_y,pos_x]) != 0:
                                pos_y = pos_y - 1
                        elif np.count_nonzero(edges_template[pos_y:479,pos_x]) != 0:
                               pos_y = pos_y + 1
                        else:
                                #go to edges_template[pos_y,pos_x + 1]
                                pos_y = pos_y + 1
                                pos_x = pos_x + 1
                white_pix_count = np.count_nonzero(edges_template)
                print "white_pix_count: ",white_pix_count
                print "pos_y: ",pos_y
                print "pos_x: ",pos_x
                cv2.imshow('drawing',drawing)
                cv2.waitKey(1)
        #white_pix_count = np.count_nonzero(edges_template)
        #print "white_pix_count: ",white_pix_count
cv2.imshow('drawing',drawing)
cv2.waitKey(0)
