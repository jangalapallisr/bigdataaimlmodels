#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings("ignore")
import re

##60 -70
print("0 :",ord('0')," 9:",ord('9'))
print("a :",ord('a')," z:",ord('z'))
print("A :",ord('A')," Z:",ord('Z'))

# decoder = (("a".."z").zip(("a".."z").to_a.rotate k) + ("A".."Z").zip(("A".."Z").to_a.rotate k)).to_h
# print s.chars.map{|c| decoder.include?(c) ? decoder[c] : c}.join
# print("******* CIPHER ROTATIONAL ********")
s = "Sr _ J35s'r"
k = 2
strlst = list(s)
dstrlst = []
for c in strlst:
    if c.isalnum:
        if c.isdigit():
            c = chr((ord(c) - ord('0') + k) % 10 + ord('0'))
        elif c.islower():
            c = chr((ord(c) - ord('a') + k) % 26 + ord('a'))
        elif c.isupper():
            c = chr((ord(c) - ord('A') + k) % 26 + ord('A'))
        # else:  ## WILL NOT WORK if string has special characters since its fall into this block and raise exceptions.
        #     raise Exception("Invalid ALPHANUM character")
    dstrlst.append(c)
# return ''.join(dstrlst)
print(''.join(dstrlst))
# def caesarCipher(s, k):
#     # Write your code here
#     strlst = list(s)
#     dstrlst = []
#     for c in strlst:
#         if c.isalnum:
#             if c.isdigit():
#                 c = chr((ord(c) - ord('0') + k)%10 + ord('0'))
#             elif c.islower():
#                 c = chr((ord(c) - ord('a') + k)%26 + ord('a'))
#             elif c.isupper():
#                 c = chr((ord(c) - ord('A') + k)%26 + ord('A'))
#             # else:
#             #     raise Exception("Inavalid AlphaNumeric")
#         dstrlst.append(c)
#     return ''.join(dstrlst)
#



