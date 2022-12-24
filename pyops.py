#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings("ignore")
import collections
import numpy as np

a =[1,2,3,4,3,4,3,4,3]
print(a)
## Count no.of occurances
results = collections.Counter(a)
print('Number of occuranccies')
for (key, val) in results.items():
    print (key,"->",val)
print() ## will not do anything
print('Length of Array:',len(a)) 
print('Sum of array:',sum(a))
print('Sort of A',sorted(a))
b=a.copy()
a.sort
print('Sorting Array:',a)
print('b is;', b)
## how to reverse an array  
rev_arr=a[::-1]        #option-1 reversing using array slicing
print(rev_arr)
a.reverse()       #option-2
print(a)
rvl_a=list(reversed(a))      #option-3
print((rvl_a))
## Using numpy module
res_arr=np.flip(a)   #Option -4 #reversing using flip() Method
print (res_arr)
res_arr1=np.flipud(a)     #option-5 reversing using flipud() Method
print (res_arr1)


number=int(input('Enter Number:'))   
for i in range(1,11,1):
    print (number,"X",i,"=", number*i)
print("======Backwards=======")
for i in range(10,0,-1):
    print (number,"X",i,"=", number*i)

print("breaak, continue & pass")

### PYTHON PASSS STATEMENT - It is used as a placeholder for future implementation of functions, loops, etc.
nbr=35
if nbr > 0.0:
    pass
if nbr > 5:
    print (True)
#if nbr > 5:
    ## todo, will figure it it out later --->will expect z EOF or indented block
print('The End with PASS loop') 
for i in range(3):
    n=int(input('Enter number :'))
    if n < 0:
        print('-ve')
        break
print('The End with break loop')    
for i in range(3):
    n=int(input('Enter number :'))
    if n < 35:
        print('Failed')
        continue
print('The End with continue loop') 

print('**** BREAK vs RETURN*****')
def test_break():
    for n in range(5):
        if n == 3 :
            break 
        print (n)
print('The End with break loop:',test_break())    
def test_return():
    for n in range(5):
        if n == 3 :
            return n
        print (n)
print('The End with return loop:',test_return()) 