# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:46:02 2019

@author: yang
"""
import cv2
import csv



path = ('/home/yang/cross_view/Data/CVUSA/cvusa_places/air_train' + '/') 

filename = '/home/yang/cross_view/Data/CVUSA/splits/train-19zl.csv'
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        # 行号从1开始
        img_name = (row[0])
        img = cv2.imread(img_name)
        cv2.imwrite(path + img_name[-11:], img)
'''        
        
path = ('/home/yang/cross_view/Data/CVUSA/cvusa_places/ground_train' + '/') 


filename = '/home/yang/cross_view/Data/CVUSA/splits/train-19zl.csv'
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        # 行号从1开始
        img_name = (row[1])
        img = cv2.imread(img_name)
        cv2.imwrite(path + img_name[-11:], img)
'''        
        
 


        