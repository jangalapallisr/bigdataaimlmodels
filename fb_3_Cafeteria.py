# A cafeteria table consists of a row of NN seats, numbered from 11 to NN from left to right.
# Social distancing guidelines require that every diner be seated such that KK seats to their left and KK seats to their right (or all the remaining seats to that side if there are fewer than KK) remain empty.
# There are currently MM diners seated at the table, the iith of whom is in seat Si
# No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.
# Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.

# Sample test case #1
N = 10
K = 1
M = 2
S = [2, 6]
# (N/2K)-M = 5 -2=3,
# Expected Return Value = 3
# Sample test case #2
# N = 15
# K = 2
# M = 3
# S = [11, 6, 14]
#(N/2K) - M = 15/4=3.77 -3 =ROUNDUP
# Expected Return Value = 1
# Sample Explanation
# In the first case, the cafeteria table has N = 10 seats, with two diners currently at seats 2 and 6 respectively.
# The table initially looks as follows, with brackets covering the K = 1 seat to the left and right of each existing diner that may not be taken.
#   1 2 3 4 5 6 7 8 9 10
#   [   ]   [   ]
# Three additional diners may sit at seats 4, 8, and 10 without violating the social distancing guidelines.
# In the second case, only 11 additional diner is able to join the table, by sitting in any of the first 33 seats.

from typing import List
import math

# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    print(N,":", K,":", M,":", S)
    total_prability = N / (2*K)
    print(total_prability)
    # print(math.ceil(3/3))
    # print(math.ceil(1/3))
    # if (N/2) == 0:
    #     possibility = math.floor(total_prability - M)
    #     print(possibility)
    #     return possibility
    # else:
    #     possibility = math.ceil(total_prability - M)
    #     print(possibility)
    #     return possibility
    S.sort()
    start, res = 1, 0
    S.append(N + K + 1)  # 10+1+1=12 15+2+1=18
    for s in S:
        print(s)
        delta = s - K - start  # 2-1-1=0,6-1-(2+1+1)=1; ceil(0.5); 6+1+1=8, 12-1-8=3,ceil(1.5)=2 ==>1+2=3
        # 6-2-1=3,ceil(3/3)=1; 11-2-9=0;14-2-14=-2; 18-2-17=-1
        if delta > 0:
            res += math.ceil(delta / (K + 1))
        start = s + K + 1
    return res
if __name__ == '__main__':
    # pass
    print(getMaxAdditionalDinersCount(N,K,M,S))