# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 04:57:04 2019

@author: yang
"""

import os
if not os.path.exists('val/'):
    os.mkdir('val/')
if not os.path.exists('train/'):
    os.mkdir('train/')
os.system("python ./1class2split.py")
os.system("python ./2sort.py")
os.system("python ./3val_extract.py")