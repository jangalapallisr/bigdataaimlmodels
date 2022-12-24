#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 08:34:18 2022

@author: s0j01ys, Find Second largest 
"""
"""###According to these rules, the years 2000 and 2400 are leap years,
####while 1800, 1900, 2100, 2200, 2300, and 2500 are not leap years.
print("\n*** IS LEAP YEAR *****")
def is_leap(year):
    leap = False 
    if year in range(1900, pow(10,5)+1):
        ##if (year%4)==0:
        if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
            leap=True   
    return leap

year = int(input('Enter a year to check leap year or not:'))
print(is_leap(year))

print("\m***** PRINT in SINGLE lINE*****")
n = int(input())
if n in range(1,151):
    for i in range(1,n+1):
        print(i,end="")   

print("\n******* RPINT X, Y< Z sum is not N*******")
x = int(input())
y = int(input())
z = int(input())
n = int(input())

print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

print('\n**** FIND Second Largest ******')
n = int(input('ENTER Number for list:'))
arr = map(int, input().split())
lst = list(arr)
if n in range(2, 11) and min(lst)>=-100 and max(lst)<=100:
        print("I'm in IF finally'")
        rev_srt_lst = list(reversed(sorted(lst)))
        mx = max(lst)
        for i in rev_srt_lst:
            if mx == i:
                lst.remove(mx)
            else:
                break
        print(max(lst)) 
else:
        print('Not in Constarints range')
"""
"""
print("\n****If there are multiple students with the second lowest grade*****" )
marks=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    marks.append([name, score])
    #print(marks)
    
print(marks) 
scores = sorted({s[1] for s in marks})  
print(scores)
result = sorted(s[0] for s in marks if s[1] == scores[1])
print(result)
print ('\n'.join(result))
#n = int(input())
#marksheet = [[input(), float(input())] for _ in range(n)]
"""
"""print("*** Find Average Marks *******")
n = int(input('How many Students:'))
student_marks = {}
for _ in range(n):
    name, *line = input('Enter Student Name followed by Marks:').split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input('Enter Student Name wnat to see:')
    
each_marks = student_marks[query_name]
print(i for i in each_marks if i in range(0,100))
#total_marks = sum(each_marks)
#nsubjects = len(each_marks)
#avg=total_marks/nsubjects
#print(round(avg,2))
print(round(sum(each_marks)/len(each_marks),2))
"""
"""
    N = int(input())
    stud_dict = dict()

    for i in range(N):
        tmp = input().split(' ')
        name = tmp[0]
        stud_dict[name] = (float(tmp[1]), float(tmp[2]), float(tmp[3]))
    
    name = input()
    print('%.2f' % (sum(stud_dict[name]) / 3.0))"""
print("***** SHOW how  many Strings get added*****")
print(len(set([str(input("Enter String:")) for x in range(int(input("Enter N:")))])))

"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
"""
"""
##if __name__ == '__main__':
N = int(input())
my_list=list()
for _ in range(N):
        s=input().strip().split(" ")
        if s[0]=="insert":
            my_list.insert(int(s[1]),int(s[2]))
        if s[0]=="print":
            print(my_list)
        if s[0]=="remove":
            my_list.remove(int(s[1]))
        if s[0]=="append":
            my_list.append(int(s[1]))
        if s[0]=="sort":
            my_list.sort()
        if s[0]=="pop":
            my_list.pop()
        if s[0]=="reverse":
            my_list.reverse()
            
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tt=tuple(integer_list)
    print(hash(tt))            
 """
 import re
 m=re.search(r'([a-zA-Z0-9])\1+', "..12345678910111213141516171820212223".strip())

            