##1. [1,3,1,4,23] & 8, contigeous elements make target?
##2. "aabbaab" or "abc" - how many palidorm strings can be made?
test_str="abc"
test_str="aabbaab"
print("The original string is : " + str(test_str))

# Get all substrings of string
# Using list comprehension + string slicing
res = [test_str[i: j] for i in range(len(test_str))
       for j in range(i + 1, len(test_str) + 1)]

# printing result
print("All substrings of string are : " + str(res))
palidromcnt=0
for i in res:
    if len(i)==1: palidromcnt +=1
        # print(i,":",palidromcnt)
    else:
        # print(str(i), str(i)[::-1])
        if str(i) == str(i)[::-1]: palidromcnt +=1
print(palidromcnt)
###############


def check(arry, trgt):
    if sum(arry) < trgt: raise Exception("Invalid")
    elif sum(arry) == trgt: return True
    else:
        for i in range(len(arry)):
            for j in range(i+1, len(arry)+1):
                if sum(arry[i:j]) == trgt: return True
        return False

arry = [1, 3, 1, 4, 23]
trgt = 8
print(check(arry,trgt))