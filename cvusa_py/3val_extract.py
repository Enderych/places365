# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 23:04:24 2019

@author: yang
"""

import os
import cv2


path = ('/home/yang/cross_view/Data/CVUSA' + '/')
with open('class_sorted.txt', 'r') as fa:
    with open('train.txt', 'w') as fb:
        with open('val.txt', 'w') as fc:
            count = 0
            
            for (num, line) in enumerate(fa):
                if (num%5 == 0):
                    line=line.strip('\n')
                    img = cv2.imread(path + line)
                    class_name = line[6:-12]
                    img_name = line[-11:]
                    if not os.path.exists('val/' + class_name):
                        os.mkdir('val/' + class_name)
                    cv2.imwrite(path + 'val/' + class_name + '/' + img_name, img)
                    fc.write('val/' + class_name + '/' + img_name + '\n')
                    os.remove(path + line)
                else:
                    fb.write(line)
                
                