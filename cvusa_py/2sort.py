# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 23:13:16 2019

@author: yang
"""

with open('class.txt', 'r') as fa:
    with open('class_sorted.txt', 'w') as fb:

#with open('val_unsorted.txt', 'r') as fa:
#    with open('val.txt', 'w') as fb:
        result = []
        for line in fa:
            result.append(line)
        fa.close
        result.sort()
        fb.writelines(result)
        fb.close