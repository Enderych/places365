# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:31:26 2019

@author: yang
"""


with open('train_unsorted.txt', 'r') as fa:
    with open('train.txt', 'w') as fb:

#with open('val_unsorted.txt', 'r') as fa:
#    with open('val.txt', 'w') as fb:
        result = []
        for line in fa:
            result.append(line)
        fa.close
        result.sort()
        fb.writelines(result)
        fb.close