#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 17:18:50 2022

@author: s0j01ys
"""
import warnings
warnings.filterwarnings("ignore")

class student:
    def __init__(self, name,marks):
        self.name=name
        self.marks=marks
        
    def check_pass_fail(self):
        if self.marks >40:
            return True
        else:
            return False

student1=student("SR",35)
student2=student("Bin", 65)        
student3=student("Ksh", 95)
print(student1.name, student1.marks, student1.check_pass_fail())
print(student2.name, student2.marks, student2.check_pass_fail())
print(student3.name, student3.marks, student3.check_pass_fail())

class complex:
    def __init__(self, real, imag):
        self.real=real
        self.imag=imag
        
    def add(self,num):
        real=self.real + num.real
        imag=self.imag + num.imag
        result=complex(real,imag)
        return result
n1=complex(5, 6)
n2=complex(-4, 2)
result = n1.add(n2)
print("Real:", result.real)
print("Imag:", result.imag)