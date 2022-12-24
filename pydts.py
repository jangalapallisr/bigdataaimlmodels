#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 15:59:16 2022

@author: s0j01ys
"""
## Lists
list= [1,2,5,3,4,4,5,6,2.5,4.54,"Subbu",True]
print(list)
print(type(list))
print(list[:]) ## from staring position 0 to n-1
print(len(list))
print(list[2:5]) ## pos 2 to 5 index starting with 0
print(list[-1:]) ## last one -1
print(list[11:]) ## last one in list
print(list[len(list)-1:]) ## last one in list
print(list[::-1])  # print reverse
print(list)
##print(sorted(list))  ## sort wokrs on similar data types works int & float, won't work with str
list1=["Subbu","Kshrugal","Bindu"]
print(sorted(list1))
list2=[2,4,3,5,4,5,3.5,2.3,-4,-3,4]
print(sorted(list2))

import numpy as np
arr= np.array([1,3,4,6,7,2,4])
## To use arrays in Python, you need to import either an array module or a NumPy
#import array as arr
#or import numpy as np
print(arr)
print(type(arr))
print(len(arr))

array_div = arr/2
print(array_div)
## you can divide each element of an array by the same number with just one line of code. If you try the same with a list, you'll get an error.
#list_div=list2/2
#print(list_div)
print("Bindu" in list1)
print(7 in arr)
print(4 in arr)
list1.append("Jangalapalli")
list1.insert(1,"YTL")
print(list1)
print(list.pop(3))
print(list)
'''
The remove() function removes the first matching value from the list.
The pop() function is used to return the removed element from the list.
The del() function is used to delete an element at a specified index number in the list. and range of index: example
want to delete from index 4 to 8 del list[4:8]
'''
print("Tuple & List are same except the Tuple is immutable, list is mutable/changeble")
list_num = [1,2,3,4]
tup_num = (1,2,3,4)

print(list_num)
print(tup_num)
print(type(list_num)) ## type tellls what type of object
print(type(tup_num))

list_num[2] = 5
print(list_num)

##tup_num[2] = 5   ##TypeError: 'tuple' object does not support item assignment

print(dir(list_num)) ## dir to show list all methods
print(id(list_num)) ## its memory location unique id
print(dir(tup_num))
print(len(tup_num))