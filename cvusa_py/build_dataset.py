# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 23:01:49 2019

@author: yang
"""

import os
import cv2


path = ('/home/yang/cross_view/Data/CVUSA/cvusa_places/air_val' + '/')
with open('ground_val.txt', 'r') as fa:
    with open('val_unsorted.txt', 'w') as fb:
        

#path = ('/home/yang/cross_view/Data/CVUSA/cvusa_places/air_train' + '/')
#with open('ground_train.txt', 'r') as fa:
#    with open('train_unsorted.txt', 'w') as fb:        
        
        count = 0
        for line in fa:
            lineA = line.strip().split(',')
            img_name = lineA[0][-11:]
            topA1 = lineA[2][1:-7]
#            topA2 = lineA[3][1:-7]
#            topA3 = lineA[4][1:-7]
#            topA4 = lineA[5][1:-7]
#            topA5 = lineA[6][1:-7]
            if topA1.count('/'):
                count += 1
                print (img_name + ',' + topA1)
            topA1 = topA1.replace('/','-')
            if not os.path.exists('val/' + topA1):
                os.mkdir('val/' + topA1)
            img = cv2.imread(path + '/' + img_name)
            cv2.imwrite('val/' + topA1 + '/' + img_name, img)
            fb.write('val/' + topA1 + '/' + img_name + '\n')
            
            """
            if not os.path.exists('train/' + topA1):
                os.mkdir('train/' + topA1)
            img = cv2.imread(path + '/' + img_name)
            cv2.imwrite('train/' + topA1 + '/' + img_name, img)
            fb.write('train/' + topA1 + '/' + img_name + '\n')            
            """
        print(count)

