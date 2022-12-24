# ##Reverse to Make Equal
# Given two arrays A and B of length N, determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.
# Signature
# bool areTheyEqual(int[] arr_a, int[] arr_b)
# Input
# All integers in array are in the range [0, 1,000,000,000].
# Output
# Return true if B can be made equal to A, return false otherwise.
# Example
# A = [1, 2, 3, 4]
# B = [1, 4, 3, 2]
# output = true
# After reversing the subarray of B from indices 1 to 3, array B will equal array A.
import collections
import math
def are_they_equal(a, b):
    # pass
    if len(a) != len(b): return False
    elif sum(a) != sum(b): return False
    else: return True

def are_they_equal1(array_a, array_b):
    counter = collections.Counter(array_a)
    # print(counter)
    for e in array_b:
        # print(e)
        counter[e] -= 1
        # print(counter)
    return not any(filter(lambda x: x != 0, counter.values()))

if __name__ == "__main__":
  n_1 = 4
  a_1 = [1, 2, 3, 4,5]
  b_1 = [1, 4, 3, 2,5]
  print(are_they_equal(a_1, b_1))
  print(are_they_equal1(a_1, b_1))


