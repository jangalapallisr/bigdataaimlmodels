#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns

dataset=[11,10,12,14,12,15,14,13,15,102,12,14,17,19,107, 10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]
print ('******** SND Standara Normal distribution where mean=0 and std=1  *****')
outliers=[]
def find_otlieres(data):
    thresold=3 ##till 3rd std as per BSME, will change if required
    mean=np.mean(data)
    std=np.std(data)
    
    for i in data:
        zscore =(i-mean)/std
        if zscore > thresold:
            outliers.append(i)
    return outliers

outliers_pt=find_otlieres(dataset)
print(outliers_pt)   


## MEAN & MODE are different on specfic feature/input varaiable then there is out lierss in data
mean=np.mean(dataset)
median=np.median(dataset)
diff=np.abs(mean-median) 
print ('Mean',mean, '  Median:',median, ' & difference is:', diff)


plt.hist(dataset)  ## hist plt helps to see data nomarlly distributed or not
sns.histplot(dataset)

plt.boxplot(dataset)  ## box plot helps to see outliers out of box
sns.boxplot(dataset)

sns.countplot(dataset)
sns.barplot(dataset)
#sns.heatmap(dataset)

print ('***** IQR *******')
### IQR 
#1. sort the data
#2. calucluate Q1 & Q3
#3. IQR(q3-q1)
#4. Find the lower fence/line (q1-1.5(iqr))
#5. Find the upper fence/line (q3+1.5(iqr))
#6. Remeve/speratae the elemenets from data set whose are out of LOWER & UPPER Fence range
dataset=sorted(dataset)
q1,q3 = np.percentile(dataset,[25,75])
print (q1, q3)
iqr = q3-q1
lower_fence = q1-1.5*iqr
upper_fence = q3+1.5*iqr
print ('IQR:',iqr, ' LOWER FENCE:',lower_fence, ' & Upper fence:',upper_fence)
## for loop