import itertools
def getWrongAnswers(N: int, C: str) -> str:
    return (''.join('A' if i =='B' else 'B' for i in C))


if __name__ == '__main__':
    # N=3
    # C="ABA"
    N = 5
    C ="BBBBB"
    print(getWrongAnswers(N,C))

    ##TEST CHECK zip() and enumerate(), zip is value based, enumerator is index based.
    l1 = ['A','B','C']
    l2 =[1,2,3,4]
    lz= zip(l1,l2)
    for i in lz:
        print(i)
    lrz = zip(l2,l1)
    for i in lrz:
        print(i)
    le = enumerate(l1)
    for i in le:
        print(i)
    l1z = zip(l1)
    for i in l1z:
        print(i)
        # What is the difference between %, /, and // ?
    print(11 % 2)  ##       % is the modulus operator that returns a remainder after the division.
    print((11 / 2))  ##       / is the operator that returns the quotient after the division.
    print(11 // 2)  ##       // is the floor division that rounds off the quotient to the bottom.
    print("****LAMBDA******")
# ## Lambda functions are an anonymous or nameless function.
# These functions are called anonymous because they are not declared in the standard manner by using the def  keyword. It doesn’t require the return keyword as well. These are implicit in the function.
# The function can have any number of parameters but can have just one statement and return just one value in the form of an expression. They cannot contain commands or multiple expressions.
# An anonymous function cannot be a direct call to print because lambda requires an expression.
# Lambda functions have their own local namespace and cannot access variables other than those in their parameter list and those in the global namespace

    x = lambda i,j:i+j  ## no NAME, no DEF keyword for method, & RETURN Type
    print(x(5,4))
    print("**** MAP *****")
## The map() function iterates through all items in the given iterable and executes the function we passed as an argument on each of them.
## The Sysntax is:
    # map(function, iterable(s))
    # map(datatype, iterable)
    def starts_with_A(s):
        return s[0] =='A'   ## To check
    fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
    map_object = map(starts_with_A,fruit)
    print(list(map_object))

    map_object = map(int, range(1,12))
    print(list(map_object))
    print(list(map_object)) ## In Python any object traverse till end next will be an empty
    print("***** FILTER ******")
## Similar to map(), filter() takes a function object and an iterable and creates a new list.
## As the name suggests, filter() forms a new list that contains only elements that satisfy a certain condition, i.e. the function we passed returns True.
## The syntax is:
    #filter(function, iterable(s))
    FILETR_OBJECT = filter(starts_with_A, fruit)
    print(list(FILETR_OBJECT))
    print(list(FILETR_OBJECT))
    # FILETR_OBJECT = filter(int, lambda : i%2 ==0 for i in range(1,15))
    # FILETR_OBJECT.seek(0)
    # FILETR_OBJECT.__next__(0)
    print(list(FILETR_OBJECT))
    # print(list(itertools.cycle(FILETR_OBJECT)))
    # l2 = list.index(FILETR_OBJECT,0)
    # print(l2)
    FILETR_OBJECT = filter(starts_with_A, fruit)
    print(list(FILETR_OBJECT))
    # class myiterator(object):
    #     def __init__(self):
    #         self.reset()
    #     def reset(self):
    #         self.reset =0
    #     def __iter__(self):
    #         return self
    # myiter = myiterator()
    # myiter= myiterator.reset(FILETR_OBJECT)
    print(list(FILETR_OBJECT))
print("***** REDUCE *****")
# reduce() works differently than map() and filter(). It does not return a new list based on the function and iterable we've passed. Instead, it returns a single value.
# Also, in Python 3 reduce() isn't a built-in function anymore, and it can be found in the functools module.
from functools import reduce
def add(x, y):
    return x + y
list = [2, 4, 7, 3]
print(reduce(add, list))

print(reduce(lambda x, y: x + y, list))
print("With an initial value: " + str(reduce(lambda x, y: x + y, list, 10)))
print("****** RANGE, XRANGE, & ARANGE")
# range(): returns a Python list object, which is of integers. It is a function of BASE python.
# xrange(): returns a range object.
# arange(): is a function in Numpy library. It can return fractional values as well.

# range(): range(1, 10) returns a list from 1 to 10 numbers & hold whole list in memory.
# xrange(): Like range(), but instead of returning a list, returns an object that generates the numbers in the range on demand.
# For looping, this is lightly faster than range() and more memory efficient.
# xrange() object like an iterator and generates the numbers on demand.(Lazy Evaluation)
import timeit
t1 = timeit.default_timer()
for i in range(1,10000000):
    pass
t2 = timeit.default_timer()
print(t2 -t1)
# t1 = timeit.default_timer()
# for i in xrange(1,10000000):
#     pass
# t2 = timeit.default_timer()
# print(t2 -t1)
print("There is No XRANGE in python 3")