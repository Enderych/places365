# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 20:35:49 2019

@author: yang
"""


import numpy as np
import pandas as pd
 
txt = np.loadtxt('ground_semantic.txt')
txtDF = pd.DataFrame(txt)
txtDF.to_csv('ground_semantic.csv',index=False)

txt2 = np.loadtxt('air_semantic_raw.txt')
txtDF2 = pd.DataFrame(txt2)
txtDF2.to_csv('air_semantic_raw.csv',index=False)