# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 22:36:59 2019

@author: yang
"""




with open('air_semantic_raw.txt', 'r') as fa:
    with open('ground_semantic.txt', 'r') as fb:
        with open('result_top5.txt', 'w') as fc:
            top1count = 0
            indoor_count_air = 0
            indoor_count_ground = 0
            for line in fa:
                lineA = line.strip().split(',')
                lineB = fb.readline().strip().split(',')
                img_name = lineA[0]
                classA = lineA[1]
                classB = lineB[1]
                topA1 = lineA[2][:-7]
                topA2 = lineA[3][:-7]
                topA3 = lineA[4][:-7]
                topA4 = lineA[5][:-7]
                topA5 = lineA[6][:-7]
                list_a = [topA1, topA2, topA3, topA4, topA5]
                fc.write(img_name[-11:] + ',' + classA + ',' + classB + ',' + topA1 + ',' + topA2 + ',' + topA3 + ',' + topA4 + ',' + topA5 + ',')
                topB1 = lineB[2][:-7]
                topB2 = lineB[3][:-7]
                topB3 = lineB[4][:-7]
                topB4 = lineB[5][:-7]
                topB5 = lineB[6][:-7]
                list_b = [topB1, topB2, topB3, topB4, topB5]
                set_c = set(list_a) & set(list_b)
                list_c = list(set_c)
                fc.write(topB1 + ',' + topB2 + ',' + topB3 + ',' + topB4 + ',' + topB5 + '\n')
                if (list_c):
#                    print(img_name)
                    top1count += 1
                if (classA == ' indoor'):
                    indoor_count_air += 1
                if (classB == ' indoor'):
                    print(img_name[-11:] + ',' + classB + ',' + topB1)
                    indoor_count_ground += 1
#            c = str(count)
#            t = str(len(fb.readline())
            length = len(open('air_semantic_raw.txt').readlines())
            print('The number of same top5 label for air and ground without training is ' + str(top1count) + ' in ' + str(length))
            print('Number of air image was wrong classified to indoor: ' + str(indoor_count_air))
            print('Number of ground image was wrong classified to indoor: ' + str(indoor_count_ground))