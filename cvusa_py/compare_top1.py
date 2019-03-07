# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 22:00:59 2019

@author: yang
"""




with open('result_top1.txt', 'r') as f:
    top1count = 0
    
    for line in f:
        lineA = line.strip().split(',')
        img_name = lineA[0]
        classA = lineA[1]
        classA = str(classA)
        indoor = 'indoor'
        if (classA == indoor):
            print(img_name)
            top1count += 1
#            c = str(count)
#            t = str(len(fb.readline())
    length = len(open('air_semantic_raw.txt').readlines())
    print('The number of same label for air and ground without training is ' + str(top1count) + ' in ' + str(length))