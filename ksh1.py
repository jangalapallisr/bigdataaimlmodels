#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 21:46:01 2022

@author: s0j01ys
"""
print("Hello BWHS world....!")
print("==========FOR LOOP=============" )  
for i in range(5,10,2):
    print("i-->:",i)
print("==========WHILE LOOP=============" )   
j=0    
while j <= 5:  
    print("J:-->",j)
    j = j+1 ##j++
     
print("==========WHILE LOOP WITh IF CONDITION=============" )  
lname ="Jangalapalli"
print(str.upper(lname))
while True:
    lreadval = str.upper(input("Enter your last name:"))
    #if str.upper(lname) == str.upper(lreadval):
    if str.upper(lname) == lreadval:
        print("Hey uhrry we are jangalallaa Family:",lreadval)
        break 
    else:
        print("heel your not our Family::@#%%^^*&&",lreadval)    
        
print("**====== DOESNOT EQUEAL ======###")
i=5    
while i != 0:
    print("While,,..i-->:",i)
    i=i-1
print("")
for i in range(5,0,-1):
    print("Foree,,,.i-->:",i)
    