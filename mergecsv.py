#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 14:42:45 2022

@author: s0j01ys
"""

import os
import glob
import pandas as pd
#set working directory
os.chdir("/Users/s0j01ys/Desktop/PDD")


extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames)

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
#combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
combined_csv.to_csv( "combined_csv.csv", index=False)