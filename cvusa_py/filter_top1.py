# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 20:00:06 2019

@author: yang
"""



with open('air_semantic_raw.txt', 'r') as fa:
    with open('ground_semantic.txt', 'r') as fb:
        with open('result_top1.txt', 'w') as fc:
            top1count = 0
            indoor_count_air = 0
            indoor_count_ground = 0
            for line in fa:
                lineA = line.strip().split(',')
                lineB = fb.readline().strip().split(',')
                img_name = lineA[0]
                classA = lineA[1]
                classB = lineB[1]
                topA1 = lineA[2]
                topA1 = topA1[:-7]
                fc.write(img_name[-11:] + ',' + classA + ',' + classB + ',' + topA1 + ',')
                topB1 = lineB[2]
                topB1 = topB1[:-7]
                fc.write(topB1 +'\n')
                if (topA1 == topB1):
#                    print(img_name)
                    top1count += 1
                if (classA == ' indoor'):
                    indoor_count_air += 1
                if (classB == ' indoor'):
                    indoor_count_ground += 1
#            c = str(count)
#            t = str(len(fb.readline())
            length = len(open('air_semantic_raw.txt').readlines())
            print('The number of same top1 label for air and ground without training is ' + str(top1count) + ' in ' + str(length))
            print('Number of air image was wrong classified to indoor: ' + str(indoor_count_air))
            print('Number of ground image was wrong classified to indoor: ' + str(indoor_count_ground))