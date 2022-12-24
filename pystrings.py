#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 17:47:43 2022

@author: s0j01ys
"""
test="Hello  \"there'"
print(test)
text="PythonP"
print(text)
print(text[3])
#text[0]="R"    ##TypeError: 'str' object does not support item assignment - LIKE TuPLE, its immutable
print(text)
revtest=reversed(text)
print(text.replace('P', 'R'))

new_text=text * 3
print(new_text)

print(dir(text))
print(len(text))
for char in text:
    print(char)
print("P" in text)
print("yth" in text)
print("ont" in text)

text_tx= "I like Python 3 Python 3 its Python"
print(text_tx)
print(text_tx.lower())
print(text_tx.upper())
print(text_tx.replace("3", "4"))

## replace last occurance of character
original_string = "sentence one. sentence two. sentence three"

last_char_index = original_string.rfind(".")
new_string = original_string[:last_char_index] + "," + original_string[last_char_index+1:]
print(new_string)
## Replace last occurancy of string
lst=text_tx.count("Python")
print(lst)
new_text=text_tx.replace("Python", "Rython", lst)
print(new_text)


print("""***** Python Dictionaries *****""")
## K, V pair, K keys are immutable objects and where V values mutable/can changble
person={"Name":'Subbu', "Age":42}
print(person)
print(person["Age"])
person1={10:'Subbu', ("Age"):42}
print(person1)
print(person1[10])
#print(person1[15])  ## KeyError: 15
print(person1.get(15, "NO KEYFOUND"))
person1[10]="Reddy"
print (person1)
person1[15]=["Dancing","Fishing"]
print(person1)
print(person1.pop(10))
print(person1)
for k in person1:
    print(k)
    print(person1[k])
a=[1,4,2,4,3,5,6,4,5]
import collections
results = collections.Counter(sorted(a))
for (k,v) in results.items():
    print (k,"->",v)
    
print(dir(a))
print(dir(person1))
print("""\n\n***** Python  SETS collection of Tuples and No Duplictes and immutable objects *****""")
animals={"dog","pig","dog","Elephant"}
print(animals)


    